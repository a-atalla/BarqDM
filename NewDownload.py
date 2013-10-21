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
from gui.Ui_NewDownloadDialog import Ui_NewDownloadDialog

from Aria2Manager import Aria2Manager

class NewDownload(QtGui.QDialog,Ui_NewDownloadDialog):
	def __init__(self,parent=None):
		QtGui.QDialog.__init__(self,parent)
		self.setupUi(self)
		
		self.aria = Aria2Manager()
		#self.edtUrl.setText('http://cdimage.ubuntu.com/kubuntu/releases/13.10/release/kubuntu-13.10-desktop-amd64.iso')
		#self.edtDir.setText('/media/Data/Iso')

	@Slot()
	def on_btnOk_clicked(self):
		speed= str(self.spinSpeed.value())+'K'
		connections = str(self.spinConnections.value())
		dir = str(self.edtDir.text())
		print type(speed),speed
		print type(connections),connections
		uris = [self.edtUrl.text()]
		params = {'dir':dir,'max-download-limit':speed,'max-connection-per-server':connections}
		self.aria.addUris(uris,params)
		self.close()
			
	@Slot()
	def on_btnCancel_clicked(self):
		self.close()
