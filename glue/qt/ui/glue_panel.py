# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glue/qt/ui/glue_panel.ui'
#
# Created: Fri Jun 28 10:12:40 2013
#      by: pyside-uic 0.2.13 running on glue.external.qt 1.1.0
#
# WARNING! All changes made in this file will be lost!

from glue.external.qt import QtCore, QtGui

class Ui_GluePanel(object):
    def setupUi(self, GluePanel):
        GluePanel.setObjectName("GluePanel")
        GluePanel.resize(731, 696)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GluePanel.sizePolicy().hasHeightForWidth())
        GluePanel.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtGui.QVBoxLayout(GluePanel)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.contentWrapper = QtGui.QVBoxLayout()
        self.contentWrapper.setObjectName("contentWrapper")
        self.vizContainer = QtGui.QWidget(GluePanel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vizContainer.sizePolicy().hasHeightForWidth())
        self.vizContainer.setSizePolicy(sizePolicy)
        self.vizContainer.setObjectName("vizContainer")
        self.contentWrapper.addWidget(self.vizContainer)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.unSplitButton = QtGui.QPushButton(GluePanel)
        self.unSplitButton.setObjectName("unSplitButton")
        self.horizontalLayout.addWidget(self.unSplitButton)
        self.verticalSplitButton = QtGui.QPushButton(GluePanel)
        self.verticalSplitButton.setCheckable(False)
        self.verticalSplitButton.setFlat(False)
        self.verticalSplitButton.setObjectName("verticalSplitButton")
        self.horizontalLayout.addWidget(self.verticalSplitButton)
        self.horizontalSplitButton = QtGui.QPushButton(GluePanel)
        self.horizontalSplitButton.setObjectName("horizontalSplitButton")
        self.horizontalLayout.addWidget(self.horizontalSplitButton)
        self.quadSplitButton = QtGui.QPushButton(GluePanel)
        self.quadSplitButton.setObjectName("quadSplitButton")
        self.horizontalLayout.addWidget(self.quadSplitButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.contentWrapper.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.contentWrapper)

        self.retranslateUi(GluePanel)
        QtCore.QMetaObject.connectSlotsByName(GluePanel)

    def retranslateUi(self, GluePanel):
        GluePanel.setWindowTitle(QtGui.QApplication.translate("GluePanel", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.unSplitButton.setToolTip(QtGui.QApplication.translate("GluePanel", "Close all other panels", None, QtGui.QApplication.UnicodeUTF8))
        self.unSplitButton.setText(QtGui.QApplication.translate("GluePanel", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalSplitButton.setToolTip(QtGui.QApplication.translate("GluePanel", "Split panel in half, side-by-side", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalSplitButton.setText(QtGui.QApplication.translate("GluePanel", "V", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalSplitButton.setToolTip(QtGui.QApplication.translate("GluePanel", "Split panel in half, top-and-bottom", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalSplitButton.setText(QtGui.QApplication.translate("GluePanel", "H", None, QtGui.QApplication.UnicodeUTF8))
        self.quadSplitButton.setToolTip(QtGui.QApplication.translate("GluePanel", "Split panel in four", None, QtGui.QApplication.UnicodeUTF8))
        self.quadSplitButton.setText(QtGui.QApplication.translate("GluePanel", "Q", None, QtGui.QApplication.UnicodeUTF8))

