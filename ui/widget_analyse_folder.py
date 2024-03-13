# 分析需要整理的文件夹的控件
import os

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from constant import ICON_ASK_FOLDER, ICON_ANALYSE, ICON_OPEN_FOLDER
from module import function_config, function_analyse_folder
from ui.lineedit_drop_path import LineEditDropPath
from ui.ui_widget_analyse_folder import Ui_Form


class WidgetAnalyseFolder(QWidget):
    """分析需要整理的文件夹的控件"""
    signal_dropped = Signal(str)
    signal_analysed = Signal(list)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 添加自定义控件
        self.lineEdit_drop = LineEditDropPath()
        self.ui.layout_drop.addWidget(self.lineEdit_drop)

        # 设置ui属性
        self.ui.toolButton_analyse.setIcon(QIcon(ICON_ANALYSE))
        self.ui.toolButton_ask.setIcon(QIcon(ICON_ASK_FOLDER))
        self.ui.toolButton_open.setIcon(QIcon(ICON_OPEN_FOLDER))
        self.load_setting()

        # 连接信号与槽函数
        self.lineEdit_drop.signal_dropped.connect(self.reset_path)
        self.lineEdit_drop.signal_is_exist.connect(self.check_path_exist)
        self.ui.toolButton_analyse.clicked.connect(self.analyse_path)
        self.ui.toolButton_ask.clicked.connect(self.ask_folder)
        self.ui.toolButton_open.clicked.connect(self.open_folder)

    def load_setting(self):
        """加载设置"""
        path = function_config.get_analyse_dirpath()
        self.lineEdit_drop.setText(path)

    def reset_path(self, path: str):
        if path != function_config.get_analyse_dirpath():
            function_config.set_analyse_dirpath(path)
            self.signal_dropped.emit(path)

    def check_path_exist(self, is_exist: bool):
        """检查路径有效性"""
        self.ui.toolButton_analyse.setEnabled(is_exist)
        self.ui.toolButton_open.setEnabled(is_exist)

    def analyse_path(self):
        """分析路径"""
        extract_paths = function_analyse_folder.extract()
        self.signal_analysed.emit(extract_paths)

    def ask_folder(self):
        """弹出文件夹选择对话框"""
        dirpath = QFileDialog.getExistingDirectory(self, '选择文件夹')
        if dirpath:
            self.lineEdit_drop.reset_path(dirpath)
            function_config.set_analyse_dirpath(dirpath)

    def open_folder(self):
        """打开文件夹路径"""
        os.startfile(self.lineEdit_drop.text())
