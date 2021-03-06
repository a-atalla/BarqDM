# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/NewDownloadDialog.ui'
#
# Created: Fri Feb  7 11:50:50 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_NewDownloadDialog(object):
    def setupUi(self, NewDownloadDialog):
        NewDownloadDialog.setObjectName("NewDownloadDialog")
        NewDownloadDialog.resize(421, 419)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons/project-development-new-template.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NewDownloadDialog.setWindowIcon(icon)
        self.verticalLayout_7 = QtGui.QVBoxLayout(NewDownloadDialog)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.splitter = QtGui.QSplitter(NewDownloadDialog)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtGui.QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.edtUrl = QtGui.QLineEdit(self.groupBox)
        self.edtUrl.setObjectName("edtUrl")
        self.verticalLayout.addWidget(self.edtUrl)
        self.listUrls = QtGui.QListWidget(self.groupBox)
        self.listUrls.setObjectName("listUrls")
        self.verticalLayout.addWidget(self.listUrls)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnAdd = QtGui.QToolButton(self.groupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/icons/list-add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAdd.setIcon(icon1)
        self.btnAdd.setObjectName("btnAdd")
        self.verticalLayout_2.addWidget(self.btnAdd)
        self.btnRemove = QtGui.QToolButton(self.groupBox)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/icons/list-remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRemove.setIcon(icon2)
        self.btnRemove.setObjectName("btnRemove")
        self.verticalLayout_2.addWidget(self.btnRemove)
        self.btnLoadFile = QtGui.QToolButton(self.groupBox)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/icons/document-edit-sign.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLoadFile.setIcon(icon3)
        self.btnLoadFile.setObjectName("btnLoadFile")
        self.verticalLayout_2.addWidget(self.btnLoadFile)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.groupBox_2 = QtGui.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.edtFileName = QtGui.QLineEdit(self.groupBox_2)
        self.edtFileName.setObjectName("edtFileName")
        self.verticalLayout_3.addWidget(self.edtFileName)
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.edtDir = QtGui.QLineEdit(self.groupBox_2)
        self.edtDir.setObjectName("edtDir")
        self.horizontalLayout_2.addWidget(self.edtDir)
        self.btnDir = QtGui.QToolButton(self.groupBox_2)
        self.btnDir.setObjectName("btnDir")
        self.horizontalLayout_2.addWidget(self.btnDir)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.spinSpeed = QtGui.QSpinBox(self.groupBox_2)
        self.spinSpeed.setMaximum(9999)
        self.spinSpeed.setProperty("value", 999)
        self.spinSpeed.setObjectName("spinSpeed")
        self.horizontalLayout.addWidget(self.spinSpeed)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.spinPieces = QtGui.QSpinBox(self.groupBox_2)
        self.spinPieces.setProperty("value", 1)
        self.spinPieces.setObjectName("spinPieces")
        self.horizontalLayout_3.addWidget(self.spinPieces)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.spinConnectionsPerServer = QtGui.QSpinBox(self.groupBox_2)
        self.spinConnectionsPerServer.setProperty("value", 1)
        self.spinConnectionsPerServer.setObjectName("spinConnectionsPerServer")
        self.horizontalLayout_4.addWidget(self.spinConnectionsPerServer)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.btnOk = QtGui.QPushButton(self.groupBox_2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/icons/dialog-ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOk.setIcon(icon4)
        self.btnOk.setObjectName("btnOk")
        self.horizontalLayout_6.addWidget(self.btnOk)
        self.btnCancel = QtGui.QPushButton(self.groupBox_2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/icons/dialog-cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancel.setIcon(icon5)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout_6.addWidget(self.btnCancel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_7.addWidget(self.splitter)

        self.retranslateUi(NewDownloadDialog)
        QtCore.QMetaObject.connectSlotsByName(NewDownloadDialog)

    def retranslateUi(self, NewDownloadDialog):
        NewDownloadDialog.setWindowTitle(QtGui.QApplication.translate("NewDownloadDialog", "Add URL", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("NewDownloadDialog", "Add Uris", None, QtGui.QApplication.UnicodeUTF8))
        self.listUrls.setToolTip(QtGui.QApplication.translate("NewDownloadDialog", "<html><head/><body><p>All URLs should point to the same file</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd.setToolTip(QtGui.QApplication.translate("NewDownloadDialog", "Add url to the list", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd.setText(QtGui.QApplication.translate("NewDownloadDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRemove.setToolTip(QtGui.QApplication.translate("NewDownloadDialog", "Remove url from the list", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRemove.setText(QtGui.QApplication.translate("NewDownloadDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLoadFile.setToolTip(QtGui.QApplication.translate("NewDownloadDialog", "Load URLs from text file", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLoadFile.setText(QtGui.QApplication.translate("NewDownloadDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("NewDownloadDialog", "Download Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("NewDownloadDialog", "File Name (optional):", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NewDownloadDialog", "Download Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDir.setText(QtGui.QApplication.translate("NewDownloadDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("NewDownloadDialog", "Maximum Download Speed (kb/s)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("NewDownloadDialog", "Number of Pieces", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("NewDownloadDialog", "Max Connection Per server", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOk.setText(QtGui.QApplication.translate("NewDownloadDialog", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("NewDownloadDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

import images_rc
