# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_renamecJsnhE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(307, 133)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_add_prefix = QLineEdit(Dialog)
        self.lineEdit_add_prefix.setObjectName(u"lineEdit_add_prefix")

        self.gridLayout.addWidget(self.lineEdit_add_prefix, 0, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_filename = QLineEdit(Dialog)
        self.lineEdit_filename.setObjectName(u"lineEdit_filename")

        self.gridLayout.addWidget(self.lineEdit_filename, 1, 1, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit_add_suffix = QLineEdit(Dialog)
        self.lineEdit_add_suffix.setObjectName(u"lineEdit_add_suffix")

        self.gridLayout.addWidget(self.lineEdit_add_suffix, 2, 1, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.lineEdit_file_suffix = QLineEdit(Dialog)
        self.lineEdit_file_suffix.setObjectName(u"lineEdit_file_suffix")
        self.lineEdit_file_suffix.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_file_suffix, 3, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 2)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u524d\u7f00\u8bcd\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u6587\u4ef6\u540d\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u540e\u7f00\u8bcd\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u540e\u7f00\u683c\u5f0f\uff1a", None))
    # retranslateUi

