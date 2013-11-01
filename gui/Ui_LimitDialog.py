# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/LimitDialog.ui'
#
# Created: Sat Nov  2 00:42:28 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_LimitDialog(object):
    def setupUi(self, LimitDialog):
        LimitDialog.setObjectName("LimitDialog")
        LimitDialog.resize(336, 85)
        self.verticalLayout = QtGui.QVBoxLayout(LimitDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.slidLimit = QtGui.QSlider(LimitDialog)
        self.slidLimit.setMaximum(999)
        self.slidLimit.setPageStep(5)
        self.slidLimit.setOrientation(QtCore.Qt.Horizontal)
        self.slidLimit.setObjectName("slidLimit")
        self.horizontalLayout_2.addWidget(self.slidLimit)
        self.spinLimit = QtGui.QSpinBox(LimitDialog)
        self.spinLimit.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.spinLimit.setMaximum(999)
        self.spinLimit.setObjectName("spinLimit")
        self.horizontalLayout_2.addWidget(self.spinLimit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnOk = QtGui.QPushButton(LimitDialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons/dialog-ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOk.setIcon(icon)
        self.btnOk.setObjectName("btnOk")
        self.horizontalLayout.addWidget(self.btnOk)
        self.btnCancel = QtGui.QPushButton(LimitDialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/icons/dialog-cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancel.setIcon(icon1)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(LimitDialog)
        QtCore.QMetaObject.connectSlotsByName(LimitDialog)

    def retranslateUi(self, LimitDialog):
        LimitDialog.setWindowTitle(QtGui.QApplication.translate("LimitDialog", "Download Limit", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOk.setText(QtGui.QApplication.translate("LimitDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("LimitDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

import images_rc
