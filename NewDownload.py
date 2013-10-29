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
from gui.Ui_NewDownloadDialog import Ui_NewDownloadDialog

from Aria2Manager import Aria2Manager

class NewDownload(QtGui.QDialog,Ui_NewDownloadDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		
		self.aria = Aria2Manager()
	@Slot()
	def on_btnDir_clicked(self):
		dialog = QtGui.QFileDialog(self)
		dirName = dialog.getExistingDirectory(self,"Select Download Directory")
		self.edtDir.setText(dirName)
        
	@Slot()
	def on_btnOk_clicked(self):
		speed= str(self.spinSpeed.value())+'K'
		connections = str(self.spinConnections.value())
		dir = str(self.edtDir.text())
		
		uris = []
		if self.edtUrl.text()=='':
		  for i in range(0,self.listUrls.count()):
			  uris.append(self.listUrls.item(i).text())
		params = {'dir':dir,'max-download-limit':speed,'split':connections}
		self.aria.addUris(uris,params)
		self.close()
			
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
