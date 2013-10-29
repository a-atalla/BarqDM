# -*- coding: utf-8 -*-
#
# <A PySide Gui for Aria2 Download Manager>
# Copyright (C) 2013  a.atalla <a.atalla@hacari.org>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
#
from PySide.QtCore import Slot
from PySide import QtGui,QtCore
from gui.Ui_MainWindow import Ui_MainWindow
from NewDownload import NewDownload
from LimitDialog import LimitDialog
from Aria2Manager import Aria2Manager
import pprint as p

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)
		self.showMaximized()
		self.aria = Aria2Manager()
		self.aria.startAria2()
		if self.aria.isRunning():
			self.fillCategories()
			self.timer = QtCore.QTimer(self)
			self.timer.start(2000)
			self.connect(self.timer,QtCore.SIGNAL("timeout()"), self.refreshView)
		else:
			self.setWindowTitle('Barq Download Manager (Offline)')
		
		self.trayIcon()	
		##Setting the columns sizes
		self.tblActive.setColumnWidth(0,150)
		self.tblActive.setColumnWidth(1,300)
		self.tblActive.setColumnWidth(2,100)
		self.tblActive.setColumnWidth(3,150)
		self.tblActive.setColumnWidth(4,150)
		self.tblActive.setColumnWidth(5,100)
		
		self.tblUris.setColumnWidth(0,800)
		self.tblUris.setColumnWidth(1,150)
		
		## The Right-click menu
		self.menuRC = QtGui.QMenu()
		self.menuRC.addAction(self.actionPause)
		self.menuRC.addAction(self.actionStart)
		self.menuRC.addAction(self.actionRemoveDownload)
		self.menuRC.addAction(self.actionDownloadLimit)
		self.tblActive.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.connect(self.tblActive, QtCore.SIGNAL('customContextMenuRequested(const QPoint&)'), self.showMenuRC)   
		

		
	@Slot()
	def on_actionQuit_triggered(self):
		self.close()
		
	@Slot()
	def on_actionNewDownload_triggered(self):
		newDlg = NewDownload()
		newDlg.exec_()
	
	@Slot()
	def on_actionStart_triggered(self):
		self.aria.unpauseSingleDownload(self.selectedGid())

	@Slot()
	def on_actionStartAll_triggered(self):
		self.aria.unpauseAllDownloads()

	@Slot()
	def on_actionPause_triggered(self):
		self.aria.pauseSingleDownload(self.selectedGid())
		
	@Slot()
	def on_actionPauseAll_triggered(self):
		self.aria.pauseAllDownloads()

	@Slot()
	def on_lwCategories_itemClicked(self):
		print self.lwCategories.currentItem().text()
	
	@Slot()
	def on_cboxGlobalSpeed_currentIndexChanged(self):
		speed = self.cboxGlobalSpeed.currentText().split()[0]
		if speed=='Unlimited':
			speed = '0'
		self.aria.changeGlobalOption({'max-overall-download-limit':speed+'K'})

		
	@Slot()
	def on_actionDownloadLimit_triggered(self):
		limitDlg = LimitDialog(self.selectedGid())
		limitDlg.exec_()
		
	@Slot()
	def on_actionRemoveDownload_triggered(self):
		msgBox = QtGui.QMessageBox()
		msgBox.setText('Remove Download!')
		msgBox.setInformativeText('Are You Sure ?')
		msgBox.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		msgBox.setDefaultButton(QtGui.QMessageBox.Save)
		ret = msgBox.exec_()
		if ret==QtGui.QMessageBox.Yes:
			self.aria.removeSingleDownload(self.selectedGid())
			self.tblActive.removeRow(self.tblActive.selectionModel().currentIndex().row())
		
	@Slot()
	def on_actionCleanList_triggered(self):
		self.aria.cleanDownloadList()
	
	@Slot()
	def on_tblActive_itemSelectionChanged(self):	
		self.urisTimer = QtCore.QTimer(self)
		self.urisTimer.start(2000)
		self.connect(self.urisTimer,QtCore.SIGNAL("timeout()"), self.viewUris)
		
	def closeEvent(self,event):
		self.aria.stopAria2()
		
	def trayIcon(self):
		self.trayicon=QtGui.QSystemTrayIcon(QtGui.QIcon(':images/icons/barq.png'))
		self.trayicon.show()
		self.menu=QtGui.QMenu()
		self.menu.addAction(self.actionPauseAll)
		self.menu.addAction(self.actionStartAll)
		self.menu.addAction(self.actionQuit)
		self.trayicon.setContextMenu(self.menu)
		self.trayicon.activated.connect(self.onTrayIconActivated)
	
	def onTrayIconActivated(self, reason):
		if reason == QtGui.QSystemTrayIcon.DoubleClick:
			if self.isVisible():
				self.hide()
			else:
				self.show()  

	def fillCategories(self):
		global_status = self.aria.getGlobalStatus()
		self.lwCategories.clear()
		item = QtGui.QListWidgetItem('Active Downloads ('+global_status['numActive']+')',self.lwCategories)
		item.setIcon(QtGui.QIcon(':images/icons/media-playback-start.png'))
		item = QtGui.QListWidgetItem('Waiting Downloads ('+global_status['numWaiting']+')',self.lwCategories)
		item.setIcon(QtGui.QIcon(':images/icons/media-playback-pause.png'))
		item = QtGui.QListWidgetItem('Stopped Downloads ('+global_status['numStopped']+')',self.lwCategories)
		item.setIcon(QtGui.QIcon(':images/icons/media-playback-stop.png'))
	
	def viewActive(self):
		activeList  = self.aria.getAllGids()[0]
		waitingList = self.aria.getAllGids()[1]
		stoppedList = self.aria.getAllGids()[2]
		allList = activeList+waitingList+stoppedList
		if self.tblActive.rowCount() > len(allList):
			self.tblActive.clearContents()
			self.tblActive.setRowCount(self.tblActive.rowCount()-1)
		for active in allList:
			i=allList.index(active)
			gid = active.get('gid')
			data =  self.aria.getDownloadStatus(gid)
			# [gid,filename,status,size,dsize,speed]
			size= str(round(float(data[3])/1000000,2))+' Mb'
			speed  = str(round(float(data[5])/1000,2))+' Kb/sec'
			try:
				progress = round(float(data[4])*100/float(data[3]),2)
			except:
				progress =0
				
			try: # To avoid dividing by zero until connect to the server
				RemainingTime = (float(data[3])-float(data[4]))/float(data[5])
				remainingTime = round (RemainingTime/(3600),2) #Hour Format
				timeFormat = '  Hr'
				if remainingTime < 1 :
					remainingTime = round (RemainingTime/(60),2) #Min Format
					timeFormat = '  Min'
					if remainingTime < 1 :
						remainingTime = round (RemainingTime,2) #Sec Format
						timeFormat = '  Sec'
			except:
				remainingTime = ''
				timeFormat=''
				
			if self.tblActive.rowCount() < len(allList):
				self.tblActive.setRowCount(self.tblActive.rowCount()+1)

				
			pbar = QtGui.QProgressBar()
			pbar.setRange(0,100) # The range is from 0  to Size
			pbar.setValue(progress)			# The value is the dsize which is completedLength
			self.tblActive.setItem(i,0,QtGui.QTableWidgetItem(data[0]))
			self.tblActive.setItem(i,1,QtGui.QTableWidgetItem(data[1]))
			self.tblActive.setItem(i,2,QtGui.QTableWidgetItem(data[2]))
			self.tblActive.setItem(i,3,QtGui.QTableWidgetItem(size))
			self.tblActive.setCellWidget(i,4,pbar)
			self.tblActive.setItem(i,5,QtGui.QTableWidgetItem(speed))
			self.tblActive.setItem(i,6,QtGui.QTableWidgetItem(str(remainingTime)+timeFormat))
			self.tblActive.setRowHeight(i,22)
			for j in range(0,7):
				if not j==4:
					self.tblActive.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
					if data[2]=='error' or data[2]=='removed' :
						self.tblActive.item(i,j).setBackground(QtCore.Qt.red)
					elif data[2]=='complete':
						self.tblActive.item(i,j).setBackground(QtCore.Qt.green)

	def selectedGid(self):
		selectedRow =  self.tblActive.selectionModel().currentIndex().row()
		gid =str(self.tblActive.item(selectedRow,0).text())
		return gid
	
	def viewUris(self):
		self.btmTab.setTabText(0,self.tblActive.item(self.tblActive.currentRow(),1).text())

		uris = self.aria.getUrisDetails(self.selectedGid())
		if self.tblUris.rowCount()<len(uris):
			self.tblUris.setRowCount(len(uris))
			self.tblUris.clearContents()
		i=0
		for i in range(0,len(uris)):
			self.tblUris.setItem(i,0,QtGui.QTableWidgetItem(uris[i]['uri']))
			self.tblUris.setItem(i,1,QtGui.QTableWidgetItem(uris[i]['status']))
			self.tblUris.setRowHeight(i,25)
			
	def refreshView(self):
		'''
		This piece of code will be executed each 2 seconds to refresh the 
		data viewed in the main window
		'''
		self.viewActive()
		global_status = self.aria.getGlobalStatus()
		self.lwCategories.item(0).setText('Active Downloads ('+global_status['numActive']+')')
		self.lwCategories.item(1).setText('Waiting Downloads ('+global_status['numWaiting']+')')
		self.lwCategories.item(2).setText('Stopped Downloads ('+global_status['numStopped']+')')
		
	def showMenuRC(self):  
		'''
		Show menu when right-click a download
		'''
		self.menuRC.exec_(QtGui.QCursor.pos()) 