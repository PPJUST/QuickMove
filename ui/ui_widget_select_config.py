# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_select_configqSWNvI.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(270, 40)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox_config = QComboBox(Form)
        self.comboBox_config.setObjectName(u"comboBox_config")

        self.horizontalLayout.addWidget(self.comboBox_config)

        self.toolButton_add = QToolButton(Form)
        self.toolButton_add.setObjectName(u"toolButton_add")

        self.horizontalLayout.addWidget(self.toolButton_add)

        self.toolButton_delete = QToolButton(Form)
        self.toolButton_delete.setObjectName(u"toolButton_delete")

        self.horizontalLayout.addWidget(self.toolButton_delete)

        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u914d\u7f6e\uff1a", None))
        self.toolButton_add.setText(QCoreApplication.translate("Form", u"add", None))
        self.toolButton_delete.setText(QCoreApplication.translate("Form", u"del", None))
    # retranslateUi

