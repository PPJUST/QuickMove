# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uinjRdKE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from DropLineEdit import DropLineEdit

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(586, 475)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_7 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_check_origin_path = QPushButton(self.widget_2)
        self.button_check_origin_path.setObjectName(u"button_check_origin_path")
        self.button_check_origin_path.setMaximumSize(QSize(50, 16777215))
        icon = QIcon()
        icon.addFile(u"res_icon/\u786e\u8ba4.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_check_origin_path.setIcon(icon)

        self.horizontalLayout.addWidget(self.button_check_origin_path)

        self.lineedit_origin_path = DropLineEdit(self.widget_2)
        self.lineedit_origin_path.setObjectName(u"lineedit_origin_path")
        self.lineedit_origin_path.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.lineedit_origin_path)

        self.button_ask_origin_path = QToolButton(self.widget_2)
        self.button_ask_origin_path.setObjectName(u"button_ask_origin_path")
        icon1 = QIcon()
        icon1.addFile(u"res_icon/\u9009\u62e9\u6587\u4ef6\u5939.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_ask_origin_path.setIcon(icon1)

        self.horizontalLayout.addWidget(self.button_ask_origin_path)

        self.button_open_origin_path = QPushButton(self.widget_2)
        self.button_open_origin_path.setObjectName(u"button_open_origin_path")
        self.button_open_origin_path.setMaximumSize(QSize(16777215, 16777215))
        icon2 = QIcon()
        icon2.addFile(u"res_icon/\u6253\u5f00\u6587\u4ef6\u5939.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_open_origin_path.setIcon(icon2)

        self.horizontalLayout.addWidget(self.button_open_origin_path)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_8.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.label_schedule = QLabel(self.widget_2)
        self.label_schedule.setObjectName(u"label_schedule")

        self.horizontalLayout_8.addWidget(self.label_schedule)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.label_current = QLabel(self.widget_2)
        self.label_current.setObjectName(u"label_current")
        self.label_current.setMaximumSize(QSize(280, 16777215))
        self.label_current.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_current)

        self.text_info = QTextBrowser(self.widget_2)
        self.text_info.setObjectName(u"text_info")
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(10)
        self.text_info.setFont(font)

        self.verticalLayout_3.addWidget(self.text_info)


        self.horizontalLayout_7.addWidget(self.widget_2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_2.addWidget(self.label_3)

        self.combobox_config = QComboBox(self.widget)
        self.combobox_config.setObjectName(u"combobox_config")
        self.combobox_config.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.combobox_config)

        self.button_add_config = QPushButton(self.widget)
        self.button_add_config.setObjectName(u"button_add_config")
        self.button_add_config.setMaximumSize(QSize(16777215, 16777215))
        icon3 = QIcon()
        icon3.addFile(u"res_icon/\u52a0\u53f7.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_add_config.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.button_add_config)

        self.button_delete_config = QPushButton(self.widget)
        self.button_delete_config.setObjectName(u"button_delete_config")
        self.button_delete_config.setMaximumSize(QSize(16777215, 16777215))
        icon4 = QIcon()
        icon4.addFile(u"res_icon/\u51cf\u53f7.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_delete_config.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.button_delete_config)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.radiobutton_model_file = QRadioButton(self.widget)
        self.radiobutton_model_file.setObjectName(u"radiobutton_model_file")
        self.radiobutton_model_file.setChecked(True)

        self.verticalLayout_5.addWidget(self.radiobutton_model_file)

        self.radiobutton_model_folder = QRadioButton(self.widget)
        self.radiobutton_model_folder.setObjectName(u"radiobutton_model_folder")
        self.radiobutton_model_folder.setChecked(False)

        self.verticalLayout_5.addWidget(self.radiobutton_model_folder)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkbox_auto_open = QCheckBox(self.widget)
        self.checkbox_auto_open.setObjectName(u"checkbox_auto_open")

        self.verticalLayout.addWidget(self.checkbox_auto_open)

        self.checkbox_manual_rename = QCheckBox(self.widget)
        self.checkbox_manual_rename.setObjectName(u"checkbox_manual_rename")

        self.verticalLayout.addWidget(self.checkbox_manual_rename)


        self.horizontalLayout_6.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.lineedit_add_prefix = QLineEdit(self.widget)
        self.lineedit_add_prefix.setObjectName(u"lineedit_add_prefix")

        self.horizontalLayout_5.addWidget(self.lineedit_add_prefix)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_9.addWidget(self.label_6)

        self.lineedit_add_suffix = QLineEdit(self.widget)
        self.lineedit_add_suffix.setObjectName(u"lineedit_add_suffix")

        self.horizontalLayout_9.addWidget(self.lineedit_add_suffix)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_4.addWidget(self.label_5)

        self.spinbox_folder_number = QSpinBox(self.widget)
        self.spinbox_folder_number.setObjectName(u"spinbox_folder_number")
        self.spinbox_folder_number.setMinimum(1)
        self.spinbox_folder_number.setMaximum(10)

        self.horizontalLayout_4.addWidget(self.spinbox_folder_number)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_movefolders = QWidget()
        self.scrollAreaWidgetContents_movefolders.setObjectName(u"scrollAreaWidgetContents_movefolders")
        self.scrollAreaWidgetContents_movefolders.setGeometry(QRect(0, 0, 279, 273))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_movefolders)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_movefolders)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_pass = QPushButton(self.widget)
        self.button_pass.setObjectName(u"button_pass")
        self.button_pass.setMinimumSize(QSize(0, 0))
        self.button_pass.setMaximumSize(QSize(16777215, 16777215))
        icon5 = QIcon()
        icon5.addFile(u"res_icon/\u8df3\u8fc7.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_pass.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.button_pass)

        self.button_undo_pre = QPushButton(self.widget)
        self.button_undo_pre.setObjectName(u"button_undo_pre")
        icon6 = QIcon()
        icon6.addFile(u"res_icon/\u64a4\u56de.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_undo_pre.setIcon(icon6)

        self.horizontalLayout_3.addWidget(self.button_undo_pre)

        self.button_quit = QPushButton(self.widget)
        self.button_quit.setObjectName(u"button_quit")
        icon7 = QIcon()
        icon7.addFile(u"res_icon/\u9000\u51fa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_quit.setIcon(icon7)

        self.horizontalLayout_3.addWidget(self.button_quit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_7.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_check_origin_path.setText("")
        self.button_ask_origin_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.button_open_origin_path.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u6587\u4ef6/\u6587\u4ef6\u5939\uff1a", None))
        self.label_schedule.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u8fdb\u5ea6", None))
        self.label_current.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u5f53\u524d\u6587\u4ef6/\u6587\u4ef6\u5939", None))
        self.text_info.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u65e5\u5fd7", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\uff1a", None))
        self.button_add_config.setText("")
        self.button_delete_config.setText("")
        self.radiobutton_model_file.setText(QCoreApplication.translate("MainWindow", u"\u79fb\u52a8\u6587\u4ef6", None))
        self.radiobutton_model_folder.setText(QCoreApplication.translate("MainWindow", u"\u79fb\u52a8\u6587\u4ef6\u5939", None))
        self.checkbox_auto_open.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u6253\u5f00\u4e0b\u4e2a\u6587\u4ef6", None))
        self.checkbox_manual_rename.setText(QCoreApplication.translate("MainWindow", u"\u624b\u52a8\u6539\u540d", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u901a\u7528\u524d\u7f00", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u901a\u7528\u540e\u7f00", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u6587\u4ef6\u5939\u6570", None))
        self.button_pass.setText("")
        self.button_undo_pre.setText("")
        self.button_quit.setText("")
    # retranslateUi

