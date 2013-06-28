# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glue/qt/ui/link_editor.ui'
#
# Created: Fri Jun 28 10:12:41 2013
#      by: pyside-uic 0.2.13 running on glue.external.qt 1.1.0
#
# WARNING! All changes made in this file will be lost!

from glue.external.qt import QtCore, QtGui

class Ui_LinkEditor(object):
    def setupUi(self, LinkEditor):
        LinkEditor.setObjectName("LinkEditor")
        LinkEditor.resize(854, 507)
        LinkEditor.setSizeGripEnabled(False)
        self.horizontalLayout_6 = QtGui.QHBoxLayout(LinkEditor)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.left_components = ComponentSelector(LinkEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_components.sizePolicy().hasHeightForWidth())
        self.left_components.setSizePolicy(sizePolicy)
        self.left_components.setMinimumSize(QtCore.QSize(200, 0))
        self.left_components.setObjectName("left_components")
        self.horizontalLayout_3.addWidget(self.left_components)
        self.right_components = ComponentSelector(LinkEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right_components.sizePolicy().hasHeightForWidth())
        self.right_components.setSizePolicy(sizePolicy)
        self.right_components.setMinimumSize(QtCore.QSize(200, 0))
        self.right_components.setObjectName("right_components")
        self.horizontalLayout_3.addWidget(self.right_components)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.toggle_editor = QtGui.QToolButton(LinkEditor)
        self.toggle_editor.setAutoRaise(True)
        self.toggle_editor.setObjectName("toggle_editor")
        self.verticalLayout_2.addWidget(self.toggle_editor)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(LinkEditor)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.current_links = GlueListWidget(LinkEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_links.sizePolicy().hasHeightForWidth())
        self.current_links.setSizePolicy(sizePolicy)
        self.current_links.setMinimumSize(QtCore.QSize(400, 0))
        self.current_links.setObjectName("current_links")
        self.verticalLayout.addWidget(self.current_links)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add_link = QtGui.QPushButton(LinkEditor)
        self.add_link.setObjectName("add_link")
        self.horizontalLayout_2.addWidget(self.add_link)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.remove_link = QtGui.QPushButton(LinkEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_link.sizePolicy().hasHeightForWidth())
        self.remove_link.setSizePolicy(sizePolicy)
        self.remove_link.setObjectName("remove_link")
        self.horizontalLayout_2.addWidget(self.remove_link)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.buttonBox = QtGui.QDialogButtonBox(LinkEditor)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.signature_editor = LinkEquation(LinkEditor)
        self.signature_editor.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.signature_editor.sizePolicy().hasHeightForWidth())
        self.signature_editor.setSizePolicy(sizePolicy)
        self.signature_editor.setAcceptDrops(True)
        self.signature_editor.setObjectName("signature_editor")
        self.horizontalLayout_5.addWidget(self.signature_editor)
        spacerItem2 = QtGui.QSpacerItem(400, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.retranslateUi(LinkEditor)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), LinkEditor.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), LinkEditor.reject)
        QtCore.QMetaObject.connectSlotsByName(LinkEditor)

    def retranslateUi(self, LinkEditor):
        LinkEditor.setWindowTitle(QtGui.QApplication.translate("LinkEditor", "Link Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.toggle_editor.setWhatsThis(QtGui.QApplication.translate("LinkEditor", "Show/hide advanced linking", None, QtGui.QApplication.UnicodeUTF8))
        self.toggle_editor.setText(QtGui.QApplication.translate("LinkEditor", "Advanced", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("LinkEditor", "Current Links", None, QtGui.QApplication.UnicodeUTF8))
        self.add_link.setText(QtGui.QApplication.translate("LinkEditor", "Glue", None, QtGui.QApplication.UnicodeUTF8))
        self.remove_link.setText(QtGui.QApplication.translate("LinkEditor", "Unglue", None, QtGui.QApplication.UnicodeUTF8))

from ..link_equation import LinkEquation
from ..qtutil import GlueListWidget
from ..component_selector import ComponentSelector