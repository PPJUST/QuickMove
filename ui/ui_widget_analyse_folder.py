# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_analyse_pathsQbmDe.ui'
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
        Form.resize(345, 40)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolButton_analyse = QToolButton(Form)
        self.toolButton_analyse.setObjectName(u"toolButton_analyse")

        self.horizontalLayout.addWidget(self.toolButton_analyse)

        self.layout_drop = QVBoxLayout()
        self.layout_drop.setSpacing(0)
        self.layout_drop.setObjectName(u"layout_drop")

        self.horizontalLayout.addLayout(self.layout_drop)

        self.toolButton_ask = QToolButton(Form)
        self.toolButton_ask.setObjectName(u"toolButton_ask")

        self.horizontalLayout.addWidget(self.toolButton_ask)

        self.toolButton_open = QToolButton(Form)
        self.toolButton_open.setObjectName(u"toolButton_open")

        self.horizontalLayout.addWidget(self.toolButton_open)

        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.toolButton_analyse.setText(QCoreApplication.translate("Form", u"search", None))
        self.toolButton_ask.setText(QCoreApplication.translate("Form", u"ask", None))
        self.toolButton_open.setText(QCoreApplication.translate("Form", u"open", None))
    # retranslateUi

