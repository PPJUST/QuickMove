# 显示进度的控件
import os.path

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *

from constant import ICON_OPEN_FOLDER
from module import function_open_file
from ui.ui_widget_rate import Ui_Form


class WidgetRate(QWidget):
    """显示进度的控件"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
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
