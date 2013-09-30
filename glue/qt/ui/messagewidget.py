# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glue/qt/ui/messagewidget.ui'
#
# Created: Wed Jul 31 15:07:26 2013
#      by: pyside-uic 0.2.13 running on glue.external.qt 1.1.0
#
# WARNING! All changes made in this file will be lost!

from glue.external.qt import QtCore, QtGui

class Ui_MessageWidget(object):
    def setupUi(self, MessageWidget):
        MessageWidget.setObjectName("MessageWidget")
        MessageWidget.resize(700, 400)
        self.horizontalLayout = QtGui.QHBoxLayout(MessageWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.messageTable = QtGui.QTableWidget(MessageWidget)
        self.messageTable.setObjectName("messageTable")
        self.messageTable.setColumnCount(0)
        self.messageTable.setRowCount(0)
        self.horizontalLayout.addWidget(self.messageTable)

        self.retranslateUi(MessageWidget)
        QtCore.QMetaObject.connectSlotsByName(MessageWidget)

    def retranslateUi(self, MessageWidget):
        MessageWidget.setWindowTitle(QtGui.QApplication.translate("MessageWidget", "Message Widget", None, QtGui.QApplication.UnicodeUTF8))

