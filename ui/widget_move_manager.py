# 移动功能的整个控件组

from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *

from constant import ICON_SKIP, ICON_CANCEL, ICON_RECYCLE_BIN
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

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 初始化
        self.task_dict = None

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

    def load_setting(self):
        """加载设置"""
        self.ui.spinBox_folder_count.setValue(function_config.get_setting_target_dir_count())
        self.change_folder_count()

    def connect_task_dict(self, task_dict: TaskDict):
        """连接任务清单"""
        self.task_dict = task_dict

    def check_rate(self):
        """检查任务进度，启用或停用部分功能"""
        index = self.task_dict.current_index
        # 超限
        if index == 0:
            self.ui.pushButton_skip.setEnabled(False)
            self.ui.pushButton_delete.setEnabled(False)
        else:
            self.ui.pushButton_skip.setEnabled(True)
            self.ui.pushButton_delete.setEnabled(True)
        # 第一个索引
        if index == 1:
            self.ui.pushButton_cancel.setEnabled(False)
        else:
            self.ui.pushButton_cancel.setEnabled(True)

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
            child = layout.takeAt(0)
            child.widget().deleteLater()

        # 新建
        for i in range(1, self.ui.spinBox_folder_count.value() + 1):
            child_widget = WidgetMoveFolder(i)
            child_widget.signal_click_move_button.connect(self.move_current)
            layout.addWidget(child_widget)

    def move_current(self, target_folder: str):
        """移动当前任务对应的文件"""
        if self.task_dict.current_index == 0:  # 不在超限时进行移动操作
            return
        current_path = self.task_dict.current_path
        new_path = self.task_dict.operation_move(target_folder)
        self.signal_moved.emit(current_path, new_path)

    def skip_current(self):
        """跳过当前任务"""
        current_path = self.task_dict.current_path
        self.task_dict.operation_skip()
        self.signal_skipped.emit(current_path)

    def delete_current(self):
        """删除当前任务对应的文件"""
        current_path = self.task_dict.current_path
        self.task_dict.operation_delete()
        self.signal_deleted.emit(current_path)

    def cancel_last(self):
        """撤回上一个任务"""
        self.task_dict.operation_cancel()
        current_path = self.task_dict.current_path
        self.signal_cancelled.emit(current_path)
