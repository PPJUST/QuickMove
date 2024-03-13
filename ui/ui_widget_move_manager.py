# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_move_managerkchbwr.ui'
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
        Form.resize(340, 301)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.spinBox_folder_count = QSpinBox(Form)
        self.spinBox_folder_count.setObjectName(u"spinBox_folder_count")
        self.spinBox_folder_count.setMinimum(1)
        self.spinBox_folder_count.setMaximum(9)

        self.horizontalLayout.addWidget(self.spinBox_folder_count)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.widget_move_folders = QWidget()
        self.widget_move_folders.setObjectName(u"widget_move_folders")
        self.widget_move_folders.setGeometry(QRect(0, 0, 338, 243))
        self.verticalLayout = QVBoxLayout(self.widget_move_folders)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.scrollArea.setWidget(self.widget_move_folders)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_skip = QPushButton(Form)
        self.pushButton_skip.setObjectName(u"pushButton_skip")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_skip.sizePolicy().hasHeightForWidth())
        self.pushButton_skip.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.pushButton_skip)

        self.pushButton_cancel = QPushButton(Form)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        sizePolicy.setHeightForWidth(self.pushButton_cancel.sizePolicy().hasHeightForWidth())
        self.pushButton_cancel.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.pushButton_cancel)

        self.pushButton_delete = QPushButton(Form)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        sizePolicy.setHeightForWidth(self.pushButton_delete.sizePolicy().hasHeightForWidth())
        self.pushButton_delete.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.pushButton_delete)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u5939\u6570\u91cf\uff1a", None))
        self.pushButton_skip.setText(QCoreApplication.translate("Form", u"\u8df3\u8fc7", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Form", u"\u64a4\u9500", None))
        self.pushButton_delete.setText(QCoreApplication.translate("Form", u"\u5220\u9664", None))
    # retranslateUi

