# 设置重命名模板的控件

from PySide6.QtGui import *
from PySide6.QtWidgets import *

from constant import ICON_INFORMATION, RENAME_PATTERN_INFORMATION, ERROR_STYLESHEET
from module import function_config, function_normal, function_rename_pattern
from ui.ui_widget_rename_pattern import Ui_Form


class WidgetRenamePattern(QWidget):
    """设置重命名模板的控件"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # 设置ui属性
        self.ui.toolButton_info.setIcon(QIcon(ICON_INFORMATION))
        self.ui.toolButton_info.setToolTip(RENAME_PATTERN_INFORMATION)
        self.load_setting()

        self.ui.lineEdit_pattern.textChanged.connect(self.change_pattern)

    def load_setting(self):
        """加载设置"""
        self.ui.lineEdit_pattern.setText(function_config.get_setting_rename_pattern())
        self.show_pattern_chs()

    def change_pattern(self):
        pattern = self.ui.lineEdit_pattern.text()
        function_config.set_setting_rename_pattern(pattern)
        self.show_pattern_chs()

    def show_pattern_chs(self):
        self.ui.label_pattern.setText(function_rename_pattern.get_pattern_chs())

    def check_feasible(self):
        """检查规则是否符合Windows文件名规范"""
        pattern = self.ui.lineEdit_pattern.text()
        is_feasible = function_normal.check_filename_feasible(pattern)
        if not is_feasible:
            self.ui.lineEdit_pattern.setStyleSheet(ERROR_STYLESHEET)
        else:
            self.ui.lineEdit_pattern.setStyleSheet()
