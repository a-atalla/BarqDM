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

import os
import sys
from PySide.QtCore import Slot
from PySide import QtGui,QtCore
from gui.Ui_NewDownloadDialog import Ui_NewDownloadDialog

from Aria2Manager import Aria2Manager


HOME_DIR = os.environ['HOME']

class NewDownload(QtGui.QDialog,Ui_NewDownloadDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.aria = Aria2Manager()
		self.edtDir.setText(HOME_DIR+'/Downloads')
		
	@Slot()
	def on_btnDir_clicked(self):
		dialog = QtGui.QFileDialog(self)
		dirName = dialog.getExistingDirectory(self,"Select Download Directory")
		self.edtDir.setText(dirName)
        
	@Slot()
	def on_btnOk_clicked(self):
		speed= str(self.spinSpeed.value())+'K'
		pieces = str(self.spinPieces.value())
		maxconnectionperserver = str(self.spinConnectionsPerServer.value())
		dir = self.edtDir.text()
		oFileName = self.edtFileName.text()
		
		uris = []
		for i in range(0,self.listUrls.count()):
			url = self.listUrls.item(i).text()
			if url.startswith('http') or url.startswith('ftp'):
				uris.append(url)
			else:
				self.showMessage(url+'\n is not a valid url')
		print dir+'/'+oFileName
		params = {'dir':dir,\
				'max-download-limit':speed,\
				'max-concurrent-downloads':pieces,\
				'max-connection-per-server':maxconnectionperserver,\
				'out':oFileName}
		if not len(uris)==0:
			try:
				self.aria.addUris(uris,params)
				self.close()
			except:
				self.showMessage('Unexpected error:\n'+ str(sys.exc_info()[1]))
		else:
			self.showMessage('Please add at least one valid url to the list!')
			
	@Slot()
	def on_btnCancel_clicked(self):
		self.close()
		
	@Slot()
	def on_btnAdd_clicked(self):
		self.listUrls.addItem(self.edtUrl.text())
		self.edtUrl.setText('')
		
	@Slot()
	def on_btnRemove_clicked(self):
		self.listUrls.takeItem(self.listUrls.currentRow())
		
	@Slot()
	def on_btnLoadFile_clicked(self):
		dialog = QtGui.QFileDialog(self)
		fileName,_ = dialog.getOpenFileName(self,"Select a file",HOME_DIR)
		f = open(fileName,'r')
		for line in f.readlines():
			self.listUrls.addItem(line.strip())
			
	def showMessage(self,msg):
		msgBox = QtGui.QMessageBox()
		msgBox.setText(msg)
		msgBox.exec_()
		
