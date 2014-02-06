# -*- coding: utf-8 -*-
#
# <A PySide Gui for Aria2 Download Manager>
# Copyright (C) 2013  a.atalla <a.atalla[at]hacari[dot] org
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation,  either version 3 of the License,  or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not,  see <http://www.gnu.org/licenses/>.
# 
#TODO: Notify on (Complete,Error).  Target V-0.5
#TODO:Show all download options. Target V-0.5
#TODO:Start with system startup. Target V-0.5
#TODO: Change Download Options. Target V-0.6
#

from PySide.QtCore import Slot
from PySide import QtGui, QtCore
from gui.Ui_MainWindow import Ui_MainWindow
from NewDownload import NewDownload
from LimitDialog import LimitDialog
from Aria2Manager import Aria2Manager
#import pprint as p
import subprocess
import os


class MainWindow(QtGui.QMainWindow,  Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.showMaximized()
        self._isQuit = False
        self.aria = Aria2Manager()
        self.aria.startAria2()
        if self.aria.isRunning():
            self.fillCategories()
            self.timer = QtCore.QTimer(self)
            self.timer.start(2000)
            self.connect(self.timer, QtCore.SIGNAL("timeout()"),  self.refreshView)
        else:
            self.setWindowTitle('Barq Download Manager (Offline)')

        self.trayIcon()

        ##Setting the columns sizes
        self.tblActive.setColumnWidth(0, 140)
        self.tblActive.setColumnWidth(1, 400)
        self.tblActive.setColumnWidth(2, 75)
        self.tblActive.setColumnWidth(3, 100)
        self.tblActive.setColumnWidth(4, 175)
        self.tblActive.setColumnWidth(5, 100)

        self.tblUris.setColumnWidth(0, 800)
        self.tblUris.setColumnWidth(1, 150)

        ## The Right-click menu
        self.menuRC = QtGui.QMenu()
        self.menuRC.addAction(self.actionOpenFile)
        self.menuRC.addAction(self.actionOpenFolder)
        self.menuRC.addSeparator()
        self.menuRC.addAction(self.actionPause)
        self.menuRC.addAction(self.actionStart)
        self.menuRC.addAction(self.actionRemoveDownload)
        self.menuRC.addAction(self.actionResumeError)
        self.menuRC.addSeparator()
        self.menuRC.addAction(self.actionDownloadLimit)
        self.tblActive.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.connect(self.tblActive,  QtCore.SIGNAL('customContextMenuRequested(const QPoint&)'),  self.showMenuRC)

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
        if speed == 'Unlimited':
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
        if ret == QtGui.QMessageBox.Yes:
            self.aria.removeSingleDownload(self.selectedGid())
            self.tblActive.removeRow(self.tblActive.selectionModel().currentIndex().row())

    @Slot()
    def on_actionCleanList_triggered(self):
        self.aria.cleanDownloadList()

    @Slot()
    def on_actionOpenFolder_triggered(self):
        folder =  self.aria.getDownloadDetail(self.selectedGid(), 'dir')
        subprocess.call(['xdg-open', folder])

    @Slot()
    def on_actionOpenFile_triggered(self):
        dir =  self.aria.getDownloadDetail(self.selectedGid(), 'dir')
        selectedRow =  self.tblActive.selectionModel().currentIndex().row()
        if not selectedRow == -1:
            filename =  self.tblActive.item(selectedRow, 1).text()
        else:
            filename=''
        print dir+'/'+filename
        subprocess.call(['xdg-open', dir+'/'+filename])

    @Slot()
    def on_actionResumeError_triggered(self):
        uri= self.aria.getDownloadDetail(self.selectedGid(), 'files')[0].get('uris')[0].get('uri')
        dir =  self.aria.getDownloadDetail(self.selectedGid(), 'dir')
        params = {'dir':dir}
        self.aria.addUris([uri], params)


    @Slot()
    def on_tblActive_itemSelectionChanged(self):
        self.tblUris.clearContents()
        self.tblUris.setRowCount(0)
        self.urisTimer = QtCore.QTimer(self)
        self.urisTimer.start(2000)
        self.connect(self.urisTimer, QtCore.SIGNAL("timeout()"),  self.viewUris)

    @Slot()
    def on_actionAboutQt_triggered(self):
        QtGui.QApplication.aboutQt()
    @Slot()
    def on_actionQuit_triggered(self):
        self._isQuit = True
        self.closeEvent(QtGui.QCloseEvent)

    def closeEvent(self, event):
        if not self._isQuit:
            event.ignore()
            if self.isVisible():
                self.hide()
                self.trayicon.showMessage(self.tr('Barq Download Manager is still running'), self.tr(''))
        else:
            self.aria.stopAria2()
            self.close()

    def trayIcon(self):
        self.trayicon=QtGui.QSystemTrayIcon(QtGui.QIcon(':images/icons/barq-tray-icon.png'))
        self.trayicon.show()
        self.menu=QtGui.QMenu()
        self.menu.addAction(self.actionPauseAll)
        self.menu.addAction(self.actionStartAll)
        self.menu.addAction(self.actionQuit)
        self.trayicon.setContextMenu(self.menu)
        self.trayicon.activated.connect(self.onTrayIconActivated)

    def onTrayIconActivated(self,  reason):
        if reason  ==  QtGui.QSystemTrayIcon.DoubleClick:
            if self.isVisible():
                self.hide()
            else:
                self.show()

    def fillCategories(self):
        try:
            global_status = self.aria.getGlobalStatus()
            self.lwCategories.clear()
            item = QtGui.QListWidgetItem('Active Downloads ('+global_status['numActive']+')', self.lwCategories)
            item.setIcon(QtGui.QIcon(':images/icons/media-playback-start.png'))
            item = QtGui.QListWidgetItem('Waiting Downloads ('+global_status['numWaiting']+')', self.lwCategories)
            item.setIcon(QtGui.QIcon(':images/icons/media-playback-pause.png'))
            item = QtGui.QListWidgetItem('Stopped Downloads ('+global_status['numStopped']+')', self.lwCategories)
            item.setIcon(QtGui.QIcon(':images/icons/media-playback-stop.png'))
        except:
            pass



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
            size= str(round(float(self.aria.getDownloadDetail(gid, 'totalLength'))/1000000, 2))+' MB'
            speed  = str(round(float(self.aria.getDownloadDetail(gid, 'downloadSpeed'))/1000, 2))+' Kb/sec'
            try:
                progress = round(float(self.aria.getDownloadDetail(gid, 'completedLength'))*100/float(self.aria.getDownloadDetail(gid, 'totalLength')), 2)
            except:
                progress =0

            try: # To avoid dividing by zero until connect to the server
                RemainingTime = (float(self.aria.getDownloadDetail(gid, 'totalLength'))-float(self.aria.getDownloadDetail(gid, 'completedLength')))/float(self.aria.getDownloadDetail(gid, 'downloadSpeed'))
                remainingTime = round (RemainingTime/(3600), 2) #Hour Format
                timeFormat = '  H'
                if remainingTime < 1 :
                    remainingTime = round (RemainingTime/(60), 2) #Min Format
                    timeFormat = '  M'
                    if remainingTime < 1 :
                        remainingTime = round (RemainingTime, 2) #Sec Format
                        timeFormat = '  S'
            except:
                remainingTime = ''
                timeFormat=''

            if self.tblActive.rowCount() < len(allList):
                self.tblActive.setRowCount(self.tblActive.rowCount()+1)


            pbar = QtGui.QProgressBar()
            pbar.setRange(0, 100) # The range is from 0  to Size
            pbar.setValue(progress)			#The value is the dsize which is completedLength
            files = self.aria.getDownloadDetail(gid, 'files')
            self.tblActive.setItem(i, 0, QtGui.QTableWidgetItem(gid))
            self.tblActive.setItem(i, 1, QtGui.QTableWidgetItem(os.path.split(files[0].get('path'))[1]))
            self.tblActive.setItem(i, 2, QtGui.QTableWidgetItem(self.aria.getDownloadDetail(gid, 'status')))
            self.tblActive.setItem(i, 3, QtGui.QTableWidgetItem(size))
            self.tblActive.setCellWidget(i, 4, pbar)
            self.tblActive.setItem(i, 5, QtGui.QTableWidgetItem(speed))
            self.tblActive.setItem(i, 6, QtGui.QTableWidgetItem(str(remainingTime)+timeFormat))
            self.tblActive.setRowHeight(i, 20)

            s=self.aria.getDownloadDetail(gid, 'status')
            for j in range(0, 7):
                if not j == 4:
                    if j == 2 or j == 3 or j == 5 or j == 6:
                        self.tblActive.item(i, j).setTextAlignment(QtCore.Qt.AlignCenter)

                    if s == 'error' or s == 'removed' :
                        self.tblActive.item(i, j).setBackground(QtCore.Qt.red)
                    elif s == 'complete':
                        self.tblActive.item(i, j).setBackground(QtCore.Qt.green)

    def selectedGid(self):
        selectedRow =  self.tblActive.selectionModel().currentIndex().row()
        if not selectedRow == -1:
            gid =str(self.tblActive.item(selectedRow, 0).text())
            return gid

    def viewUris(self):
        self.btmTab.setTabText(0, self.tblActive.item(self.tblActive.currentRow(), 1).text())

        uris = self.aria.getUrisDetails(self.selectedGid())
        if self.tblUris.rowCount()<len(uris):
            self.tblUris.setRowCount(len(uris))
            self.tblUris.clearContents()
        i=0
        for i in range(0, len(uris)):
            self.tblUris.setItem(i, 0, QtGui.QTableWidgetItem(uris[i]['uri']))
            self.tblUris.setItem(i, 1, QtGui.QTableWidgetItem(uris[i]['status']))
            self.tblUris.setRowHeight(i, 25)

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
        selectedRow = self.tblActive.selectionModel().currentIndex().row()
        if not selectedRow == -1:
            if self.tblActive.item(selectedRow, 2).text() == 'error':
                self.actionResumeError.setEnabled(True)

        self.menuRC.exec_(QtGui.QCursor.pos())