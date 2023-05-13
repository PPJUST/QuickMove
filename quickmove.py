import os
from PySide2.QtWidgets import QApplication, QPushButton, QHBoxLayout, QLineEdit, QToolButton, QFileDialog, QInputDialog
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QObject, Qt
from PySide2.QtGui import QDragEnterEvent, QDropEvent
import datetime
import sys
import shutil
import configparser
import random
from windows_sorted import windows_sorted
import natsort
import locale
import re


# 自定义MyLineEdit类，继承自QLineEdit
class MyLineEdit(QLineEdit):
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


class Quickmove(QObject):
    def __init__(self):
        super(Quickmove, self).__init__()
        self.ui = QUiLoader().load("ui.ui")

        # 初始化
        # self.ui.setFixedSize(576, 482)  # 设置窗口大小，用于固定大小
        self.start_code = False  # 开始码，True则执行后续操作

        # 替换line edit为MyLineEdit
        self.ui.my_line_edit_path_old = MyLineEdit()  # 新建控件
        self.ui.my_line_edit_path_old.setObjectName('my_line_edit_path_old')
        self.ui.horizontalLayout.removeWidget(self.ui.line_edit_path_old)  # 删除原控件
        self.ui.line_edit_path_old.deleteLater()  # 清空内存
        self.ui.horizontalLayout.insertWidget(1, self.ui.my_line_edit_path_old)  # 插入新控件

        self.config_load()
        for i in config.sections():  # 初始设置一次配置文件下拉框
            self.ui.combobox_select_config.addItem(i)
        self.ui.combobox_select_config.setCurrentText(config.get('DEFAULT', 'show_config'))

        # 信号与槽函数连接
        self.ui.button_create_new_config.clicked.connect(self.config_create)
        self.ui.button_ask_path_old.clicked.connect(self.ask_path_old)
        self.ui.button_makesure.clicked.connect(self.makesure)
        self.ui.button_quit.clicked.connect(lambda: sys.exit(1))
        self.ui.button_open_old.clicked.connect(self.open_old)
        self.ui.text_info.textChanged.connect(self.scroll)
        self.ui.combobox_select_config.currentIndexChanged.connect(self.select_config)
        self.ui.button_selete_config.clicked.connect(self.config_delete)
        self.ui.spinbox_move_folder_number.valueChanged.connect(self.change_move_folder_number)
        self.ui.radio_button_file.clicked.connect(self.check_model)
        self.ui.radio_button_folder.clicked.connect(self.check_model)
        self.ui.check_box_open_next.clicked.connect(self.check_auto_open)
        self.ui.button_cancel_remove.clicked.connect(self.cancel_remove)
        self.ui.my_line_edit_path_old.textChanged.connect(self.auto_old_path_input_save)
        self.ui.button_pass.clicked.connect(lambda: self.pass_this_time())

    def resizeEvent(self, event):  # 重设方法
        self.setFixedSize(event.oldSize())  # 禁止改变窗口大小

    def config_load(self):
        """读取配置文件"""
        global config, show_config, model, auto_open, folder_number, folder_old
        config = configparser.ConfigParser()
        config.read("config.ini", encoding='utf-8')
        show_config = config.get('DEFAULT', 'show_config')
        model = config.get(show_config, 'model')
        auto_open = config.get(show_config, 'auto_open')
        folder_number = int(config.get(show_config, 'folder_number'))
        folder_old = config.get(show_config, 'folder_old')
        self.config_show_ui()

    def config_create(self):
        """新建配置文件，并重新读取"""
        self.start_code = False  # 重置开始码
        new_config = self.input_config_name()
        if new_config in config:
            self.ui.text_info.insertHtml("<font color='red' size='3'>" + "<br>" + "配置文件名重复" + "</font>")
        else:
            config.add_section(new_config)
            config.set(new_config, 'model', 'file')
            config.set(new_config, 'auto_open', 'True')
            config.set(new_config, 'folder_number', '1')
            config.set(new_config, 'folder_old', '')
            for i in range(1, 11):
                config.set(new_config, f'folder_new_{i}', '')
            config.set('DEFAULT', 'show_config', new_config)
            config.write(open('config.ini', 'w',  encoding='utf-8'))
            self.ui.combobox_select_config.addItem(new_config)
            self.config_load()

    def input_config_name(self):
        """输入配置文件名称"""
        name, ok = QInputDialog.getText(self.ui, "配置文件", "输入配置名称:", text="new config")
        if name == "":
            return self.input_config_name()
        else:
            return name

    def config_delete(self):
        """删除配置文件"""
        self.start_code = False
        if len(config.sections()) == 1:
            self.ui.text_info.insertHtml("<font color='red' size='3'>" + "<br>" + "请勿删除最后一个配置文件" + "</font>")
        else:
            del_num = config.sections().index(config.get('DEFAULT', 'show_config'))
            config.remove_section(config.get('DEFAULT', 'show_config'))
            config.set('DEFAULT', 'show_config', config.sections()[0])
            config.write(open('config.ini', 'w', encoding='utf-8'))
            self.ui.combobox_select_config.removeItem(del_num)
            self.config_load()

    def config_show_ui(self):
        """将读取的配置文件显示在界面上"""
        # 修改配置文件下拉框
        self.ui.combobox_select_config.setCurrentText(config.get('DEFAULT', 'show_config'))
        # 修改原文件夹
        self.ui.my_line_edit_path_old.setText(folder_old)
        # 修改模式
        if model == 'file':
            self.ui.radio_button_file.setChecked(True)
            self.ui.radio_button_folder.setChecked(False)
        else:
            self.ui.radio_button_file.setChecked(False)
            self.ui.radio_button_folder.setChecked(True)
        # 修改自动打开下一个文件
        if auto_open == "True":
            self.ui.check_box_open_next.setChecked(True)
        else:
            self.ui.check_box_open_next.setChecked(False)
        # 修改控件数量
        self.ui.spinbox_move_folder_number.setValue(folder_number)
        # 运行自动生成控件
        self.auto_create_button()
        # 设置文件显示框字体颜色
        self.ui.label_show_file.setStyleSheet("color: blue")
        # 禁止信息显示框被点击
        self.ui.text_info.setTextInteractionFlags(Qt.NoTextInteraction)

    def clearlayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            elif child.layout():
                self.clearlayout(child.layout())

    def clear_layout_add_button(self):
        """清空自动添加按钮的布局"""
        layout = self.ui.layout_add_move_button  # 获取需要清空的布局对象
        while layout.count():  # 循环遍历布局中的所有控件
            child = layout.takeAt(0)  # 获取布局中的第一个控件
            if child.widget():  # 判断控件是否存在
                child.widget().deleteLater()  # 删除控件
            elif child.layout():  # 判断子布局是否存在
                self.clearlayout(child.layout())  # 递归清除子布局中的控件

    def auto_create_button(self):
        """自动创建按钮"""
        self.clear_layout_add_button()  # 先清空布局
        for i in range(folder_number):
            i = i + 1
            self.ui.name_layout_group = QHBoxLayout()  # 创建水平布局
            self.ui.layout_add_move_button.addLayout(self.ui.name_layout_group)  # 将水平布局添加到原始布局中
            # 相同操作创建每一次按钮
            self.ui.move_button = QPushButton()  # 创建一个按钮
            self.ui.move_button.setText(str(i))  # 按钮设置文本
            # self.ui.move_button.setStyleSheet('background-color: pink')
            self.ui.move_button.setObjectName(f'button_move_{i}')  # 按钮设置控件名
            self.ui.move_button.setFixedSize(40, 40)  # 设置按钮大小
            self.ui.name_layout_group.addWidget(self.ui.move_button)  # 将按钮添加到布局中
            self.ui.move_button.clicked.connect(self.auto_move_button)  # 所有的按钮都会链接到一个槽函数，可以在槽函数中判断每个按钮独立的属性来进行不同的操作

            self.ui.move_line_edit = MyLineEdit()  # 创建一个文本框
            self.ui.move_line_edit.setObjectName(f'line_edit_move_{i}')  # 按钮设置控件名
            self.ui.move_line_edit.setText(config.get(show_config, f'folder_new_{i}'))  # 设置文本
            self.ui.name_layout_group.addWidget(self.ui.move_line_edit)  # 将按钮添加到布局中
            self.ui.move_line_edit.textChanged.connect(self.auto_new_path_input_save)

            self.ui.move_ask_button = QToolButton()   # 创建一个按钮
            self.ui.move_ask_button.setText('...')  # 按钮设置文本
            self.ui.move_ask_button.setObjectName(f'button_move_ask_{i}')  # 按钮设置控件名
            self.ui.name_layout_group.addWidget(self.ui.move_ask_button)  # 将按钮添加到布局中
            self.ui.move_ask_button.clicked.connect(self.auto_move_ask_button)  # 所有的按钮都会链接到一个槽函数，可以在槽函数中判断每个按钮独立的属性来进行不同的操作

            self.ui.move_open_button = QPushButton()  # 创建一个按钮
            self.ui.move_open_button.setText('打开')  # 按钮设置文本
            self.ui.move_open_button.setObjectName(f'button_move_open_{i}')  # 按钮设置控件名
            # self.ui.move_open_button.setFixedSize(40, 25)  # 设置按钮大小
            self.ui.name_layout_group.addWidget(self.ui.move_open_button)  # 将按钮添加到布局中
            self.ui.move_open_button.clicked.connect(self.auto_move_open_button)  # 所有的按钮都会链接到一个槽函数，可以在槽函数中判断每个按钮独立的属性来进行不同的操作

    def auto_move_button(self):
        """移动按钮"""
        if self.start_code:  # 如果开始码为True则执行
            try:
                move_folder_number = self.sender().objectName().split('_')[-1]
                if os.path.exists(config.get(show_config, f'folder_new_{move_folder_number}')):  # 判断要移动的路径是否存在
                    self.start_move(move_folder_number)
                else:
                    self.ui.text_info.insertHtml("<font color='red' size='3'>" + "<br>" + "对应目录不存在" + "</font>")
            except NameError:
                self.ui.text_info.insertHtml("<font color='red' size='3'>" + "<br>" + "未确认原文件夹" + "</font>")
        else:
            self.ui.text_info.insertHtml("<font color='red' size='3'>" + "<br>" + "设置已重置，请重新确认原文件夹" + "</font>")

    def start_move(self, move_folder_number):
        """移动文件夹操作，需要一个目标文件夹路径的变量"""
        file_number_max = len(need_moves)  # 确认需要移动的总文件数量
        if self.file_number + 1 > file_number_max:  # 确认移动到第几个文件了，是否超限了
            self.ui.text_info.insertHtml("<font color='red' size='3'>" + "<br>" + "已完成全部文件的移动" + "</font>")
        else:
            if os.path.exists(need_moves[self.file_number]):
                move_to_folder = config.get(show_config, f'folder_new_{move_folder_number}')
                move_files = os.listdir(move_to_folder)  # 检查目标文件夹下的文件，是否和要移动的文件重复
                move_files = [x.upper() for x in move_files]  # 转大写，统一格式用于查重
                if os.path.split(need_moves[self.file_number])[1].upper() in move_files:
                    old_filepath = need_moves[self.file_number]
                    new_name = self.rename_recursion(old_filepath, move_to_folder)
                    new_full_name = os.path.split(need_moves[self.file_number])[0] + '/' + new_name
                    os.renames(need_moves[self.file_number], new_full_name)
                    shutil.move(new_full_name, config.get(show_config, f'folder_new_{move_folder_number}'))
                    self.file_number_with_new_full_path[self.file_number] = config.get(show_config, f'folder_new_{move_folder_number}') + '/' + new_name  # 将编号与新路径+新文件名对应，用于撤销操作
                else:
                    shutil.move(need_moves[self.file_number], config.get(show_config, f'folder_new_{move_folder_number}'))
                    self.file_number_with_new_full_path[self.file_number] = config.get(show_config, f'folder_new_{move_folder_number}') + '/' + os.path.split(need_moves[self.file_number])[1]  # 将编号与新路径+新文件名对应，用于撤销操作
                self.file_number += 1
                self.ui.text_info.insertHtml(
                    "<br>" + "<font color='purple' size='3'>" + self.get_time() + "</font>" + " 完成文件移动：" + "<font color='green' size='3'>" +
                    os.path.split(need_moves[self.file_number - 1])[
                        1] + "</font>" + " >>> " + "<font color='orange' size='3'>" + config.get(show_config,
                                                                                                 f'folder_new_{move_folder_number}') + "</font>")
            else:
                self.ui.text_info.insertHtml(
                    "<font color='red' size='3'>" + "<br>" + "当前文件不存在，已跳过" + "</font>")
                self.file_number += 1
            try:
                self.ui.label_show_file.setText(os.path.split(need_moves[self.file_number])[1])
                self.show_where_is_now()
            except IndexError:  # 超限说明已经移动完全部文件
                self.ui.label_show_file.setText('已完成全部文件的移动')
                self.show_where_is_now()

        # 是否自动打开下一个文件
        if auto_open == "True":  # 检查勾选框状态
            if model == 'file':
                os.startfile(need_moves[self.file_number])
            elif model == 'folder':
                # temp_path = need_moves[self.file_number]
                # os.startfile(temp_path + "/" + windows_sorted(temp_path, 'file')[0])  # 如果是文件夹则打开文件夹里面的第一个文件
                self.auto_open_next_folder_no_hidden(need_moves[self.file_number])

    @staticmethod
    def rename_recursion(filepath, the_folder):
        """递归改名，确保无同名文件"""
        filename_without_suffix = os.path.split(os.path.splitext(filepath)[0])[1]
        suffix = os.path.splitext(filepath)[1]
        count = 1
        all_filename = os.listdir(the_folder) + os.listdir(os.path.split(filepath)[0])
        all_filename = [x.upper() for x in all_filename]  # 转大写，防止大小写匹配不到
        while True:
            new_filename = f"{filename_without_suffix} - new{count}{suffix}"
            if new_filename.upper() not in all_filename:
                return new_filename
            else:
                count += 1

    def pass_this_time(self):
        """跳过本次文件"""
        if self.start_code:
            if self.file_number < len(need_moves):  # 防止跳过后超限
                try:
                    self.file_number += 1
                    self.ui.label_show_file.setText(os.path.split(need_moves[self.file_number])[1])
                    self.show_where_is_now()
                    if auto_open == "True":  # 检查勾选框状态
                        if model == 'file':
                            os.startfile(need_moves[self.file_number])
                        elif model == 'folder':
                            # temp_path = need_moves[self.file_number]
                            # os.startfile(temp_path + "/" + windows_sorted(temp_path, 'file')[0])  # 如果是文件夹则打开文件夹里面的第一个文件
                            self.auto_open_next_folder_no_hidden(need_moves[self.file_number])
                except IndexError:
                    self.ui.label_show_file.setText('已完成全部文件的移动')
            else:
                self.ui.text_info.insertHtml("<font color='red' size='3'>" + "<br>" + "没有可跳过的文件" + "</font>")
        else:
            self.ui.text_info.insertHtml("<font color='red' size='3'>" + "<br>" + "设置已重置，请重新确认原文件夹" + "</font>")

    def cancel_remove(self):
        """撤销移动"""
        self.config_load()  # 先读取一遍设置，防止出错
        if self.start_code:
            try:
                if self.file_number > 0:  # 判断移动几个文件了，防止超出限制
                    self.file_number -= 1
                    if os.path.split(self.file_number_with_new_full_path[self.file_number])[1] != os.path.split(need_moves[self.file_number])[1]:  # 如果两边提取的文件名不同，则说明有过改名操作
                        shutil.move(self.file_number_with_new_full_path[self.file_number], folder_old)  # 先移回去再改名
                        os.renames(folder_old + '/' + os.path.split(self.file_number_with_new_full_path[self.file_number])[1], need_moves[self.file_number])
                    else:
                        shutil.move(self.file_number_with_new_full_path[self.file_number], folder_old)
                    self.ui.text_info.insertHtml(
                        "<br>" + "<font color='purple' size='3'>" + self.get_time() + "</font>" + "<font color='blue' size='3'>" + " 撤销移动：" + "</font>" + "<font color='green' size='3'>" +
                        os.path.split(self.file_number_with_new_full_path[self.file_number])[1] + "</font>")
                    self.file_number_with_new_full_path.pop(self.file_number)
                    if auto_open == "True":  # 检查勾选框状态
                        if model == 'file':
                            os.startfile(need_moves[self.file_number])
                        elif model == 'folder':
                            # temp_path = need_moves[self.file_number]
                            # os.startfile(temp_path + "/" + windows_sorted(temp_path, 'file')[0])  # 如果是文件夹则打开文件夹里面的第一个文件
                            self.auto_open_next_folder_no_hidden(need_moves[self.file_number])
                else:
                    self.ui.text_info.insertHtml("<font color='red' size='3'>" + "<br>" + "没有可以撤销移动的文件/文件夹" + "</font>")
            except KeyError:
                self.ui.text_info.insertHtml("<font color='pink' size='3'>" + "<br>" + "已撤回跳过操作" + "</font>")
                if auto_open == "True":  # 检查勾选框状态
                    if model == 'file':
                        os.startfile(need_moves[self.file_number])
                    elif model == 'folder':
                        # temp_path = need_moves[self.file_number]
                        # os.startfile(temp_path + "/" + windows_sorted(temp_path, 'file')[0])  # 如果是文件夹则打开文件夹里面的第一个文件
                        self.auto_open_next_folder_no_hidden(need_moves[self.file_number])

            self.ui.label_show_file.setText(os.path.split(need_moves[self.file_number])[1])  # 显示撤回的文件
            self.show_where_is_now()
        else:
            self.ui.text_info.insertHtml("<font color='red' size='3'>" + "<br>" + "设置已重置，请重新确认原文件夹" + "</font>")

    def auto_new_path_input_save(self):
        """手工输入文件路径后自动更新配置文件"""
        move_folder_number = self.sender().objectName().split('_')[-1]
        new_path = self.sender().text()
        config.set(show_config, f'folder_new_{move_folder_number}', new_path)
        config.write(open('config.ini', 'w', encoding='utf-8'))

    def auto_old_path_input_save(self):
        """手工输入文件路径后自动更新配置文件"""
        self.start_code = False
        old_path = self.ui.my_line_edit_path_old.text()
        config.set(show_config, 'folder_old', old_path)
        config.write(open('config.ini', 'w', encoding='utf-8'))

    def auto_move_ask_button(self):
        """选择新文件路径按钮"""
        move_number = self.sender().objectName().split('_')[-1]
        config.set(show_config, 'folder_new_' + str(move_number), self.ask_path())
        config.write(open('config.ini', 'w', encoding='utf-8'))
        self.config_load()

    def auto_move_open_button(self):
        """打开新路径"""
        move_number = self.sender().objectName().split('_')[-1]
        try:
            os.startfile(config.get(show_config, f'folder_new_{move_number}'))
        except FileNotFoundError:
            self.ui.text_info.insertHtml("<font color='red' size='3'>" + "<br>" + "对应目录不存在" + "</font>")

    def ask_path(self):
        """选取文件夹路径"""
        path = QFileDialog.getExistingDirectory(self.ui, "选择文件夹")
        return path

    def ask_path_old(self):
        """选择原文件夹按钮"""
        config.set(show_config, 'folder_old', self.ask_path())
        config.write(open('config.ini', 'w', encoding='utf-8'))
        self.config_load()

    def makesure(self):
        try:
            self.makesure_main()
            self.start_code = True
        except FileNotFoundError:
            self.ui.text_info.insertHtml("<font color='red' size='3'>" + "<br>" + "测试2对应目录不存在" + "</font>")

    def makesure_main(self):
        """确认路径，遍历文件"""
        # 设置一些要用的变量的初始值
        self.file_number = 0  # 文件顺序编号，用于定位
        self.files = []  # 存放识别到的文件
        self.folders = []  # 存放识别到的文件夹
        self.file_number_with_new_full_path = dict()  # 存放空字典，用于存放新文件夹有重复后改名的文件信息

        travel_path = config.get(show_config, "folder_old")  # 遍历后的文件路径
        files_name = windows_sorted(travel_path, 'file')
        for i in files_name:
            self.files.append(os.path.join(travel_path, i))
        no_hidden_list = []
        for i in self.files:
            if not self.check_hidden(i):  # 排除隐藏文件
                no_hidden_list.append(i)
        self.files = no_hidden_list

        folders_name = windows_sorted(travel_path, 'folder')
        for i in folders_name:
            self.folders.append(os.path.join(travel_path, i))
        no_hidden_list = []
        for i in self.folders:
            if not self.check_hidden(i):  # 排除隐藏文件
                no_hidden_list.append(i)
        self.folders = no_hidden_list

        global need_moves
        # 确认要移动的文件类型
        if model == "file":
            need_moves = self.files
        else:
            need_moves = self.folders
        # 先显示第一个文件
        try:
            self.ui.label_show_file.setText(os.path.split(need_moves[0])[1])
            self.show_where_is_now()
        except IndexError:
            self.ui.text_info.insertHtml("<font color='red' size='3'>" + "<br>" + "当前路径没有文件/文件夹" + "</font>")

        # 如果选中自动打开下一个文件则直接打开第一个文件
        if auto_open == "True":  # 检查勾选框状态
            if model == 'file':
                os.startfile(need_moves[0])
            elif model == 'folder':
                # temp_path = need_moves[0]
                # os.startfile(temp_path + "/" + windows_sorted(temp_path, 'file')[0])  # 如果是文件夹则打开文件夹里面的第一个文件
                self.auto_open_next_folder_no_hidden(need_moves[0])

    @staticmethod
    def check_hidden(file_path):
        """检查文件是否隐藏"""
        import ctypes

        # 定义WinAPI函数
        GetFileAttributesW = ctypes.windll.kernel32.GetFileAttributesW

        # 定义常量
        FILE_ATTRIBUTE_HIDDEN = 0x2
        INVALID_FILE_ATTRIBUTES = -1

        def is_hidden(file):
            # 获取文件属性
            attrs = GetFileAttributesW(file)
            if attrs == INVALID_FILE_ATTRIBUTES:
                # 文件不存在或无法访问
                return False
            return attrs & FILE_ATTRIBUTE_HIDDEN == FILE_ATTRIBUTE_HIDDEN
        return is_hidden(file_path)

    def auto_open_next_folder_no_hidden(self, path):
        """自动打开下一个文件夹中的第一个非隐藏文件"""
        temp_list = []
        files = windows_sorted(path, 'file')
        for i in files:
            temp_list.append(os.path.join(path, i))
        no_hidden_list = []
        for i in temp_list:
            if not self.check_hidden(i):  # 排除隐藏文件
                no_hidden_list.append(i)
        os.startfile(no_hidden_list[0])  # 如果是文件夹则打开文件夹里面的第一个文件

    @staticmethod
    def get_time():
        """获取当前时间"""
        tm = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return tm

    def open_old(self):
        """打开原文件夹"""
        try:
            os.startfile(config.get(show_config, "folder_old"))
        except FileNotFoundError:
            self.ui.text_info.insertHtml("<font color='red' size='3'>" + "<br>" + "对应目录不存在" + "</font>")

    def check_model(self):
        """选择模式"""
        self.start_code = False
        if self.ui.radio_button_file.isChecked():
            config.set(show_config, 'model', 'file')
        else:
            config.set(show_config, 'model', 'folder')
        config.write(open('config.ini', 'w', encoding='utf-8'))
        self.config_load()

    def check_auto_open(self):
        """检查自动打开状态"""
        if self.ui.check_box_open_next.isChecked():
            config.set(show_config, 'auto_open', 'True')
        else:
            config.set(show_config, 'auto_open', 'False')
        config.write(open('config.ini', 'w', encoding='utf-8'))
        self.config_load()

    def scroll(self):
        """文本框下拉到底"""
        self.ui.text_info.verticalScrollBar().setValue(self.ui.text_info.verticalScrollBar().maximum())

    def select_config(self):
        """下拉框选择配置文件"""
        self.start_code = False
        selected = self.ui.combobox_select_config.currentText()
        config.set('DEFAULT', 'show_config', selected)
        config.write(open('config.ini', 'w', encoding='utf-8'))
        self.config_load()

    def change_move_folder_number(self):
        """改变文件夹数量"""
        new_number = str(self.ui.spinbox_move_folder_number.value())
        config.set(show_config, 'folder_number', new_number)
        config.write(open('config.ini', 'w', encoding='utf-8'))
        self.config_load()

    def show_where_is_now(self):
        """在当前文件/当前文件夹后添加标识（1/10）"""
        if self.file_number == len(need_moves):
            where_is_now = f"当前文件/文件夹：（{str(self.file_number)}/{str(len(need_moves))}）"
        else:
            where_is_now = f'当前文件/文件夹：（{str(self.file_number + 1)}/{str(len(need_moves))}）'
        self.ui.label_2.setText(str(where_is_now))


def main():
    app = QApplication()
    with open("UbuntuStyle.qss", "r", encoding='utf-8') as f:
        style = f.read()
        app.setStyleSheet(style)
    # app.setStyle('Fusion')
    quickmove = Quickmove()
    quickmove.ui.show()
    app.exec_()


if __name__ == "__main__":
    main()
