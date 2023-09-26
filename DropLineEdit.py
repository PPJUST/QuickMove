import os

from PySide2.QtGui import QDragEnterEvent, QDropEvent
from PySide2.QtWidgets import QLineEdit


class DropLineEdit(QLineEdit):
    """Qt的QLineEdit类复写，拖入文件后将控件文本设置为拖入文件所属的文件夹路径/拖入文件夹的路径"""

    def __init__(self, parent=None):
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
                self.setText(path)
            elif os.path.isfile(path):
                self.setText(os.path.split(path)[0])
                # self.setText(path)