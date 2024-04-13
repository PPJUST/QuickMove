# 显示进度的控件
import os

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *

from constant import ICON_OPEN_FOLDER
from module import function_open_file, pynput_fix_hotkey
from ui.ui_widget_rate import Ui_Form


class WidgetRate(QWidget):
    """显示进度的控件"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._hotkey_thread = None
        self.bind_hotkey()
        # 设置ui属性
        self.ui.toolButton_open_dir.setIcon(QIcon(ICON_OPEN_FOLDER))
        # 连接信号与槽函数
        self.ui.toolButton_open_dir.clicked.connect(self.open_dir)

    def open_dir(self):
        """打开当前进度对应的路径"""
        path = self.ui.label_current_path.text()
        if not path or not os.path.exists(path):
            return
        function_open_file.open_path(path)

    def reset_current_index(self, text):
        if text == 0:
            text = '-'
        self.ui.label_current_index.setText(str(text))

    def reset_total_count(self, text):
        self.ui.label_total_count.setText(str(text))

    def reset_current_path(self, text):
        self.ui.label_current_path.setText(str(text))

    def bind_hotkey(self):
        """绑定快捷键"""
        if self._hotkey_thread:  # 先停止再绑定
            self._hotkey_thread.stop()
        self._hotkey_thread = pynput_fix_hotkey.GlobalHotKeysFix({
            '<alt_gr>+<96>': self.open_dir, })

    def enable_hotkey(self):
        """启用快捷键"""
        self.bind_hotkey()  # pynput的监听线程在stop后无法重新start，需要重新绑定
        self._hotkey_thread.start()

    def disable_hotkey(self):
        """停用快捷键"""
        self._hotkey_thread.stop()
