# 单个移动目标文件夹的子控件
import os.path

from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *
from pynput import keyboard

from constant import ICON_ASK_FOLDER, ICON_MOVE, ICON_OPEN_FOLDER, ICON_CLEAR
from module import function_config
from ui.lineedit_drop_path import LineEditDropPath
from ui.ui_widget_move_folder import Ui_Frame


class WidgetMoveFolder(QFrame):
    """单个移动目标文件夹的子控件"""
    signal_dropped = Signal(str)
    signal_click_move_button = Signal(str)

    def __init__(self, index=0):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        # 初始化
        self.target_dirpath = None  # 目标文件夹
        self.index = index  # 当前控件组的编号（从1开始）
        self._hotkey_thread = None

        # 添加自定义控件
        self.lineEdit_drop = LineEditDropPath()
        self.ui.layout_drop.addWidget(self.lineEdit_drop)

        # 设置ui属性
        self.setMaximumHeight(60)
        self.ui.toolButton_move.setIcon(QIcon(ICON_MOVE))
        self.ui.toolButton_ask_folder.setIcon(QIcon(ICON_ASK_FOLDER))
        self.ui.toolButton_open_folder.setIcon(QIcon(ICON_OPEN_FOLDER))
        self.ui.toolButton_clear_folder.setIcon(QIcon(ICON_CLEAR))
        self.load_setting()
        self.ui.pushButton_hotkey.setEnabled(False)

        # 连接信号与槽函数
        self.ui.toolButton_move.clicked.connect(self.do_move)
        self.lineEdit_drop.signal_dropped.connect(self.reset_path)
        self.lineEdit_drop.signal_is_exist.connect(self.check_path_exist)
        self.ui.toolButton_ask_folder.clicked.connect(self.ask_folder)
        self.ui.toolButton_open_folder.clicked.connect(self.open_folder)
        self.ui.toolButton_clear_folder.clicked.connect(self.clear_path)
        self.ui.pushButton_hotkey.clicked.connect(self.set_hotkey)

    def load_setting(self):
        """加载设置"""
        path = function_config.get_setting_target_dirpath(self.index)
        self.lineEdit_drop.setText(path)
        self.target_dirpath = path
        # 绑定快捷键
        hotkey = function_config.get_move_hotkey(self.index)
        self.ui.pushButton_hotkey.setText(hotkey)
        self.bind_hotkey(hotkey)

    def do_move(self):
        """移动当前任务"""
        if self.target_dirpath and os.path.exists(self.target_dirpath):
            self.signal_click_move_button.emit(self.target_dirpath)

    def reset_path(self, path: str):
        self.lineEdit_drop.setText(path)
        if path != self.target_dirpath:
            self.target_dirpath = path
            function_config.set_setting_target_dirpath(self.index, path)
            self.signal_dropped.emit(self.target_dirpath)

    def check_path_exist(self, is_exist: bool):
        """检查路径有效性"""
        self.ui.toolButton_move.setEnabled(is_exist)
        self.ui.toolButton_open_folder.setEnabled(is_exist)

    def ask_folder(self):
        """弹出文件夹选择对话框"""
        dirpath = QFileDialog.getExistingDirectory(self, '选择文件夹')
        if dirpath:
            self.lineEdit_drop.reset_path(dirpath)

    def open_folder(self):
        """打开文件夹路径"""
        os.startfile(self.target_dirpath)

    def clear_path(self):
        """清除路径"""
        self.lineEdit_drop.reset_path('')

    def set_hotkey(self):
        """设置快捷键"""
        new_hotkey = None  # 备忘录 - TBD 弹出dialog
        function_config.set_move_hotkey(self.index, new_hotkey)
        self.bind_hotkey(new_hotkey)  # 重新绑定

    def bind_hotkey(self, hotkey):
        """绑定快捷键"""
        if self._hotkey_thread:  # 先停止再绑定
            self._hotkey_thread.stop()
        self._hotkey_thread = keyboard.GlobalHotKeys({
            hotkey: self.do_move, })

    def enable_hotkey(self):
        """启用快捷键"""
        hotkey = self.ui.pushButton_hotkey.text()
        self.bind_hotkey(hotkey)  # pynput的监听线程在stop后无法重新start，需要重新绑定
        self._hotkey_thread.start()

    def disable_hotkey(self):
        """停用快捷键"""
        self._hotkey_thread.stop()
