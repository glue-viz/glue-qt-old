# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glue/qt/ui/subsetlinkerdialog.ui'
#
# Created: Wed Jul 31 15:07:26 2013
#      by: pyside-uic 0.2.13 running on glue.external.qt 1.1.0
#
# WARNING! All changes made in this file will be lost!

from glue.external.qt import QtCore, QtGui

class Ui_SubsetLinkerDialog(object):
    def setupUi(self, SubsetLinkerDialog):
        SubsetLinkerDialog.setObjectName("SubsetLinkerDialog")
        SubsetLinkerDialog.setWindowModality(QtCore.Qt.WindowModal)
        SubsetLinkerDialog.resize(319, 339)
        SubsetLinkerDialog.setModal(True)
        self.verticalLayout_2 = QtGui.QVBoxLayout(SubsetLinkerDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(SubsetLinkerDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.layerTree = QtGui.QTreeWidget(SubsetLinkerDialog)
        self.layerTree.setObjectName("layerTree")
        self.verticalLayout.addWidget(self.layerTree)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelButton = QtGui.QPushButton(SubsetLinkerDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.okButton = QtGui.QPushButton(SubsetLinkerDialog)
        self.okButton.setEnabled(False)
        self.okButton.setDefault(False)
        self.okButton.setFlat(False)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(SubsetLinkerDialog)
        QtCore.QMetaObject.connectSlotsByName(SubsetLinkerDialog)
        SubsetLinkerDialog.setTabOrder(self.layerTree, self.cancelButton)
        SubsetLinkerDialog.setTabOrder(self.cancelButton, self.okButton)

    def retranslateUi(self, SubsetLinkerDialog):
        SubsetLinkerDialog.setWindowTitle(QtGui.QApplication.translate("SubsetLinkerDialog", "Subset Linker", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SubsetLinkerDialog", "Select two or more subsets to link", None, QtGui.QApplication.UnicodeUTF8))
        self.layerTree.headerItem().setText(0, QtGui.QApplication.translate("SubsetLinkerDialog", "Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("SubsetLinkerDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("SubsetLinkerDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))

