# -*- coding: utf-8 -*-#
# <A PySide Gui for Aria2 Download Manager>
# Copyright (C) 2013  a.atalla <email>
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
from Aria2Manager import Aria2Manager
from PySide import QtGui,QtCore
from PySide.QtCore import Slot
from gui.Ui_InfoDialog import Ui_InfoDialog

class InfoDialog(QtGui.QDialog,Ui_InfoDialog):
    def __init__(self,gid):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.gid = gid
        self.aria = Aria2Manager()

        self.tblInformation.setColumnWidth(0, 200)
        self.tblInformation.setColumnWidth(1, 200)

        options = self.aria.getOptions(gid)
        self.lblFileName.setText(options['out'])
        self.tblInformation.setRowCount(1)
        for option in options:
            print option, ' : ', options[option]
            self.tblInformation.setItem(self.tblInformation.rowCount() - 1, 0, QtGui.QTableWidgetItem(option))
            self.tblInformation.setItem(self.tblInformation.rowCount() - 1, 1, QtGui.QTableWidgetItem(options[option]))
            self.tblInformation.setRowCount(self.tblInformation.rowCount()+1)