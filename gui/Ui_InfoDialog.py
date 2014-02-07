# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/InfoDialog.ui'
#
# Created: Fri Feb  7 11:50:50 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_InfoDialog(object):
    def setupUi(self, InfoDialog):
        InfoDialog.setObjectName("InfoDialog")
        InfoDialog.resize(479, 420)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons/help-about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        InfoDialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(InfoDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblFileName = QtGui.QLabel(InfoDialog)
        self.lblFileName.setObjectName("lblFileName")
        self.verticalLayout.addWidget(self.lblFileName)
        self.tblInformation = QtGui.QTableWidget(InfoDialog)
        self.tblInformation.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.tblInformation.setGridStyle(QtCore.Qt.SolidLine)
        self.tblInformation.setObjectName("tblInformation")
        self.tblInformation.setColumnCount(2)
        self.tblInformation.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblInformation.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblInformation.setHorizontalHeaderItem(1, item)
        self.tblInformation.horizontalHeader().setVisible(True)
        self.tblInformation.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tblInformation)

        self.retranslateUi(InfoDialog)
        QtCore.QMetaObject.connectSlotsByName(InfoDialog)

    def retranslateUi(self, InfoDialog):
        InfoDialog.setWindowTitle(QtGui.QApplication.translate("InfoDialog", "Download Information", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFileName.setText(QtGui.QApplication.translate("InfoDialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">File Name </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tblInformation.setSortingEnabled(True)
        self.tblInformation.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("InfoDialog", "Option", None, QtGui.QApplication.UnicodeUTF8))
        self.tblInformation.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("InfoDialog", "Value", None, QtGui.QApplication.UnicodeUTF8))

import images_rc
