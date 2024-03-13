# 拖入路径的文本框控件
import os

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from constant import ERROR_STYLESHEET


class LineEditDropPath(QLineEdit):
    """拖入路径的文本框控件"""
    signal_dropped = Signal(str)
    signal_is_exist = Signal(bool)

    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setReadOnly(True)
        self.setPlaceholderText('拖入文件到此处...')

        # 设置一个QTime定时更新检查路径有效性
        self.qtimer_check_path = QTimer()
        self.qtimer_check_path.timeout.connect(self.check_path)
        self.qtimer_check_path.setInterval(1000)
        self.qtimer_check_path.start()

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        urls = event.mimeData().urls()
        if urls:
            path = urls[0].toLocalFile()
            self.reset_path(path)

    def reset_path(self, path: str):
        """设置文本框的文本"""
        if os.path.isdir(path):
            dirpath = path
        else:
            dirpath = os.path.dirname(path)

        # reverse_dirpath = function_normal.reverse_path(dirpath)  # 反转后的文件路径
        self.setText(dirpath)
        self.setToolTip(dirpath)
        self.signal_dropped.emit(dirpath)

    def check_path(self):
        """检查路径规范"""
        path = self.text()
        if path:
            self.signal_is_exist.emit(os.path.exists(path))
            if os.path.exists(path):
                self.setStyleSheet('')
            else:
                self.setStyleSheet(ERROR_STYLESHEET)
        else:
            self.signal_is_exist.emit(False)
