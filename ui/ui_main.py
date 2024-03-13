# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainHvtFvH.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 540)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layout_widget_drop = QVBoxLayout()
        self.layout_widget_drop.setSpacing(0)
        self.layout_widget_drop.setObjectName(u"layout_widget_drop")

        self.verticalLayout.addLayout(self.layout_widget_drop)

        self.layout_rate = QVBoxLayout()
        self.layout_rate.setSpacing(0)
        self.layout_rate.setObjectName(u"layout_rate")

        self.verticalLayout.addLayout(self.layout_rate)

        self.layout_history = QVBoxLayout()
        self.layout_history.setSpacing(0)
        self.layout_history.setObjectName(u"layout_history")

        self.verticalLayout.addLayout(self.layout_history)

        self.verticalLayout.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.layout_config = QVBoxLayout()
        self.layout_config.setSpacing(0)
        self.layout_config.setObjectName(u"layout_config")

        self.verticalLayout_2.addLayout(self.layout_config)

        self.layout_settings = QVBoxLayout()
        self.layout_settings.setObjectName(u"layout_settings")

        self.verticalLayout_2.addLayout(self.layout_settings)

        self.layout_rename_pattern = QVBoxLayout()
        self.layout_rename_pattern.setObjectName(u"layout_rename_pattern")

        self.verticalLayout_2.addLayout(self.layout_rename_pattern)

        self.layout_widget_move = QVBoxLayout()
        self.layout_widget_move.setObjectName(u"layout_widget_move")

        self.verticalLayout_2.addLayout(self.layout_widget_move)

        self.verticalLayout_2.setStretch(3, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"QuickMove", None))
    # retranslateUi

