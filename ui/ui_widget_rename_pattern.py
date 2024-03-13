# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_rename_patternoTeALj.ui'
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
        Form.resize(331, 75)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_pattern = QLineEdit(Form)
        self.lineEdit_pattern.setObjectName(u"lineEdit_pattern")

        self.horizontalLayout.addWidget(self.lineEdit_pattern)

        self.toolButton_info = QToolButton(Form)
        self.toolButton_info.setObjectName(u"toolButton_info")
        self.toolButton_info.setAutoRaise(True)
        self.toolButton_info.setArrowType(Qt.NoArrow)

        self.horizontalLayout.addWidget(self.toolButton_info)

        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u547d\u540d\u6a21\u677f\uff1a", None))
        self.toolButton_info.setText(QCoreApplication.translate("Form", u"info", None))
    # retranslateUi

