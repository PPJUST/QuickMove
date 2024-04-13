# 主程序

from PySide6.QtGui import QIcon, QPalette, QColor
from PySide6.QtWidgets import *

from constant import ICON_MAIN
from module import function_config
from module.class_task_dict import TaskDict
from ui.textbrowser_history import TextBrowserHistory
from ui.ui_main import Ui_MainWindow
from ui.widget_analyse_folder import WidgetAnalyseFolder
from ui.widget_move_manager import WidgetMoveManager
from ui.widget_rate import WidgetRate
from ui.widget_rename_pattern import WidgetRenamePattern
from ui.widget_select_config import WidgetSelectConfig
from ui.widget_settings import WidgetSettings
from ui.window_tip import WindowTip


class Main(QMainWindow):
    """移动功能的整个控件组"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 初始化
        self.task_dict = TaskDict()

        # 添加自定义控件
        self.widget_analyse_path = WidgetAnalyseFolder()
        self.ui.layout_widget_drop.addWidget(self.widget_analyse_path)
        self.widget_analyse_path.signal_analysed.connect(self.analyse_path)
        self.widget_analyse_path.signal_dropped.connect(self.clear_task)

        self.widget_rate = WidgetRate()
        self.ui.layout_rate.addWidget(self.widget_rate)

        self.textbrowser_history = TextBrowserHistory()
        self.ui.layout_history.addWidget(self.textbrowser_history)

        self.widget_select_config = WidgetSelectConfig()
        self.ui.layout_config.addWidget(self.widget_select_config)
        self.widget_select_config.signal_config_changed.connect(self.reload_setting)
        self.widget_select_config.signal_config_changed.connect(self.clear_task)

        self.widget_settings = WidgetSettings()
        self.ui.layout_settings.addWidget(self.widget_settings)
        self.widget_settings.signal_special_setting_changed.connect(self.clear_task)

        self.widget_rename_pattern = WidgetRenamePattern()
        self.ui.layout_rename_pattern.addWidget(self.widget_rename_pattern)

        self.widget_move_manager = WidgetMoveManager()
        self.ui.layout_widget_move.addWidget(self.widget_move_manager)
        self.widget_move_manager.signal_moved.connect(self.current_file_moved)
        self.widget_move_manager.signal_skipped.connect(self.current_file_skipped)
        self.widget_move_manager.signal_deleted.connect(self.current_file_deleted)
        self.widget_move_manager.signal_cancelled.connect(self.last_file_cancelled)
        self.widget_move_manager.signal_completed.connect(self.complete_task)
        self.widget_move_manager.signal_file_not_exist.connect(self.file_not_exist)
        self.widget_move_manager.signal_file_occupied.connect(self.file_occupied)
        self.widget_move_manager.signal_hotkey_state.connect(self.set_hotkey_state)

    def reload_setting(self):
        """切换配置文件后重新加载设置"""
        self.widget_settings.load_setting()
        self.widget_rename_pattern.load_setting()
        self.widget_move_manager.load_setting()
        self.task_dict.set_task([])

    def analyse_path(self, extract_paths: list):
        """分析路径"""
        # 更新任务字典
        self.task_dict.set_task(extract_paths)
        # 停用快捷键
        self.widget_move_manager.set_hotkey_enable(is_enable=False)
        # 更新进度控件组
        self.update_rate()
        # 更新历史记录控件组
        self.textbrowser_history.record_initialize()
        # 弹出提示窗口（需要实例化）
        self.window_tip = WindowTip('完成初始化')
        # 任务字典连接移动控件组
        self.widget_move_manager.connect_task_dict(self.task_dict)

    def clear_task(self):
        """修改部分选项后，清空任务，防止不期望的操作"""
        # 清空任务字典
        self.task_dict.set_task([])
        # 停用快捷键
        self.widget_move_manager.set_hotkey_enable(is_enable=False)
        # 更新进度控件组
        self.update_rate()
        # 更新历史记录控件组
        self.textbrowser_history.record_need_init()
        # 弹出提示窗口（需要实例化）
        self.window_tip = WindowTip('已修改设置，需要重新初始化')

    def update_rate(self):
        """更新进度控件组"""
        self.widget_rate.reset_current_index(self.task_dict.current_index)
        self.widget_rate.reset_total_count(self.task_dict.count)
        self.widget_rate.reset_current_path(self.task_dict.current_path)

    def current_file_moved(self, old_path, new_path):
        """对当前任务执行了移动操作"""
        # 更新进度控件组
        self.update_rate()
        # 更新历史记录控件组
        self.textbrowser_history.record_move(old_path, new_path)
        # 弹出提示窗口（需要实例化）
        self.window_tip = WindowTip('完成移动')

    def current_file_skipped(self, old_path):
        """对当前任务执行了跳过操作"""
        # 更新进度控件组
        self.update_rate()
        # 更新历史记录控件组
        self.textbrowser_history.record_skip(old_path)
        # 弹出提示窗口（需要实例化）
        self.window_tip = WindowTip('跳过文件')

    def current_file_deleted(self, old_path):
        """对当前任务执行了删除操作"""
        # 更新进度控件组
        self.update_rate()
        # 更新历史记录控件组
        self.textbrowser_history.record_delete(old_path)
        # 弹出提示窗口（需要实例化）
        self.window_tip = WindowTip('删除文件')

    def last_file_cancelled(self, old_path):
        """对上一个任务执行了撤销操作"""
        # 更新进度控件组
        self.update_rate()
        # 更新历史记录控件组
        self.textbrowser_history.record_cancel(old_path)
        # 弹出提示窗口（需要实例化）
        self.window_tip = WindowTip('撤销操作')

    def complete_task(self):
        """完成任务清单"""
        # 更新进度控件组
        self.update_rate()
        # 更新历史记录控件组
        self.textbrowser_history.record_complete()
        # 弹出提示窗口（需要实例化）
        self.window_tip = WindowTip('完成全部任务')

    def file_not_exist(self, path):
        """当前处理的路径不存在"""
        # 更新进度控件组
        self.update_rate()
        # 更新历史记录控件组
        self.textbrowser_history.record_not_exist(path)
        # 弹出提示窗口（需要实例化）
        self.window_tip = WindowTip('当前文件不存在')

    def file_occupied(self, path):
        """当前处理的文件被占用导致无法操作"""
        self.textbrowser_history.record_file_occupied(path)
        # 弹出提示窗口（需要实例化）
        self.window_tip = WindowTip('当前文件被占用')

    def set_hotkey_state(self, is_enable):
        """是否启用其他控件的快捷键"""
        if is_enable:
            self.widget_rate.enable_hotkey()
        else:
            self.widget_rate.disable_hotkey()


if __name__ == '__main__':
    function_config.check_default_config()

    app = QApplication()
    app.setStyle('Fusion')  # 设置风格
    # 设置白色背景色
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(255, 255, 255))
    app.setPalette(palette)
    app.setWindowIcon(QIcon(ICON_MAIN))
    show_ui = Main()
    show_ui.show()
    app.exec()
