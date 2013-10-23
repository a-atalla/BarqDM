# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/MainWindow.ui'
#
# Created: Wed Oct 23 05:25:19 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(818, 489)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons/barq.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.lwCategories = QtGui.QListWidget(self.splitter_2)
        self.lwCategories.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lwCategories.setAlternatingRowColors(False)
        self.lwCategories.setIconSize(QtCore.QSize(24, 24))
        self.lwCategories.setObjectName("lwCategories")
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tblActive = QtGui.QTableWidget(self.splitter)
        self.tblActive.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblActive.sizePolicy().hasHeightForWidth())
        self.tblActive.setSizePolicy(sizePolicy)
        self.tblActive.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tblActive.setProperty("showDropIndicator", False)
        self.tblActive.setDragDropOverwriteMode(False)
        self.tblActive.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblActive.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tblActive.setShowGrid(False)
        self.tblActive.setGridStyle(QtCore.Qt.NoPen)
        self.tblActive.setColumnCount(7)
        self.tblActive.setObjectName("tblActive")
        self.tblActive.setColumnCount(7)
        self.tblActive.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblActive.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblActive.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tblActive.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tblActive.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tblActive.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tblActive.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tblActive.setHorizontalHeaderItem(6, item)
        self.tblActive.horizontalHeader().setVisible(True)
        self.tblActive.horizontalHeader().setCascadingSectionResizes(True)
        self.tblActive.horizontalHeader().setDefaultSectionSize(100)
        self.tblActive.verticalHeader().setVisible(False)
        self.frame = QtGui.QFrame(self.splitter)
        self.frame.setMinimumSize(QtCore.QSize(0, 150))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtGui.QTabWidget(self.frame)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtGui.QTableWidget(self.tab)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.splitter_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cboxGlobalSpeed = QtGui.QComboBox(self.centralwidget)
        self.cboxGlobalSpeed.setObjectName("cboxGlobalSpeed")
        self.cboxGlobalSpeed.addItem("")
        self.cboxGlobalSpeed.addItem("")
        self.cboxGlobalSpeed.addItem("")
        self.cboxGlobalSpeed.addItem("")
        self.cboxGlobalSpeed.addItem("")
        self.cboxGlobalSpeed.addItem("")
        self.cboxGlobalSpeed.addItem("")
        self.cboxGlobalSpeed.addItem("")
        self.cboxGlobalSpeed.addItem("")
        self.cboxGlobalSpeed.addItem("")
        self.cboxGlobalSpeed.addItem("")
        self.cboxGlobalSpeed.addItem("")
        self.cboxGlobalSpeed.addItem("")
        self.cboxGlobalSpeed.addItem("")
        self.cboxGlobalSpeed.addItem("")
        self.horizontalLayout.addWidget(self.cboxGlobalSpeed)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuDownload = QtGui.QMenu(self.menubar)
        self.menuDownload.setObjectName("menuDownload")
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(16, 16))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNewDownload = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/icons/project-development-new-template.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewDownload.setIcon(icon1)
        self.actionNewDownload.setObjectName("actionNewDownload")
        self.actionRemoveDownload = QtGui.QAction(MainWindow)
        self.actionRemoveDownload.setEnabled(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/icons/list-remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemoveDownload.setIcon(icon2)
        self.actionRemoveDownload.setObjectName("actionRemoveDownload")
        self.actionStart = QtGui.QAction(MainWindow)
        self.actionStart.setEnabled(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/icons/media-playback-start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStart.setIcon(icon3)
        self.actionStart.setObjectName("actionStart")
        self.actionStartAll = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/icons/media-seek-forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStartAll.setIcon(icon4)
        self.actionStartAll.setObjectName("actionStartAll")
        self.actionPause = QtGui.QAction(MainWindow)
        self.actionPause.setEnabled(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/icons/media-playback-pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPause.setIcon(icon5)
        self.actionPause.setObjectName("actionPause")
        self.actionPauseAll = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/icons/media-record.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPauseAll.setIcon(icon6)
        self.actionPauseAll.setObjectName("actionPauseAll")
        self.actionQuit = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/icons/application-exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon7)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPreference = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/icons/preferences-system.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreference.setIcon(icon8)
        self.actionPreference.setObjectName("actionPreference")
        self.actionAbout_aria2 = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/images/icons/barq.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout_aria2.setIcon(icon9)
        self.actionAbout_aria2.setObjectName("actionAbout_aria2")
        self.actionAbout_Qt = QtGui.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionDownloadLimit = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/icons/go-down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDownloadLimit.setIcon(icon10)
        self.actionDownloadLimit.setObjectName("actionDownloadLimit")
        self.actionCleanList = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/icons/edit-clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCleanList.setIcon(icon11)
        self.actionCleanList.setObjectName("actionCleanList")
        self.menuFile.addAction(self.actionNewDownload)
        self.menuFile.addAction(self.actionRemoveDownload)
        self.menuFile.addAction(self.actionQuit)
        self.menuDownload.addAction(self.actionStart)
        self.menuDownload.addAction(self.actionStartAll)
        self.menuDownload.addAction(self.actionPause)
        self.menuDownload.addAction(self.actionPauseAll)
        self.menuDownload.addSeparator()
        self.menuDownload.addAction(self.actionCleanList)
        self.menuSettings.addAction(self.actionPreference)
        self.menu_Help.addAction(self.actionAbout_aria2)
        self.menu_Help.addAction(self.actionAbout_Qt)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDownload.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.actionNewDownload)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionStart)
        self.toolBar.addAction(self.actionPause)
        self.toolBar.addAction(self.actionStartAll)
        self.toolBar.addAction(self.actionPauseAll)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCleanList)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPreference)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.cboxGlobalSpeed.setCurrentIndex(14)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Barq Download Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.tblActive.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "gid", None, QtGui.QApplication.UnicodeUTF8))
        self.tblActive.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "File Name", None, QtGui.QApplication.UnicodeUTF8))
        self.tblActive.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.tblActive.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Total Size", None, QtGui.QApplication.UnicodeUTF8))
        self.tblActive.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "Progress", None, QtGui.QApplication.UnicodeUTF8))
        self.tblActive.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("MainWindow", "Speed", None, QtGui.QApplication.UnicodeUTF8))
        self.tblActive.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("MainWindow", "Time Left", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Global Download Limit", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxGlobalSpeed.setItemText(0, QtGui.QApplication.translate("MainWindow", "5          Kb/Sec", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxGlobalSpeed.setItemText(1, QtGui.QApplication.translate("MainWindow", "10        Kb/Sec", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxGlobalSpeed.setItemText(2, QtGui.QApplication.translate("MainWindow", "15        Kb/Sec", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxGlobalSpeed.setItemText(3, QtGui.QApplication.translate("MainWindow", "20        Kb/Sec", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxGlobalSpeed.setItemText(4, QtGui.QApplication.translate("MainWindow", "30        Kb/Sec", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxGlobalSpeed.setItemText(5, QtGui.QApplication.translate("MainWindow", "40        Kb/Sec", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxGlobalSpeed.setItemText(6, QtGui.QApplication.translate("MainWindow", "50        Kb/Sec", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxGlobalSpeed.setItemText(7, QtGui.QApplication.translate("MainWindow", "60        Kb/Sec", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxGlobalSpeed.setItemText(8, QtGui.QApplication.translate("MainWindow", "70        Kb/Sec", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxGlobalSpeed.setItemText(9, QtGui.QApplication.translate("MainWindow", "80        Kb/Sec", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxGlobalSpeed.setItemText(10, QtGui.QApplication.translate("MainWindow", "90        Kb/Sec", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxGlobalSpeed.setItemText(11, QtGui.QApplication.translate("MainWindow", "100      Kb/Sec", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxGlobalSpeed.setItemText(12, QtGui.QApplication.translate("MainWindow", "150      Kb/Sec", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxGlobalSpeed.setItemText(13, QtGui.QApplication.translate("MainWindow", "200      Kb/Sec", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxGlobalSpeed.setItemText(14, QtGui.QApplication.translate("MainWindow", "Unlimited", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDownload.setTitle(QtGui.QApplication.translate("MainWindow", "Download", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QtGui.QApplication.translate("MainWindow", "&Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewDownload.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewDownload.setToolTip(QtGui.QApplication.translate("MainWindow", "Add New Download", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveDownload.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart.setToolTip(QtGui.QApplication.translate("MainWindow", "Start Selected Downlad", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStartAll.setText(QtGui.QApplication.translate("MainWindow", "Start All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStartAll.setToolTip(QtGui.QApplication.translate("MainWindow", "Start All Downloads", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPause.setText(QtGui.QApplication.translate("MainWindow", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPause.setToolTip(QtGui.QApplication.translate("MainWindow", "Pause Selected Download", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPauseAll.setText(QtGui.QApplication.translate("MainWindow", "Pause All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPauseAll.setToolTip(QtGui.QApplication.translate("MainWindow", "Pause All Downloads", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setToolTip(QtGui.QApplication.translate("MainWindow", "Quit The Programe", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreference.setText(QtGui.QApplication.translate("MainWindow", "Preference", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_aria2.setText(QtGui.QApplication.translate("MainWindow", "About aria2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Qt.setText(QtGui.QApplication.translate("MainWindow", "About Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDownloadLimit.setText(QtGui.QApplication.translate("MainWindow", "Download Limit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCleanList.setText(QtGui.QApplication.translate("MainWindow", "Clean List", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCleanList.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>remove all downloads with status (complete , error , removed)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import images_rc
