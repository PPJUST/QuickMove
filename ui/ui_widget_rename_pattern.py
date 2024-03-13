# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_rename_patternlyHLro.ui'
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
        Form.resize(287, 45)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit_pattern = QLineEdit(Form)
        self.lineEdit_pattern.setObjectName(u"lineEdit_pattern")

        self.horizontalLayout_2.addWidget(self.lineEdit_pattern)

        self.toolButton_info = QToolButton(Form)
        self.toolButton_info.setObjectName(u"toolButton_info")
        self.toolButton_info.setAutoRaise(True)
        self.toolButton_info.setArrowType(Qt.NoArrow)

        self.horizontalLayout_2.addWidget(self.toolButton_info)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_pattern = QLabel(Form)
        self.label_pattern.setObjectName(u"label_pattern")
        self.label_pattern.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label_pattern)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u547d\u540d\u6a21\u677f\uff1a", None))
        self.toolButton_info.setText(QCoreApplication.translate("Form", u"info", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u9884\u671f\u6587\u4ef6\u540d\uff1a", None))
        self.label_pattern.setText("")
    # retranslateUi

