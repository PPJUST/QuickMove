# 显示历史记录的文本框控件
import os
import time

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class TextBrowserHistory(QTextBrowser):
    """显示历史记录的文本框控件"""

    def __init__(self):
        super().__init__()
        self.setTextInteractionFlags(Qt.NoTextInteraction)  # 禁止点击
        self.textChanged.connect(self.on_text_changed)

    def on_text_changed(self):
        """文本变化时滚动到底部"""
        self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())

    def record_initialize(self):
        """记录-初始化"""
        self.insertHtml("-" * 80 + "<br>")
        text_time = self._get_time_text()
        text_info = "<font color='purple' size='4'>" + " 文件夹检查已完成 " + "</font>"
        self.insertHtml(text_time + text_info + "<br>")

    def record_need_init(self):
        """记录-更改设置后需要初始化"""
        text_time = self._get_time_text()
        text_info = "<font color='red' size='4'>" + " 已修改设置，需要重新初始化 " + "</font>"
        self.insertHtml(text_time + text_info + "<br>")

    def record_complete(self):
        """记录-完成全部任务"""
        text_time = self._get_time_text()
        text_info = "<font color='purple' size='4'>" + " 完成所有任务 " + "</font>"
        self.insertHtml(text_time + text_info + "<br>")

    def record_not_exist(self, path):
        """记录-路径不存在"""
        text_time = self._get_time_text()
        text_path = self._get_path_text(path)
        text_info = "<font color='red' size='4'>" + " 文件不存在 " + "</font>"
        self.insertHtml(text_time + text_info + text_path + "<br>")

    def record_file_occupied(self, path):
        """记录-文件被占用"""
        text_time = self._get_time_text()
        text_path = self._get_path_text(path)
        text_info = "<font color='red' size='4'>" + " 文件被占用 " + "</font>"
        self.insertHtml(text_time + text_info + text_path + "<br>")

    def record_move(self, old_path, new_path):
        """记录-移动"""
        text_time = self._get_time_text()
        text_old_path = self._get_path_text(old_path)
        text_new_path = self._get_path_text(new_path)
        text_info = "<font color='green' size='4'>" + " 移动 " + "</font>"
        text_sign = "<font color='blue' size='4'>" + " --> " + "</font>"
        self.insertHtml(text_time + text_info + text_old_path + text_sign + text_new_path + "<br>")

    def record_skip(self, path):
        """记录-跳过"""
        text_time = self._get_time_text()
        text_path = self._get_path_text(path)
        text_info = "<font color='pink' size='4'>" + " 跳过 " + "</font>"
        self.insertHtml(text_time + text_info + text_path + "<br>")

    def record_delete(self, path):
        """记录-删除"""
        text_time = self._get_time_text()
        text_path = self._get_path_text(path)
        text_info = "<font color='red' size='4'>" + " 删除至回收站 " + "</font>"
        self.insertHtml(text_time + text_info + text_path + "<br>")

    def record_cancel(self, path):
        """记录-撤销"""
        text_time = self._get_time_text()
        text_path = self._get_path_text(path)
        text_info = "<font color='orange' size='4'>" + " 撤回操作 " + "</font>"
        self.insertHtml(text_time + text_info + text_path + "<br>")

    @staticmethod
    def _get_time_text():
        """获取时间文本"""
        current_time = time.strftime("%H:%M:%S ", time.localtime())
        text_time = "<font color='green' size='4'>" + current_time + "</font>"
        return text_time

    @staticmethod
    def _get_path_text(path):
        """获取路径文本"""
        filename = os.path.basename(path)
        parent_dirname = os.path.basename(os.path.dirname(path))
        text_path = "<font color='black' size='4'>" + parent_dirname + "/" + filename + "</font>"
        return text_path
