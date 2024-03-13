# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_move_folderXUIcRy.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(310, 63)
        Frame.setFrameShape(QFrame.Box)
        Frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(Frame)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.toolButton_move = QToolButton(Frame)
        self.toolButton_move.setObjectName(u"toolButton_move")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_move.sizePolicy().hasHeightForWidth())
        self.toolButton_move.setSizePolicy(sizePolicy)
        self.toolButton_move.setAutoRaise(False)
        self.toolButton_move.setArrowType(Qt.NoArrow)

        self.horizontalLayout_3.addWidget(self.toolButton_move)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.layout_drop = QVBoxLayout()
        self.layout_drop.setObjectName(u"layout_drop")

        self.horizontalLayout.addLayout(self.layout_drop)

        self.toolButton_ask_folder = QToolButton(Frame)
        self.toolButton_ask_folder.setObjectName(u"toolButton_ask_folder")

        self.horizontalLayout.addWidget(self.toolButton_ask_folder)

        self.toolButton_clear_folder = QToolButton(Frame)
        self.toolButton_clear_folder.setObjectName(u"toolButton_clear_folder")

        self.horizontalLayout.addWidget(self.toolButton_clear_folder)

        self.toolButton_open_folder = QToolButton(Frame)
        self.toolButton_open_folder.setObjectName(u"toolButton_open_folder")

        self.horizontalLayout.addWidget(self.toolButton_open_folder)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.pushButton_hotkey = QPushButton(Frame)
        self.pushButton_hotkey.setObjectName(u"pushButton_hotkey")

        self.horizontalLayout_2.addWidget(self.pushButton_hotkey)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.toolButton_move.setText(QCoreApplication.translate("Frame", u"move", None))
        self.toolButton_ask_folder.setText(QCoreApplication.translate("Frame", u"ask", None))
        self.toolButton_clear_folder.setText(QCoreApplication.translate("Frame", u"clear", None))
        self.toolButton_open_folder.setText(QCoreApplication.translate("Frame", u"open", None))
        self.label.setText(QCoreApplication.translate("Frame", u"\u5feb\u6377\u952e\uff1a", None))
        self.pushButton_hotkey.setText(QCoreApplication.translate("Frame", u"hotkey", None))
    # retranslateUi

