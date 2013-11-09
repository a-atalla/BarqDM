#!/usr/bin/env python
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
from sys import argv,exit
import  setproctitle
import psutil
from PySide.QtGui import QApplication,QMessageBox
#from PySide.QtCore import QString
from MainWindow import MainWindow
from NewDownload import NewDownload

def isRunning():
	proc_list = psutil.get_process_list()
	for proc in proc_list:
		if proc.name == 'barq':
			return True
	return False

app = QApplication(argv)

if isRunning():
	print 'Barq Download Manager is already running'
	if  len(argv) == 1:
		exit()
else:
	setproctitle.setproctitle('barq')
	win = MainWindow()
	win.show()
	
if len(argv) > 2:
	new = NewDownload()
	new.show()
	new.edtFileName.setText(argv[1].decode('utf-8'))
	new.listUrls.addItem(argv[2])

exit(app.exec_())
