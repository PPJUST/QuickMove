# 相关设置项的控件
from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *

from constant import ICON_HOTKEY, ICON_INFORMATION
from module import function_config
from ui.ui_widget_settings import Ui_Form


class WidgetSettings(QWidget):
    """相关设置项的控件"""
    signal_special_setting_changed = Signal(object)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # 设置ui属性
        self.ui.pushButton_information.setIcon(QIcon(ICON_INFORMATION))
        self.ui.pushButton_hotkeys_setting.setIcon(QIcon(ICON_HOTKEY))
        self.load_setting()
        self.ui.pushButton_hotkeys_setting.setEnabled(False)

        # 连接信号与槽函数
        self.ui.buttonGroup_mode_move.buttonClicked.connect(self.change_mode_move)
        self.ui.buttonGroup_mode_move.buttonClicked.connect(self.signal_special_setting_changed.emit)
        self.ui.buttonGroup_mode_walk.buttonClicked.connect(self.change_mode_walk)
        self.ui.buttonGroup_mode_walk.buttonClicked.connect(self.signal_special_setting_changed.emit)
        self.ui.checkBox_auto_open_file.stateChanged.connect(self.change_auto_open_file)
        self.ui.checkBox_auto_open_path.stateChanged.connect(self.change_auto_open_path)
        self.ui.checkBox_reconfirm_rename.stateChanged.connect(self.change_reconfirm_rename)
        self.ui.pushButton_information.clicked.connect(self.open_information)
        self.ui.pushButton_hotkeys_setting.clicked.connect(self.set_hotkeys)

    def load_setting(self):
        """加载设置"""
        # 文件模式
        mode_move = function_config.get_setting_mode_move()
        if mode_move == 'file':
            self.ui.radioButton_mode_move_file.setChecked(True)
        else:
            self.ui.radioButton_mode_move_folder.setChecked(True)
        # 层级
        mode_walk = function_config.get_setting_mode_walk()
        if mode_walk == 'single':
            self.ui.radioButton_mode_walk_single.setChecked(True)
        else:
            self.ui.radioButton_mode_walk_all.setChecked(True)
        # 自动打开
        self.ui.checkBox_auto_open_file.setChecked(function_config.get_setting_auto_open_file())
        self.ui.checkBox_auto_open_path.setChecked(function_config.get_setting_auto_open_path())
        # 手动重命名
        self.ui.checkBox_reconfirm_rename.setChecked(function_config.get_setting_reconfirm_rename())

    def change_mode_move(self):
        """修改检查文件类型选项"""
        if self.ui.radioButton_mode_move_file.isChecked():
            function_config.set_setting_mode_move('file')
        else:
            function_config.set_setting_mode_move('folder')

    def change_mode_walk(self):
        """修改检查文件层级选项"""
        if self.ui.radioButton_mode_walk_single.isChecked():
            function_config.set_setting_mode_walk('single')
        else:
            function_config.set_setting_mode_walk('all')

    def change_auto_open_file(self):
        """修改自动打开选项"""
        is_checked = self.ui.checkBox_auto_open_file.isChecked()
        function_config.set_setting_auto_open_file(is_checked)

    def change_auto_open_path(self):
        """修改自动打开选项"""
        is_checked = self.ui.checkBox_auto_open_path.isChecked()
        function_config.set_setting_auto_open_path(is_checked)

    def change_reconfirm_rename(self):
        """手动重命名选项"""
        is_checked = self.ui.checkBox_reconfirm_rename.isChecked()
        function_config.set_setting_reconfirm_rename(is_checked)

    def open_information(self):
        """打开软件说明"""

    def set_hotkeys(self):
        """设置快捷键"""
