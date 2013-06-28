# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glue/qt/ui/glue_application.ui'
#
# Created: Fri Jun 28 10:12:40 2013
#      by: pyside-uic 0.2.13 running on glue.external.qt 1.1.0
#
# WARNING! All changes made in this file will be lost!

from glue.external.qt import QtCore, QtGui

class Ui_GlueApplication(object):
    def setupUi(self, GlueApplication):
        GlueApplication.setObjectName("GlueApplication")
        GlueApplication.resize(1116, 749)
        self.centralwidget = QtGui.QWidget(GlueApplication)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_splitter = QtGui.QSplitter(self.centralwidget)
        self.main_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.main_splitter.setObjectName("main_splitter")
        self.data_plot_splitter = QtGui.QSplitter(self.main_splitter)
        self.data_plot_splitter.setOrientation(QtCore.Qt.Vertical)
        self.data_plot_splitter.setObjectName("data_plot_splitter")
        self.data_layers = QtGui.QGroupBox(self.data_plot_splitter)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.data_layers.setFont(font)
        self.data_layers.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.data_layers.setFlat(False)
        self.data_layers.setObjectName("data_layers")
        self.plot_splitter = QtGui.QSplitter(self.data_plot_splitter)
        self.plot_splitter.setOrientation(QtCore.Qt.Vertical)
        self.plot_splitter.setObjectName("plot_splitter")
        self.plot_layers = QtGui.QGroupBox(self.plot_splitter)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.plot_layers.setFont(font)
        self.plot_layers.setFlat(False)
        self.plot_layers.setObjectName("plot_layers")
        self.plot_options = QtGui.QGroupBox(self.plot_splitter)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.plot_options.setFont(font)
        self.plot_options.setFlat(False)
        self.plot_options.setCheckable(False)
        self.plot_options.setObjectName("plot_options")
        self.tabWidget = QtGui.QTabWidget(self.main_splitter)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(400, 0))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout.addWidget(self.main_splitter)
        GlueApplication.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(GlueApplication)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        GlueApplication.setStatusBar(self.statusbar)
        self.actionSave_session = QtGui.QAction(GlueApplication)
        self.actionSave_session.setObjectName("actionSave_session")
        self.actionNew_Session = QtGui.QAction(GlueApplication)
        self.actionNew_Session.setObjectName("actionNew_Session")
        self.actionQuit = QtGui.QAction(GlueApplication)
        self.actionQuit.setObjectName("actionQuit")
        self.actionLoad_data = QtGui.QAction(GlueApplication)
        self.actionLoad_data.setObjectName("actionLoad_data")
        self.actionNew_Subset = QtGui.QAction(GlueApplication)
        self.actionNew_Subset.setObjectName("actionNew_Subset")
        self.actionTransfer_Subset = QtGui.QAction(GlueApplication)
        self.actionTransfer_Subset.setObjectName("actionTransfer_Subset")
        self.actionSave_Subset = QtGui.QAction(GlueApplication)
        self.actionSave_Subset.setObjectName("actionSave_Subset")
        self.actionNew_Tab = QtGui.QAction(GlueApplication)
        self.actionNew_Tab.setObjectName("actionNew_Tab")
        self.actionNew_Tab_2 = QtGui.QAction(GlueApplication)
        self.actionNew_Tab_2.setObjectName("actionNew_Tab_2")
        self.action1x1 = QtGui.QAction(GlueApplication)
        self.action1x1.setObjectName("action1x1")
        self.action2x2 = QtGui.QAction(GlueApplication)
        self.action2x2.setObjectName("action2x2")
        self.action2x2_2 = QtGui.QAction(GlueApplication)
        self.action2x2_2.setObjectName("action2x2_2")

        self.retranslateUi(GlueApplication)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(GlueApplication)

    def retranslateUi(self, GlueApplication):
        GlueApplication.setWindowTitle(QtGui.QApplication.translate("GlueApplication", "Glue", None, QtGui.QApplication.UnicodeUTF8))
        self.data_layers.setTitle(QtGui.QApplication.translate("GlueApplication", "Data Collection", None, QtGui.QApplication.UnicodeUTF8))
        self.plot_layers.setTitle(QtGui.QApplication.translate("GlueApplication", "Plot Layers", None, QtGui.QApplication.UnicodeUTF8))
        self.plot_options.setTitle(QtGui.QApplication.translate("GlueApplication", "Plot Options", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_session.setText(QtGui.QApplication.translate("GlueApplication", "Save session", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Session.setText(QtGui.QApplication.translate("GlueApplication", "New session", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("GlueApplication", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_data.setText(QtGui.QApplication.translate("GlueApplication", "Load data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Subset.setText(QtGui.QApplication.translate("GlueApplication", "New Subset", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTransfer_Subset.setText(QtGui.QApplication.translate("GlueApplication", "Transer Subset", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Subset.setText(QtGui.QApplication.translate("GlueApplication", "Save Subset", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Tab.setText(QtGui.QApplication.translate("GlueApplication", "New Tab", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Tab_2.setText(QtGui.QApplication.translate("GlueApplication", "New Tab", None, QtGui.QApplication.UnicodeUTF8))
        self.action1x1.setText(QtGui.QApplication.translate("GlueApplication", "1x1", None, QtGui.QApplication.UnicodeUTF8))
        self.action2x2.setText(QtGui.QApplication.translate("GlueApplication", "2x2", None, QtGui.QApplication.UnicodeUTF8))
        self.action2x2_2.setText(QtGui.QApplication.translate("GlueApplication", "3x3", None, QtGui.QApplication.UnicodeUTF8))

