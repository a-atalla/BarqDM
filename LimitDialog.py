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
from gui.Ui_LimitDialog import Ui_LimitDialog

class LimitDialog(QtGui.QDialog,Ui_LimitDialog):
    def __init__(self,gid):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.gid = gid
        self.aria = Aria2Manager()

        self.slidLimit.setValue( int(self.aria.getOptions(self.gid).get('max-download-limit'))/1000)

    @Slot()
    def on_btnCancel_clicked(self):
        self.close()
    @Slot()
    def on_btnOk_clicked(self):
        speed = str(self.spinLimit.value())+'K'
        self.aria.changeOption(self.gid,{'max-download-limit':speed})
        self.close()

    @Slot()
    def on_slidLimit_valueChanged(self):
        self.spinLimit.setValue(self.slidLimit.value())

    @Slot()
    def on_spinLimit_valueChanged(self):
        self.slidLimit.setValue(self.spinLimit.value())
