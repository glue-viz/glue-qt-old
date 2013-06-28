# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glue/qt/ui/subset_facet.ui'
#
# Created: Fri Jun 28 10:12:42 2013
#      by: pyside-uic 0.2.13 running on glue.external.qt 1.1.0
#
# WARNING! All changes made in this file will be lost!

from glue.external.qt import QtCore, QtGui

class Ui_SubsetFacet(object):
    def setupUi(self, SubsetFacet):
        SubsetFacet.setObjectName("SubsetFacet")
        SubsetFacet.resize(366, 405)
        self.verticalLayout = QtGui.QVBoxLayout(SubsetFacet)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.component_selector = ComponentSelector(SubsetFacet)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.component_selector.sizePolicy().hasHeightForWidth())
        self.component_selector.setSizePolicy(sizePolicy)
        self.component_selector.setObjectName("component_selector")
        self.verticalLayout.addWidget(self.component_selector)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtGui.QLabel(SubsetFacet)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.num = QtGui.QSpinBox(SubsetFacet)
        self.num.setMaximum(20)
        self.num.setProperty("value", 5)
        self.num.setObjectName("num")
        self.horizontalLayout_5.addWidget(self.num)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtGui.QLabel(SubsetFacet)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.min = QtGui.QLineEdit(SubsetFacet)
        self.min.setObjectName("min")
        self.horizontalLayout_3.addWidget(self.min)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtGui.QLabel(SubsetFacet)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.max = QtGui.QLineEdit(SubsetFacet)
        self.max.setObjectName("max")
        self.horizontalLayout_2.addWidget(self.max)
        self.log = QtGui.QCheckBox(SubsetFacet)
        self.log.setObjectName("log")
        self.horizontalLayout_2.addWidget(self.log)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(SubsetFacet)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.color_scale = QtGui.QComboBox(SubsetFacet)
        self.color_scale.setObjectName("color_scale")
        self.horizontalLayout.addWidget(self.color_scale)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(SubsetFacet)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout.setStretch(0, 5)

        self.retranslateUi(SubsetFacet)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SubsetFacet.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), SubsetFacet.reject)
        QtCore.QMetaObject.connectSlotsByName(SubsetFacet)

    def retranslateUi(self, SubsetFacet):
        SubsetFacet.setWindowTitle(QtGui.QApplication.translate("SubsetFacet", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SubsetFacet", "Number of Subsets", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SubsetFacet", "Min", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("SubsetFacet", "Max", None, QtGui.QApplication.UnicodeUTF8))
        self.log.setText(QtGui.QApplication.translate("SubsetFacet", "Log spacing", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SubsetFacet", "Color Scale", None, QtGui.QApplication.UnicodeUTF8))

from ..component_selector import ComponentSelector
