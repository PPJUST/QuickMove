import os

from PySide2.QtCore import Signal
from PySide2.QtGui import QDragEnterEvent, QDropEvent
from PySide2.QtWidgets import QLineEdit


class DropLineEdit(QLineEdit):
    """自定义QLineEdit控件
    拖入【文件夹】/【文件】到QLineEdit中，将QLineEdit的文本设置为【拖入的文件夹路径】或【拖入的文件所属的文件夹路径】
    并发送信号 signal_lineEdit_dropped(str)
    注意：仅支持单个文件夹路径"""

    signal_lineEdit_dropped = Signal(str)  # 发送获取的文件夹路径str信号

    def __init__(self,parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)  # 设置可拖入

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        urls = event.mimeData().urls()
        if urls:
            path = urls[0].toLocalFile()  # 获取路径
            if os.path.isdir(path):
                folder_path = path
            else:
                folder_path = os.path.split(path)[0]

            self.setText(folder_path)
            self.signal_lineEdit_dropped.emit(folder_path)