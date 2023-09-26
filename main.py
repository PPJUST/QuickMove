import configparser
import ctypes
import os
import random
import shutil
import string
import time
from typing import Union

from PySide2.QtCore import Signal
from PySide2.QtGui import Qt, QIcon
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMainWindow, QFileDialog, QInputDialog, QWidget, QHBoxLayout, QApplication

from DialogRename import DialogRename
from DropLineEdit import DropLineEdit
from general_method import walk_path
from personal_sort import windows_sorted
from ui_main import Ui_MainWindow


class QuickMove(QMainWindow):
    signal_current_changed = Signal()  # 当前文件改变时的信号
    signal_do_move = Signal(str, str, str)  # 在生成的移动组件中点击移动按钮时，发送目标移动文件夹路径、添加前缀、添加后缀

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        """
        初始化
        """
        self.code_start = False  # 状态码，为True时才进行后续操作
        self.ui.text_info.setTextInteractionFlags(Qt.NoTextInteraction)  # 禁止信息显示框被点击
        self.move_dict = dict()  # 移动的文件任务，格式：{1:{'origin_path':path, 'state':'', 'new_path':''}, 2:...}
        self.move_number_total = int()  # 移动文件总数
        self.move_number_current = int()  # 当前移动文件编号，从0开始
        self.create_config_section()
        self.load_config()
        self.check_origin_path()
        self.ui.button_pass.setEnabled(False)
        self.ui.button_undo_pre.setEnabled(False)

        """
        连接信号与槽函数
        """
        # 原始文件相关
        self.ui.button_check_origin_path.clicked.connect(self.initialize_task)
        self.ui.button_ask_origin_path.clicked.connect(self.ask_origin_path)
        self.ui.button_open_origin_path.clicked.connect(lambda: os.startfile(self.ui.lineedit_origin_path.text()))
        self.ui.lineedit_origin_path.textChanged.connect(self.check_origin_path)
        # 配置文件相关
        self.ui.button_add_config.clicked.connect(self.add_config)
        self.ui.button_delete_config.clicked.connect(self.delete_config)
        self.ui.combobox_config.currentTextChanged.connect(self.change_config)
        # 日志文本框
        self.ui.text_info.textChanged.connect(
            lambda: self.ui.text_info.verticalScrollBar().setValue(self.ui.text_info.verticalScrollBar().maximum()))
        # 自定义信号
        self.signal_current_changed.connect(self.current_changed)
        self.signal_do_move.connect(self.do_move)
        # 跳过、撤回、退出
        self.ui.button_pass.clicked.connect(self.pass_current)
        self.ui.button_undo_pre.clicked.connect(self.undo_pre_action)
        self.ui.button_quit.clicked.connect(self.close)

    def change_model(self):
        """修改模式"""
        self.code_start = False

        config, current_config = self.change_setting_return_config()

        if self.ui.radiobutton_model_file.isChecked():
            config.set(current_config, 'model', 'file')
        else:
            config.set(current_config, 'model', 'folder')
        config.write(open('config.ini', 'w', encoding='utf-8'))

    def change_auto_open(self):
        """修改自动打开选项"""
        config, current_config = self.change_setting_return_config()

        if self.ui.checkbox_auto_open.isChecked():
            config.set(current_config, 'auto_open', 'True')
        else:
            config.set(current_config, 'auto_open', 'False')
        config.write(open('config.ini', 'w', encoding='utf-8'))

    def change_manual_rename(self):
        """修改手动改名选项"""
        config, current_config = self.change_setting_return_config()

        if self.ui.checkbox_manual_rename.isChecked():
            config.set(current_config, 'manual_rename', 'True')
        else:
            config.set(current_config, 'manual_rename', 'False')
        config.write(open('config.ini', 'w', encoding='utf-8'))

    def change_add_fix(self):
        """修改通用前后缀"""
        config, current_config = self.change_setting_return_config()

        add_prefix = self.ui.lineedit_add_prefix.text().strip()
        add_suffix = self.ui.lineedit_add_suffix.text().strip()

        config.set(current_config, 'add_prefix_global', add_prefix)
        config.set(current_config, 'add_suffix_global', add_suffix)
        config.write(open('config.ini', 'w', encoding='utf-8'))

    def change_move_folder_number(self):
        """改变目标文件夹数"""
        config, current_config = self.change_setting_return_config()

        folder_number = self.ui.spinbox_folder_number.value()
        self.create_move_widget()  # 更新移动组件数

        config.set(current_config, 'folder_number', str(folder_number))
        config.write(open('config.ini', 'w', encoding='utf-8'))

    def change_origin_folder(self):
        """改变原始文件夹"""
        self.code_start = False

        config, current_config = self.change_setting_return_config()

        origin_folder = self.ui.lineedit_origin_path.text().strip()

        config.set(current_config, 'folder_origin', origin_folder)
        config.write(open('config.ini', 'w', encoding='utf-8'))

    def check_origin_path(self):
        """检查原始文件夹路径的规范"""
        self.code_start = False

        origin_folderpath = self.ui.lineedit_origin_path.text()
        if not os.path.exists(origin_folderpath) or os.path.isfile(origin_folderpath):
            self.ui.button_open_origin_path.setEnabled(False)
            self.ui.button_check_origin_path.setEnabled(False)
            self.ui.lineedit_origin_path.setStyleSheet('border: 1px solid red;')
        else:
            self.ui.button_open_origin_path.setEnabled(True)
            self.ui.button_check_origin_path.setEnabled(True)
            self.ui.lineedit_origin_path.setStyleSheet('')

    def ask_origin_path(self):
        """弹出原始文件夹选框"""
        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹")
        if folder_path:
            self.ui.lineedit_origin_path.setText(folder_path)

    def initialize_task(self):
        """初始化移动任务"""
        self.move_dict = dict()  # 初始化移动列表
        origin_path = self.ui.lineedit_origin_path.text()
        model = 'file' if self.ui.radiobutton_model_file.isChecked() else 'folder'
        walk_list = walk_path(origin_path, model=model)  # 提取文件或文件夹（只有文件名）
        walk_list_fullpath = [os.path.normpath(os.path.join(origin_path, i)) for i in walk_list]
        n = 0
        for path in walk_list_fullpath:
            self.move_dict[n] = {'origin_path': path, 'state': '', 'new_path': ''}
            n += 1

        if self.move_dict:
            self.move_number_total = len(self.move_dict)
            self.code_start = True
            self.move_number_current = 0
            self.ui.label_current.setText(os.path.split(self.move_dict[self.move_number_current]['origin_path'])[1])
            self.signal_current_changed.emit()
            self.ui.button_pass.setEnabled(True)
        else:
            self.ui.label_current.setText('---没有文件---')
            self.ui.label_schedule.setText('-/-')

        self.show_info(info_type='初始化')

    def current_changed(self):
        """在当前文件改变时执行相关操作"""
        if self.move_number_current + 1 > self.move_number_total:
            self.ui.label_schedule.setText(f'-/{self.move_number_total}')
            self.ui.label_current.setText('---没有更多文件---')
        else:
            # 在ui上显示当前移动进度
            self.ui.label_schedule.setText(f'{self.move_number_current + 1}/{self.move_number_total}')
            self.ui.label_current.setText(os.path.split(self.move_dict[self.move_number_current]['origin_path'])[1])
            # 根据选项是否自动打开文件
            code_auto_open = self.ui.checkbox_auto_open.isChecked()
            model = 'file' if self.ui.radiobutton_model_file.isChecked() else 'folder'
            if code_auto_open:
                if model == 'file':
                    os.startfile(self.move_dict[self.move_number_current]['origin_path'])
                elif model == 'folder':
                    self.open_folder_no_hidden(self.move_dict[self.move_number_current]['origin_path'])

        if self.move_number_current <= 0:
            self.ui.button_undo_pre.setEnabled(False)
        else:
            self.ui.button_undo_pre.setEnabled(True)
        if self.move_number_current >= self.move_number_total:
            self.ui.button_pass.setEnabled(False)
        else:
            self.ui.button_pass.setEnabled(True)

    def show_info(self, info_type: str, info_text: Union[str, list] = None):
        """在ui中显示日志
        传参：
        info_type：日志的类型
        info_text：文本，str或list"""
        current_time = time.strftime("%H:%M:%S ", time.localtime())
        text_time = "<font color='green' size='4'>" + current_time + "</font>"
        if info_text:
            text_origin_file = "<font color='blue' size='3'>" + info_text[0] + "</font>"
        else:
            text_origin_file = ""
        if info_type == '初始化':
            self.ui.text_info.clear()
            text_info = "<font color='green' size='4'>" + " 初始化移动任务 " + "</font>"
            self.ui.text_info.insertHtml(text_time + text_info + "<br>")
        if info_type == '未确认启动代码':
            text_info = "<font color='red' size='4'>" + " 已修改设置，请重新初始化 " + "</font>"
            self.ui.text_info.insertHtml(text_time + text_info + "<br>")
        elif info_type == '已完成全部任务':
            text_info = "<font color='green' size='4'>" + " 已完成全部任务 " + "</font>"
            self.ui.text_info.insertHtml(text_time + text_info + "<br>")
        elif info_type == '原文件不存在':
            text_info = "<font color='red' size='4'>" + " 当前文件不存在，请检查或跳过 " + "</font>"
            self.ui.text_info.insertHtml(text_time + text_info + "<br>")
        elif info_type == '移动文件':
            text_info = "<font color='orange' size='4'>" + " --> " + "</font>"
            text_new_file = "<font color='purple' size='3'>" + info_text[1] + "</font>"
            self.ui.text_info.insertHtml(text_time + text_origin_file + text_info + text_new_file + "<br>")
        elif info_type == '跳过文件':
            text_info = "<font color='yellow' size='4'>" + " 已跳过 " + "</font>"
            self.ui.text_info.insertHtml(text_time + text_info + text_origin_file + "<br>")
        elif info_type == '撤销操作-跳过':
            text_info = "<font color='yellow' size='4'>" + " 已撤销跳过 " + "</font>"
            self.ui.text_info.insertHtml(text_time + text_info + text_origin_file + "<br>")
        elif info_type == '撤销操作-移动':
            text_info = "<font color='orange' size='4'>" + " 已撤销移动 " + "</font>"
            self.ui.text_info.insertHtml(text_time + text_info + text_origin_file + "<br>")

    @staticmethod
    def open_folder_no_hidden(folder_path: str):
        """打开传入路径文件夹中的第一个非隐藏文件"""

        def check_hidden(path: str):
            """检查传入路径的隐藏属性"""
            GetFileAttributesW = ctypes.windll.kernel32.GetFileAttributesW
            FILE_ATTRIBUTE_HIDDEN = 0x2
            INVALID_FILE_ATTRIBUTES = -1

            def is_hidden(file):
                # 获取文件属性
                attrs = GetFileAttributesW(file)
                if attrs == INVALID_FILE_ATTRIBUTES:
                    # 文件不存在或无法访问
                    return False

                return attrs & FILE_ATTRIBUTE_HIDDEN == FILE_ATTRIBUTE_HIDDEN

            return is_hidden(path)

        temp_list = []
        files = windows_sorted(folder_path, model='file')
        for i in files:
            if not check_hidden(i):  # 排除隐藏文件
                temp_list.append(i)
        os.startfile(temp_list[0])

    @staticmethod
    def create_config_section(section_name='默认', model_add=False):
        """检查初始配置文件"""
        default_config_top = """
[DEFAULT]
config = 默认
        """
        default_config_mid = f"""
[{section_name}]
model = file
auto_open = True
manual_rename = False
add_prefix_global = 
add_suffix_global = 
folder_origin = 

folder_number = 3
                """
        for i in range(1, 10 + 1):
            default_config_mid += f"""
folder_move_{i}_path = 
folder_move_{i}_prefix =
folder_move_{i}_suffix =
                                    """

        if not os.path.exists('config.ini'):
            with open('config.ini', 'w', encoding='utf-8') as cw:
                cw.write(default_config_top + default_config_mid)

        if model_add:
            with open('config.ini', 'a', encoding='utf-8') as ca:
                ca.write(default_config_mid)

    def add_config(self, new_config: str = None):
        """新建配置文件，可传入新配置名"""
        config, _ = self.change_setting_return_config()

        if not new_config:
            new_config, _ = QInputDialog.getText(self, "新建配置文件", "名称:", text="new config")
        if new_config:
            self.connect_config_signal(model_connect=False)
            if new_config in config:  # 如果有重复，则添加随机后缀
                random_string = ''.join(random.choices(string.ascii_lowercase, k=6))
                new_config = f"{new_config}_{random_string}"

            self.create_config_section(section_name=new_config, model_add=True)

            config, _ = self.change_setting_return_config()
            config.set('DEFAULT', 'config', new_config)
            config.write(open('config.ini', 'w', encoding='utf-8'))

            self.ui.combobox_config.addItem(new_config)
            self.load_config()

    def delete_config(self):
        """删除配置文件"""
        config, current_config = self.change_setting_return_config()
        self.connect_config_signal(model_connect=False)

        current_config_index = config.sections().index(current_config)
        self.ui.combobox_config.removeItem(current_config_index)

        config.remove_section(current_config)
        config.set('DEFAULT', 'config', config.sections()[0])
        if config.sections():  # 如果删除后没有配置文件了，则自动新增一个默认的配置文件
            self.add_config(new_config='new config')
        config.write(open('config.ini', 'w', encoding='utf-8'))

        self.load_config()

    def change_config(self):
        """选择配置文件"""
        self.code_start = False

        config, _ = self.change_setting_return_config()
        self.connect_config_signal(model_connect=False)

        choose_config = self.ui.combobox_config.currentText()
        config.set('DEFAULT', 'config', choose_config)
        config.write(open('config.ini', 'w', encoding='utf-8'))
        self.load_config()

    def load_config(self):
        """加载配置文件"""
        # 读取配置文件
        config, current_config = self.change_setting_return_config()

        current_config = config.get('DEFAULT', 'config')
        model = config.get(current_config, 'model')
        auto_open = config.get(current_config, 'auto_open')
        folder_number = int(config.get(current_config, 'folder_number'))
        folder_origin = config.get(current_config, 'folder_origin')
        manual_rename = config.get(current_config, 'manual_rename')
        add_prefix_global = config.get(current_config, 'add_prefix_global')
        add_suffix_global = config.get(current_config, 'add_suffix_global')

        # 修改配置文件下拉框
        self.ui.combobox_config.clear()
        self.ui.combobox_config.addItems(config.sections())
        self.ui.combobox_config.setCurrentText(current_config)
        # 修改原文件夹
        self.ui.lineedit_origin_path.setText(folder_origin)
        # 修改模式
        if model == 'file':
            self.ui.radiobutton_model_file.setChecked(True)
            self.ui.radiobutton_model_folder.setChecked(False)
        else:
            self.ui.radiobutton_model_file.setChecked(False)
            self.ui.radiobutton_model_folder.setChecked(True)
        # 修改自动打开下一个文件
        if auto_open == "True":
            self.ui.checkbox_auto_open.setChecked(True)
        else:
            self.ui.checkbox_auto_open.setChecked(False)
        # 修改手动改名
        if manual_rename == "True":
            self.ui.checkbox_manual_rename.setChecked(True)
        else:
            self.ui.checkbox_manual_rename.setChecked(False)
        # 修改通用前后缀
        self.ui.lineedit_add_prefix.setText(add_prefix_global)
        self.ui.lineedit_add_suffix.setText(add_suffix_global)
        # 修改计数器
        self.ui.spinbox_folder_number.setValue(folder_number)
        # 生成移动组件
        self.create_move_widget()

        # 重新连接槽函数
        self.connect_config_signal(model_connect=True)

    def create_move_widget(self):
        """生成移动组件"""
        config, current_config = self.change_setting_return_config()

        # 清空原有组件
        main_layout = self.ui.scrollAreaWidgetContents_movefolders.layout()  # 获取布局对象
        while main_layout.count():  # 循环遍历布局中的控件
            child = main_layout.takeAt(0)  # 获取布局中的第一个控件
            child.widget().deleteLater()  # 删除控件

        # 生成移动组件
        widget_number = self.ui.spinbox_folder_number.value()
        for i in range(1, widget_number + 1):
            # 添加组件
            ui_widget_move = QUiLoader().load('ui_widget_move.ui')
            widget_move = QWidget()
            widget_move.setMinimumHeight(60)
            widget_move.setMaximumHeight(60)
            layout_widget_move = QHBoxLayout()
            layout_widget_move.setContentsMargins(0, 0, 0, 0)
            layout_widget_move.addWidget(ui_widget_move)
            widget_move.setLayout(layout_widget_move)
            main_layout.addWidget(widget_move)
            ui_widget_move.setObjectName(f'movewidgets_{i}')  # 设置对象名，方便后续使用sender获取
            # 向用于存放文本框的布局中添加自定义LineEdit（直接导入ui无法自定义控件）
            ui_widget_move.lineEdit_folderpath = DropLineEdit()
            ui_widget_move.layout_place_lineEdit_folderpath.addWidget(ui_widget_move.lineEdit_folderpath)
            # 连接信号与槽函数
            ui_widget_move.button_number.clicked.connect(self.autowidget_move_to_folder)
            ui_widget_move.button_ask.clicked.connect(self.autowidget_ask_move_folder)
            ui_widget_move.button_open.clicked.connect(self.autowidget_open_move_folder)
            ui_widget_move.lineEdit_folderpath.textChanged.connect(self.autowidget_change_move_folder)
            ui_widget_move.lineEdit_add_prefix.textChanged.connect(self.autowidget_change_add_fix)
            ui_widget_move.lineEdit_add_suffix.textChanged.connect(self.autowidget_change_add_fix)
            # 读取配置，并显示在ui上
            path = config.get(current_config, f'folder_move_{i}_path')
            prefix = config.get(current_config, f'folder_move_{i}_prefix')
            suffix = config.get(current_config, f'folder_move_{i}_suffix')
            ui_widget_move.lineEdit_folderpath.setText(path)
            ui_widget_move.lineEdit_add_prefix.setText(prefix)
            ui_widget_move.lineEdit_add_suffix.setText(suffix)
            # 首次检查路径规范
            if not os.path.exists(path) or os.path.isfile(path):
                ui_widget_move.button_number.setEnabled(False)
                ui_widget_move.button_open.setEnabled(False)
                ui_widget_move.lineEdit_folderpath.setStyleSheet('border: 1px solid red;')

    def autowidget_move_to_folder(self):
        sender_widget = self.sender().parentWidget()  # 获取父控件对象

        if self.code_start:
            move_to_path = sender_widget.lineEdit_folderpath.text()
            add_prefix = sender_widget.lineEdit_add_prefix.text()
            add_suffix = sender_widget.lineEdit_add_suffix.text()
            self.signal_do_move.emit(move_to_path, add_prefix, add_suffix)
        else:
            self.signal_do_move.emit(None, None, None)

    def autowidget_ask_move_folder(self):
        sender_widget = self.sender().parentWidget()  # 获取父控件对象

        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹")
        if folder_path:
            sender_widget.lineEdit_folderpath.setText(folder_path)

    def autowidget_open_move_folder(self):
        sender_widget = self.sender().parentWidget()  # 获取父控件对象

        path = sender_widget.lineEdit_folderpath.text()
        os.startfile(path)

    def autowidget_change_move_folder(self):
        sender_widget = self.sender().parentWidget()  # 获取父控件对象
        sender_widget_name = sender_widget.objectName()  # 获取父控件对象名
        movefolder_number = sender_widget_name.split('_')[1]  # 提取编号
        folder_move = self.sender().text()  # 提取控件文本

        # 更新config
        config, current_config = self.change_setting_return_config()

        config.set(current_config, f'folder_move_{movefolder_number}_path', folder_move)
        config.write(open('config.ini', 'w', encoding='utf-8'))

        # 检查路径规范
        if not os.path.exists(folder_move) or os.path.isfile(folder_move):
            sender_widget.button_number.setEnabled(False)
            sender_widget.button_open.setEnabled(False)
            sender_widget.lineEdit_folderpath.setStyleSheet('border: 1px solid red;')
        else:
            sender_widget.button_number.setEnabled(True)
            sender_widget.button_open.setEnabled(True)
            sender_widget.lineEdit_folderpath.setStyleSheet('')

    def autowidget_change_add_fix(self):
        sender_widget = self.sender().parentWidget()  # 获取父控件对象
        sender_widget_name = sender_widget.objectName()  # 获取父控件对象名
        movefolder_number = sender_widget_name.split('_')[1]  # 提取编号
        config, current_config = self.change_setting_return_config()

        add_prefix = sender_widget.lineEdit_add_prefix.text()
        add_suffix = sender_widget.lineEdit_add_suffix.text()
        config.set(current_config, f'folder_move_{movefolder_number}_prefix', add_prefix)
        config.set(current_config, f'folder_move_{movefolder_number}_suffix', add_suffix)
        config.write(open('config.ini', 'w', encoding='utf-8'))

    def change_setting_return_config(self):
        """修改设置时，返回config对象与当前的配置名"""
        self.code_start = False
        config = configparser.ConfigParser()
        config.read("config.ini", encoding='utf-8')
        current_config = config.get('DEFAULT', 'config')

        return config, current_config

    def connect_config_signal(self, model_connect: bool = True):
        """连接或断联与信号相关的槽函数"""
        if model_connect:
            self.ui.lineedit_origin_path.textChanged.connect(self.change_origin_folder)
            self.ui.radiobutton_model_file.toggled.connect(self.change_model)
            self.ui.radiobutton_model_folder.toggled.connect(self.change_model)
            self.ui.checkbox_auto_open.toggled.connect(self.change_auto_open)
            self.ui.checkbox_manual_rename.toggled.connect(self.change_manual_rename)
            self.ui.lineedit_add_prefix.textChanged.connect(self.change_add_fix)
            self.ui.lineedit_add_suffix.textChanged.connect(self.change_add_fix)
            self.ui.spinbox_folder_number.valueChanged.connect(self.change_move_folder_number)
        else:
            self.ui.lineedit_origin_path.textChanged.disconnect(self.change_origin_folder)
            self.ui.radiobutton_model_file.toggled.disconnect(self.change_model)
            self.ui.radiobutton_model_folder.toggled.disconnect(self.change_model)
            self.ui.checkbox_auto_open.toggled.disconnect(self.change_auto_open)
            self.ui.checkbox_manual_rename.toggled.disconnect(self.change_manual_rename)
            self.ui.lineedit_add_prefix.textChanged.disconnect(self.change_add_fix)
            self.ui.lineedit_add_suffix.textChanged.disconnect(self.change_add_fix)
            self.ui.spinbox_folder_number.valueChanged.disconnect(self.change_move_folder_number)

    def do_move(self, move_to_folder: str, add_prefix: str, add_suffix: str):
        """执行移动操作，传入目标文件夹路径str，添加前缀str，添加后缀str"""
        if not self.code_start:  # 检查启动代码
            self.show_info(info_type='未确认启动代码')
            return

        if self.move_number_current + 1 > self.move_number_total:  # 检查是否超限
            self.show_info(info_type='已完成全部任务')
            return

        current_file = self.move_dict[self.move_number_current]['origin_path']

        if not os.path.exists(current_file):
            self.show_info(info_type='原文件不存在')
        else:
            add_prefix_global = self.ui.lineedit_add_prefix.text()
            add_suffix_global = self.ui.lineedit_add_suffix.text()

            if os.path.isfile(current_file):
                old_filename = os.path.split(current_file)[1]
                old_filetitle = os.path.split(os.path.splitext(current_file)[0])[1]
                file_suffix = os.path.splitext(current_file)[1]
            else:
                old_filename = os.path.split(current_file)[1]
                old_filetitle = old_filename
                file_suffix = 'file'

            # 根据前后缀组合目标文件名
            target_filetitle = add_prefix_global + add_prefix + old_filetitle + add_suffix_global + add_suffix
            target_filename = target_filetitle + file_suffix

            # 根据是否执行手动改名，组合新的文件名
            if self.ui.checkbox_manual_rename.isChecked():
                dialog = DialogRename(add_prefix_global + add_prefix, old_filetitle, add_suffix_global + add_suffix,
                                      file_suffix)
                qdialog_add_prefix, qdialog_filetitle, qdialog_add_suffix, qdialog_file_suffix = dialog.return_filename()

                if qdialog_add_prefix:
                    target_filetitle = qdialog_add_prefix + qdialog_filetitle + qdialog_add_suffix
                    target_filename = target_filetitle + qdialog_file_suffix

            # 检查目标文件夹下有无重名
            count = 0
            while os.path.exists(os.path.join(move_to_folder, target_filename)):  # 一直累加循环直到不存在同名
                count += 1
                target_filename = f"{target_filetitle} -new{count}{file_suffix}"
            old_path_with_newname = os.path.normpath(os.path.join(os.path.split(current_file)[0], target_filename))
            if old_filename != target_filename:
                os.rename(current_file, old_path_with_newname)  # 先改名
            shutil.move(old_path_with_newname, move_to_folder)  # 后移动
            new_file = os.path.normpath(os.path.join(move_to_folder, target_filename))

            # 更新日志
            self.show_info(info_type='移动文件', info_text=[current_file, new_file])
            # 更新变量
            self.move_dict[self.move_number_current]['state'] = 'move'
            self.move_dict[self.move_number_current]['new_path'] = new_file
            self.move_number_current += 1
            self.signal_current_changed.emit()

    def pass_current(self):
        """跳过当前文件"""
        self.move_dict[self.move_number_current]['state'] = 'pass'
        current_file = self.move_dict[self.move_number_current]['origin_path']

        self.show_info(info_type='跳过文件', info_text=[current_file])
        self.move_number_current += 1
        self.signal_current_changed.emit()

    def undo_pre_action(self):
        """撤销上一次操作"""
        self.move_number_current -= 1
        current_file = self.move_dict[self.move_number_current]['origin_path']
        pre_action = self.move_dict[self.move_number_current]['state']
        if pre_action == 'pass':  # 如果上一次操作是跳过，则不做其他处理
            self.signal_current_changed.emit()
            self.show_info(info_type='撤销操作-跳过', info_text=[current_file])
        elif pre_action == 'move':  # 如果上一次操作是移动，则移回原文件夹
            new_path = self.move_dict[self.move_number_current]['new_path']
            origin_path = self.move_dict[self.move_number_current]['origin_path']
            shutil.move(new_path, origin_path)
            self.signal_current_changed.emit()
            self.show_info(info_type='撤销操作-移动', info_text=[current_file])


def main():
    app = QApplication()
    app.setStyle('Fusion')
    show_ui = QuickMove()
    show_ui.setWindowIcon(QIcon(r'./res_icon/icon.ico'))
    show_ui.show()
    app.exec_()


if __name__ == "__main__":
    main()