# -*- coding: utf-8 -*-
#
# <one line to give the program's name and a brief idea of what it does.>
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
from Aria2Manager import Aria2Manager

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.showMaximized()
		self.aria = Aria2Manager()
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
        
	@Slot()
	def on_actionQuit_triggered(self):
		self.close()
		
	@Slot()
	def on_actionNewDownload_triggered(self):
		newDlg = NewDownload()
		newDlg.exec_()
	
	@Slot()
	def on_actionStart_triggered(self):
		self.aria.unpauseSingleDownload(self.getGid())

	@Slot()
	def on_actionStartAll_triggered(self):
		self.aria.unpauseAllDownloads()

	@Slot()
	def on_actionPause_triggered(self):
		self.aria.pauseSingleDownload(self.getGid())
		
	@Slot()
	def on_actionPauseAll_triggered(self):
		self.aria.pauseAllDownloads()

	@Slot()
	def on_lwCategories_itemClicked(self):
		print self.lwCategories.currentItem().text()
        
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

	def getGid(self):
		selectedRow =  self.tblActive.selectionModel().currentIndex().row()
		gid =str(self.tblActive.item(selectedRow,0).text())
		return gid
		
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