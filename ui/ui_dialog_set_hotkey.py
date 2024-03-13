# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_set_hotkeyUMSvcP.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(255, 125)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.label_hotkey = QLabel(Dialog)
        self.label_hotkey.setObjectName(u"label_hotkey")

        self.horizontalLayout_2.addWidget(self.label_hotkey)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_confirm = QPushButton(Dialog)
        self.pushButton_confirm.setObjectName(u"pushButton_confirm")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_confirm.sizePolicy().hasHeightForWidth())
        self.pushButton_confirm.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.pushButton_confirm)

        self.pushButton_cancel = QPushButton(Dialog)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        sizePolicy.setHeightForWidth(self.pushButton_cancel.sizePolicy().hasHeightForWidth())
        self.pushButton_cancel.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.pushButton_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u8bbe\u7f6e\u5feb\u6377\u952e", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u5f53\u524d\u5feb\u6377\u952e\uff1a", None))
        self.label_hotkey.setText("")
        self.pushButton_confirm.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

