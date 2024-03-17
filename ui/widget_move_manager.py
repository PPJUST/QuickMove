# 移动功能的整个控件组
import os

from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *

from constant import ICON_SKIP, ICON_CANCEL, ICON_RECYCLE_BIN, ICON_ENABLE, ICON_DISABLE
from module import function_config
from module.class_task_dict import TaskDict
from ui.ui_widget_move_manager import Ui_Form
from ui.widget_move_folder import WidgetMoveFolder


class WidgetMoveManager(QWidget):
    """移动功能的整个控件组"""
    signal_moved = Signal(str, str)
    signal_skipped = Signal(str)
    signal_deleted = Signal(str)
    signal_cancelled = Signal(str)
    signal_file_not_exist = Signal(str)
    signal_completed = Signal()
    signal_file_occupied = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 初始化
        self.task_dict = None  # 任务清单
        # 快捷键设置（默认禁用）
        self.is_hotkey_enable = False
        self.ui.pushButton_enable_hotkey.setIcon(QIcon(ICON_DISABLE))
        self.ui.pushButton_enable_hotkey.setText('快捷键已禁用')

        # 设置ui属性
        self.ui.pushButton_skip.setIcon(QIcon(ICON_SKIP))
        self.ui.pushButton_cancel.setIcon(QIcon(ICON_CANCEL))
        self.ui.pushButton_delete.setIcon(QIcon(ICON_RECYCLE_BIN))
        self.load_setting()
        self.add_child_widget_move()

        # 连接信号与槽函数
        self.ui.spinBox_folder_count.valueChanged.connect(self.change_folder_count)
        self.ui.pushButton_skip.clicked.connect(self.skip_current)
        self.ui.pushButton_cancel.clicked.connect(self.cancel_last)
        self.ui.pushButton_delete.clicked.connect(self.delete_current)
        self.ui.pushButton_enable_hotkey.clicked.connect(self.set_hotkey_enable)

    def load_setting(self):
        """加载设置"""
        self.ui.spinBox_folder_count.setValue(function_config.get_setting_target_dir_count())
        self.change_folder_count()

    def connect_task_dict(self, task_dict: TaskDict):
        """连接任务清单"""
        self.task_dict = task_dict
        self.check_rate()

    def check_rate(self):
        """检查任务进度，启用或停用部分功能"""
        index = self.task_dict.current_index
        # 禁用全部按钮，按需启用
        self.ui.pushButton_skip.setEnabled(False)
        self.ui.pushButton_delete.setEnabled(False)
        self.ui.pushButton_cancel.setEnabled(False)
        # 超限
        if index == 0:
            self.signal_completed.emit()  # 发送全部完成信号
            self.ui.pushButton_cancel.setEnabled(True)
        # 未超限时
        if index != 0:
            self.ui.pushButton_skip.setEnabled(True)
            self.ui.pushButton_delete.setEnabled(True)
            # 在第一个索引时
            if index != 1:
                self.ui.pushButton_cancel.setEnabled(True)
        # 无任务时
        if not self.task_dict:
            self.ui.pushButton_skip.setEnabled(False)
            self.ui.pushButton_delete.setEnabled(False)
            self.ui.pushButton_cancel.setEnabled(False)

    def change_folder_count(self):
        """修改目标文件夹数量"""
        count = self.ui.spinBox_folder_count.value()
        function_config.set_setting_target_dir_count(count)

        self.add_child_widget_move()

    def add_child_widget_move(self):
        """添加移动子控件"""
        # 清空
        layout = self.ui.widget_move_folders.layout()
        while layout.count():
            # item_d = layout.itemAt(0)
            # del item_d

            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        # 新建
        for i in range(1, self.ui.spinBox_folder_count.value() + 1):
            child_widget = WidgetMoveFolder(i)
            child_widget.signal_click_move_button.connect(self.move_current)
            layout.addWidget(child_widget)

    def move_current(self, target_folder: str):
        """移动当前任务对应的文件"""
        if not self.task_dict:
            return
        if self.task_dict.current_index == 0:  # 不在超限时进行移动操作
            return
        current_path = self.task_dict.current_path
        if current_path and os.path.exists(current_path):
            new_path = self.task_dict.operation_move(target_folder)
            if new_path:
                self.signal_moved.emit(current_path, new_path)
            else:  # 文件被占用
                self.signal_file_occupied.emit(current_path)

        else:
            self.task_dict.operation_skip()
            self.signal_file_not_exist.emit(current_path)

        self.check_rate()

    def skip_current(self):
        """跳过当前任务"""
        current_path = self.task_dict.current_path
        if current_path and os.path.exists(current_path):
            self.task_dict.operation_skip()
            self.signal_skipped.emit(current_path)
        else:
            self.task_dict.operation_skip()
            self.signal_file_not_exist.emit(current_path)

        self.check_rate()

    def delete_current(self):
        """删除当前任务对应的文件"""
        current_path = self.task_dict.current_path
        if current_path and os.path.exists(current_path):
            is_succeed = self.task_dict.operation_delete()
            if is_succeed:
                self.signal_deleted.emit(current_path)
            else:
                self.signal_file_occupied.emit(current_path)
        else:
            self.task_dict.operation_skip()
            self.signal_file_not_exist.emit(current_path)

        self.check_rate()

    def cancel_last(self):
        """撤回上一个任务"""
        self.task_dict.operation_cancel()
        current_path = self.task_dict.current_path
        self.signal_cancelled.emit(current_path)

        if not current_path or not os.path.exists(current_path):
            self.signal_file_not_exist.emit(current_path)

        self.check_rate()

    def set_hotkey_enable(self):
        """启用或禁用快捷键"""
        self.is_hotkey_enable = not self.is_hotkey_enable  # 修改状态
        if self.is_hotkey_enable:  # 启用快捷键
            self.ui.pushButton_enable_hotkey.setIcon(QIcon(ICON_ENABLE))
            self.ui.pushButton_enable_hotkey.setText('快捷键已启用')
            self.enable_hotkeys()
        else:  # 禁用快捷键
            self.ui.pushButton_enable_hotkey.setIcon(QIcon(ICON_DISABLE))
            self.ui.pushButton_enable_hotkey.setText('快捷键已禁用')
            self.disable_hotkeys()

    def enable_hotkeys(self):
        """启用快捷键"""
        layout = self.ui.widget_move_folders.layout()
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item:
                widget = item.widget()
                if widget:
                    widget.enable_hotkey()

    def disable_hotkeys(self):
        """禁用快捷键"""
        layout = self.ui.widget_move_folders.layout()
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item:
                widget = item.widget()
                if widget:
                    widget.disable_hotkey()
