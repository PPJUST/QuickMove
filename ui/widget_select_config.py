# 配置文件选择的控件
import random
import string

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from constant import ICON_ADD, ICON_DELETE
from module import function_config
from ui.ui_widget_select_config import Ui_Form


class WidgetSelectConfig(QWidget):
    """配置文件选择的控件"""
    signal_config_changed = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # 设置ui属性
        self.ui.toolButton_add.setIcon(QIcon(ICON_ADD))
        self.ui.toolButton_delete.setIcon(QIcon(ICON_DELETE))
        self.load_setting()

        # 连接信号与槽函数
        self.ui.toolButton_add.clicked.connect(self.add_config)
        self.ui.toolButton_delete.clicked.connect(self.delete_config)
        self.ui.comboBox_config.currentTextChanged.connect(self.choose_config)

    def load_setting(self):
        """加载设置"""
        sections = function_config.get_sections()
        self.ui.comboBox_config.clear()
        self.ui.comboBox_config.addItems(sections)
        self.ui.comboBox_config.setCurrentText(function_config.get_default_section())

    def add_config(self, config_name: str = None):
        """新建配置项
        :param config_name:str，配置名"""
        # 如果没有传入配置名，则弹出对话框
        if not config_name:
            config_name, _ = QInputDialog.getText(self, "新建配置", "配置名:", text="默认")
            if not config_name:
                return

        # 检查是否重复，否则添加随机后缀
        if function_config.is_has_section(config_name):
            random_string = ''.join(random.choices(string.ascii_lowercase, k=6))
            config_name = f"{config_name}_{random_string}"

        self.ui.comboBox_config.addItem(config_name)
        self.ui.comboBox_config.setCurrentText(config_name)

    def delete_config(self):
        """删除配置项"""
        current_section = function_config.get_default_section()
        function_config.delete_section(current_section)
        self.load_setting()

    def choose_config(self):
        """选择配置项"""
        current_config = self.ui.comboBox_config.currentText()
        function_config.set_default_section(current_config)
        self.signal_config_changed.emit()
