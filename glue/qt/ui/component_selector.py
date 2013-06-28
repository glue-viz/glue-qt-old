# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glue/qt/ui/component_selector.ui'
#
# Created: Fri Jun 28 10:12:40 2013
#      by: pyside-uic 0.2.13 running on glue.external.qt 1.1.0
#
# WARNING! All changes made in this file will be lost!

from glue.external.qt import QtCore, QtGui

class Ui_ComponentSelector(object):
    def setupUi(self, ComponentSelector):
        ComponentSelector.setObjectName("ComponentSelector")
        ComponentSelector.resize(295, 452)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ComponentSelector)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(ComponentSelector)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.data_selector = QtGui.QComboBox(ComponentSelector)
        self.data_selector.setObjectName("data_selector")
        self.verticalLayout.addWidget(self.data_selector)
        self.label_2 = QtGui.QLabel(ComponentSelector)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.component_selector = GlueListWidget(ComponentSelector)
        self.component_selector.setObjectName("component_selector")
        self.verticalLayout.addWidget(self.component_selector)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ComponentSelector)
        QtCore.QMetaObject.connectSlotsByName(ComponentSelector)

    def retranslateUi(self, ComponentSelector):
        ComponentSelector.setWindowTitle(QtGui.QApplication.translate("ComponentSelector", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ComponentSelector", "Data Set", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ComponentSelector", "Component Identifiers", None, QtGui.QApplication.UnicodeUTF8))
        self.component_selector.setToolTip(QtGui.QApplication.translate("ComponentSelector", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Component IDs associated with this data set</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

from ..qtutil import GlueListWidget
