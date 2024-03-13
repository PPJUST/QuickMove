# 设置快捷键的dialog

from PySide6.QtWidgets import *

from ui.ui_dialog_set_hotkey import Ui_Dialog
from pynput import keyboard


class DialogSetHotkey(QDialog):
    """设置快捷键的dialog"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # 设置ui属性
