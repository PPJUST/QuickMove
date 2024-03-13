# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_settingsssnpxl.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QFrame,
    QGridLayout, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(231, 123)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(3, 0, 0, 0)
        self.radioButton_mode_move_file = QRadioButton(self.frame)
        self.buttonGroup_mode_move = QButtonGroup(Form)
        self.buttonGroup_mode_move.setObjectName(u"buttonGroup_mode_move")
        self.buttonGroup_mode_move.addButton(self.radioButton_mode_move_file)
        self.radioButton_mode_move_file.setObjectName(u"radioButton_mode_move_file")

        self.verticalLayout_5.addWidget(self.radioButton_mode_move_file)

        self.radioButton_mode_move_folder = QRadioButton(self.frame)
        self.buttonGroup_mode_move.addButton(self.radioButton_mode_move_folder)
        self.radioButton_mode_move_folder.setObjectName(u"radioButton_mode_move_folder")

        self.verticalLayout_5.addWidget(self.radioButton_mode_move_folder)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(3, 0, 0, 0)
        self.checkBox_auto_open_current = QCheckBox(self.frame_3)
        self.checkBox_auto_open_current.setObjectName(u"checkBox_auto_open_current")

        self.verticalLayout_7.addWidget(self.checkBox_auto_open_current)

        self.checkBox_auto_open_parent = QCheckBox(self.frame_3)
        self.checkBox_auto_open_parent.setObjectName(u"checkBox_auto_open_parent")

        self.verticalLayout_7.addWidget(self.checkBox_auto_open_parent)

        self.checkBox_reconfirm_rename = QCheckBox(self.frame_3)
        self.checkBox_reconfirm_rename.setObjectName(u"checkBox_reconfirm_rename")

        self.verticalLayout_7.addWidget(self.checkBox_reconfirm_rename)


        self.gridLayout.addWidget(self.frame_3, 0, 1, 1, 1)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(3, 0, 0, 0)
        self.radioButton_mode_walk_single = QRadioButton(self.frame_2)
        self.buttonGroup_mode_walk = QButtonGroup(Form)
        self.buttonGroup_mode_walk.setObjectName(u"buttonGroup_mode_walk")
        self.buttonGroup_mode_walk.addButton(self.radioButton_mode_walk_single)
        self.radioButton_mode_walk_single.setObjectName(u"radioButton_mode_walk_single")

        self.verticalLayout_6.addWidget(self.radioButton_mode_walk_single)

        self.radioButton_mode_walk_all = QRadioButton(self.frame_2)
        self.buttonGroup_mode_walk.addButton(self.radioButton_mode_walk_all)
        self.radioButton_mode_walk_all.setObjectName(u"radioButton_mode_walk_all")

        self.verticalLayout_6.addWidget(self.radioButton_mode_walk_all)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_information = QPushButton(self.frame_4)
        self.pushButton_information.setObjectName(u"pushButton_information")

        self.verticalLayout_8.addWidget(self.pushButton_information)

        self.pushButton_hotkeys_setting = QPushButton(self.frame_4)
        self.pushButton_hotkeys_setting.setObjectName(u"pushButton_hotkeys_setting")

        self.verticalLayout_8.addWidget(self.pushButton_hotkeys_setting)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.radioButton_mode_move_file.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u6a21\u5f0f", None))
        self.radioButton_mode_move_folder.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u5939\u6a21\u5f0f", None))
        self.checkBox_auto_open_current.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u6253\u5f00\u6587\u4ef6", None))
        self.checkBox_auto_open_parent.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u6253\u5f00\u6240\u5728\u76ee\u5f55", None))
        self.checkBox_reconfirm_rename.setText(QCoreApplication.translate("Form", u"\u624b\u52a8\u6539\u540d", None))
        self.radioButton_mode_walk_single.setText(QCoreApplication.translate("Form", u"\u904d\u5386\u5355\u5c42\u4e0b\u7ea7", None))
        self.radioButton_mode_walk_all.setText(QCoreApplication.translate("Form", u"\u904d\u5386\u5168\u90e8\u5c42\u7ea7", None))
        self.pushButton_information.setText(QCoreApplication.translate("Form", u"\u8f6f\u4ef6\u8bf4\u660e", None))
        self.pushButton_hotkeys_setting.setText(QCoreApplication.translate("Form", u"\u5feb\u6377\u952e\u8bbe\u7f6e", None))
    # retranslateUi

