# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glue/qt/ui/scatterwidget.ui'
#
# Created: Fri Jun 28 10:12:42 2013
#      by: pyside-uic 0.2.13 running on glue.external.qt 1.1.0
#
# WARNING! All changes made in this file will be lost!

from glue.external.qt import QtCore, QtGui

class Ui_ScatterWidget(object):
    def setupUi(self, ScatterWidget):
        ScatterWidget.setObjectName("ScatterWidget")
        ScatterWidget.resize(300, 349)
        ScatterWidget.setBaseSize(QtCore.QSize(555, 500))
        ScatterWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        ScatterWidget.setStyleSheet("")
        self.horizontalLayout = QtGui.QHBoxLayout(ScatterWidget)
        self.horizontalLayout.setContentsMargins(3, 2, 2, 4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.option_dashboard = QtGui.QWidget(ScatterWidget)
        self.option_dashboard.setObjectName("option_dashboard")
        self.verticalLayout = QtGui.QVBoxLayout(self.option_dashboard)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.xAxisLayout = QtGui.QHBoxLayout()
        self.xAxisLayout.setSpacing(8)
        self.xAxisLayout.setContentsMargins(0, 0, 0, 0)
        self.xAxisLayout.setObjectName("xAxisLayout")
        self.xlabel = QtGui.QLabel(self.option_dashboard)
        self.xlabel.setObjectName("xlabel")
        self.xAxisLayout.addWidget(self.xlabel)
        self.xAxisComboBox = QtGui.QComboBox(self.option_dashboard)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xAxisComboBox.sizePolicy().hasHeightForWidth())
        self.xAxisComboBox.setSizePolicy(sizePolicy)
        self.xAxisComboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.xAxisComboBox.setObjectName("xAxisComboBox")
        self.xAxisLayout.addWidget(self.xAxisComboBox)
        self.xLogCheckBox = QtGui.QCheckBox(self.option_dashboard)
        self.xLogCheckBox.setObjectName("xLogCheckBox")
        self.xAxisLayout.addWidget(self.xLogCheckBox)
        self.xFlipCheckBox = QtGui.QCheckBox(self.option_dashboard)
        self.xFlipCheckBox.setObjectName("xFlipCheckBox")
        self.xAxisLayout.addWidget(self.xFlipCheckBox)
        self.xAxisLayout.setStretch(1, 4)
        self.verticalLayout.addLayout(self.xAxisLayout)
        self.yAxisLayout = QtGui.QHBoxLayout()
        self.yAxisLayout.setSpacing(8)
        self.yAxisLayout.setObjectName("yAxisLayout")
        self.ylabel = QtGui.QLabel(self.option_dashboard)
        self.ylabel.setObjectName("ylabel")
        self.yAxisLayout.addWidget(self.ylabel)
        self.yAxisComboBox = QtGui.QComboBox(self.option_dashboard)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yAxisComboBox.sizePolicy().hasHeightForWidth())
        self.yAxisComboBox.setSizePolicy(sizePolicy)
        self.yAxisComboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.yAxisComboBox.setObjectName("yAxisComboBox")
        self.yAxisLayout.addWidget(self.yAxisComboBox)
        self.yLogCheckBox = QtGui.QCheckBox(self.option_dashboard)
        self.yLogCheckBox.setObjectName("yLogCheckBox")
        self.yAxisLayout.addWidget(self.yLogCheckBox)
        self.yFlipCheckBox = QtGui.QCheckBox(self.option_dashboard)
        self.yFlipCheckBox.setObjectName("yFlipCheckBox")
        self.yAxisLayout.addWidget(self.yFlipCheckBox)
        self.yAxisLayout.setStretch(1, 4)
        self.verticalLayout.addLayout(self.yAxisLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.snapLimits = QtGui.QPushButton(self.option_dashboard)
        self.snapLimits.setObjectName("snapLimits")
        self.horizontalLayout_3.addWidget(self.snapLimits)
        self.swapAxes = QtGui.QPushButton(self.option_dashboard)
        self.swapAxes.setObjectName("swapAxes")
        self.horizontalLayout_3.addWidget(self.swapAxes)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.hidden_attributes = QtGui.QCheckBox(self.option_dashboard)
        self.hidden_attributes.setObjectName("hidden_attributes")
        self.verticalLayout.addWidget(self.hidden_attributes)
        self.line = QtGui.QFrame(self.option_dashboard)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label = QtGui.QLabel(self.option_dashboard)
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setFrameShadow(QtGui.QFrame.Sunken)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.xmin_label = QtGui.QLabel(self.option_dashboard)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xmin_label.sizePolicy().hasHeightForWidth())
        self.xmin_label.setSizePolicy(sizePolicy)
        self.xmin_label.setMinimumSize(QtCore.QSize(40, 0))
        self.xmin_label.setObjectName("xmin_label")
        self.horizontalLayout_4.addWidget(self.xmin_label)
        self.xmin = QtGui.QLineEdit(self.option_dashboard)
        self.xmin.setObjectName("xmin")
        self.horizontalLayout_4.addWidget(self.xmin)
        self.xmax_label = QtGui.QLabel(self.option_dashboard)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xmax_label.sizePolicy().hasHeightForWidth())
        self.xmax_label.setSizePolicy(sizePolicy)
        self.xmax_label.setMinimumSize(QtCore.QSize(40, 0))
        self.xmax_label.setObjectName("xmax_label")
        self.horizontalLayout_4.addWidget(self.xmax_label)
        self.xmax = QtGui.QLineEdit(self.option_dashboard)
        self.xmax.setObjectName("xmax")
        self.horizontalLayout_4.addWidget(self.xmax)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ymin_label = QtGui.QLabel(self.option_dashboard)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ymin_label.sizePolicy().hasHeightForWidth())
        self.ymin_label.setSizePolicy(sizePolicy)
        self.ymin_label.setMinimumSize(QtCore.QSize(40, 0))
        self.ymin_label.setObjectName("ymin_label")
        self.horizontalLayout_5.addWidget(self.ymin_label)
        self.ymin = QtGui.QLineEdit(self.option_dashboard)
        self.ymin.setObjectName("ymin")
        self.horizontalLayout_5.addWidget(self.ymin)
        self.ymax_label = QtGui.QLabel(self.option_dashboard)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ymax_label.sizePolicy().hasHeightForWidth())
        self.ymax_label.setSizePolicy(sizePolicy)
        self.ymax_label.setMinimumSize(QtCore.QSize(40, 0))
        self.ymax_label.setObjectName("ymax_label")
        self.horizontalLayout_5.addWidget(self.ymax_label)
        self.ymax = QtGui.QLineEdit(self.option_dashboard)
        self.ymax.setObjectName("ymax")
        self.horizontalLayout_5.addWidget(self.ymax)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem = QtGui.QSpacerItem(1, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.option_dashboard)

        self.retranslateUi(ScatterWidget)
        QtCore.QMetaObject.connectSlotsByName(ScatterWidget)

    def retranslateUi(self, ScatterWidget):
        ScatterWidget.setWindowTitle(QtGui.QApplication.translate("ScatterWidget", "Scatter Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.xlabel.setText(QtGui.QApplication.translate("ScatterWidget", "x axis", None, QtGui.QApplication.UnicodeUTF8))
        self.xAxisComboBox.setToolTip(QtGui.QApplication.translate("ScatterWidget", "Set which attribute is plotted on the x axis", None, QtGui.QApplication.UnicodeUTF8))
        self.xLogCheckBox.setToolTip(QtGui.QApplication.translate("ScatterWidget", "Toggle on/off log scaling on the x axis", None, QtGui.QApplication.UnicodeUTF8))
        self.xLogCheckBox.setText(QtGui.QApplication.translate("ScatterWidget", "log", None, QtGui.QApplication.UnicodeUTF8))
        self.xFlipCheckBox.setToolTip(QtGui.QApplication.translate("ScatterWidget", "Flip/unflip the order of the x axis", None, QtGui.QApplication.UnicodeUTF8))
        self.xFlipCheckBox.setText(QtGui.QApplication.translate("ScatterWidget", "flip", None, QtGui.QApplication.UnicodeUTF8))
        self.ylabel.setText(QtGui.QApplication.translate("ScatterWidget", "y axis", None, QtGui.QApplication.UnicodeUTF8))
        self.yAxisComboBox.setToolTip(QtGui.QApplication.translate("ScatterWidget", "Set which attribute is plotted on the y axis", None, QtGui.QApplication.UnicodeUTF8))
        self.yLogCheckBox.setToolTip(QtGui.QApplication.translate("ScatterWidget", "Toggle on/off log scaling on the y axis", None, QtGui.QApplication.UnicodeUTF8))
        self.yLogCheckBox.setText(QtGui.QApplication.translate("ScatterWidget", "log", None, QtGui.QApplication.UnicodeUTF8))
        self.yFlipCheckBox.setToolTip(QtGui.QApplication.translate("ScatterWidget", "Flip/unflip the order of the y axis", None, QtGui.QApplication.UnicodeUTF8))
        self.yFlipCheckBox.setText(QtGui.QApplication.translate("ScatterWidget", "flip", None, QtGui.QApplication.UnicodeUTF8))
        self.snapLimits.setToolTip(QtGui.QApplication.translate("ScatterWidget", "Rescale plot limits to fit data", None, QtGui.QApplication.UnicodeUTF8))
        self.snapLimits.setText(QtGui.QApplication.translate("ScatterWidget", "Auto scale", None, QtGui.QApplication.UnicodeUTF8))
        self.swapAxes.setToolTip(QtGui.QApplication.translate("ScatterWidget", "Swap what\'s plotted on the x and y axes", None, QtGui.QApplication.UnicodeUTF8))
        self.swapAxes.setText(QtGui.QApplication.translate("ScatterWidget", "Swap Axes", None, QtGui.QApplication.UnicodeUTF8))
        self.hidden_attributes.setText(QtGui.QApplication.translate("ScatterWidget", "show hidden attributes", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ScatterWidget", "Plot Limits", None, QtGui.QApplication.UnicodeUTF8))
        self.xmin_label.setText(QtGui.QApplication.translate("ScatterWidget", "x min", None, QtGui.QApplication.UnicodeUTF8))
        self.xmax_label.setText(QtGui.QApplication.translate("ScatterWidget", "x max", None, QtGui.QApplication.UnicodeUTF8))
        self.ymin_label.setText(QtGui.QApplication.translate("ScatterWidget", "y min", None, QtGui.QApplication.UnicodeUTF8))
        self.ymax_label.setText(QtGui.QApplication.translate("ScatterWidget", "y max", None, QtGui.QApplication.UnicodeUTF8))

