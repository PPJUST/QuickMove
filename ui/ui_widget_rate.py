# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_rateXDevRX.ui'
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
        Form.resize(214, 67)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_current_index = QLabel(Form)
        self.label_current_index.setObjectName(u"label_current_index")

        self.horizontalLayout.addWidget(self.label_current_index)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_total_count = QLabel(Form)
        self.label_total_count.setObjectName(u"label_total_count")

        self.horizontalLayout.addWidget(self.label_total_count)

        self.toolButton_open_dir = QToolButton(Form)
        self.toolButton_open_dir.setObjectName(u"toolButton_open_dir")

        self.horizontalLayout.addWidget(self.toolButton_open_dir)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_current_path = QLabel(Form)
        self.label_current_path.setObjectName(u"label_current_path")
        self.label_current_path.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_current_path)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8fdb\u5ea6\uff1a", None))
        self.label_current_index.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"/", None))
        self.label_total_count.setText(QCoreApplication.translate("Form", u"0", None))
        self.toolButton_open_dir.setText(QCoreApplication.translate("Form", u"open", None))
        self.label_current_path.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u5bf9\u5e94\u8def\u5f84", None))
    # retranslateUi

