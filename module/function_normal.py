# 一般方法
import ctypes
import inspect
import os
import shutil
import time

import send2trash


def print_function_info(mode: str = 'current'):
    """打印当前/上一个执行的函数信息
    传参：mode 'current' 或 'last'"""
    # pass

    if mode == 'current':
        print(time.strftime('%H:%M:%S ', time.localtime()),
              inspect.getframeinfo(inspect.currentframe().f_back).function)
    elif mode == 'last':
        print(time.strftime('%H:%M:%S ', time.localtime()),
              inspect.getframeinfo(inspect.currentframe().f_back.f_back).function)


def reverse_path(path: str):
    """反转路径，从后到前排列目录层级"""
    path = os.path.normpath(path)
    split_path = path.split('\\')
    path_reversed = ' \\ '.join(split_path[::-1])
    return path_reversed


def check_filename_feasible(filename: str):
    """检查一个文件名是否符合Windows文件命名规范"""
    # 官方文档：文件和文件夹不能命名为“.”或“..”，也不能包含以下任何字符: \ / : * ? " < > |
    except_word = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']

    # 检查.
    if filename[0] == '.':
        return False

    # 检查其余符号
    for key in except_word:
        if key in filename:
            return False
    return True


def create_nodup_filename(path: str, target_filetitle: str, target_dirpath: str, add_suffix: str = ' -New') -> str:
    """
    生成传入的文件或文件夹在指定文件夹中没有重复的文件名（添加自定义后缀）
    :param path: 原始文件或文件夹路径str
    :param target_filetitle: 目标文件名str（不含后缀）
    :param target_dirpath: 指定文件夹路径str
    :param add_suffix: 自定义后缀
    :return: str，无重复的文件名（非完整路径，仅文件名）
    """
    if os.path.isfile(path):
        suffix = os.path.splitext(path)[1]
    else:
        suffix = ''

    new_filename = target_filetitle + suffix
    temp_filename = target_filetitle + add_suffix + '1' + suffix

    # 生成无重复的文件名
    count = 0
    # 一直累加循环直到不存在同名（同级目录也要检查，防止重命名报错）
    while os.path.exists(os.path.join(target_dirpath, new_filename)) or os.path.exists(
            os.path.join(os.path.split(path)[0], temp_filename)):
        count += 1
        new_filename = f'{target_filetitle}{add_suffix}{count}{suffix}'
        temp_filename = new_filename

    return new_filename


def is_hidden_file(path: str):
    """路径对应的文件是否隐藏"""
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


def delete_file(path: str) -> bool:
    """删除文件/文件夹
    :return: bool，是否成功删除"""
    try:
        send2trash.send2trash(path)
        return True
    except PermissionError:  # 如果文件被占用，则返回False
        return False


def move_file(path: str, target_filetitle: str, target_folder: str):
    """移动文件/文件夹至指定文件夹"""
    # 生成新文件名
    new_filename = create_nodup_filename(path, target_filetitle, target_folder)
    # 先重命名原文件
    parent_dirpath = os.path.dirname(path)
    new_path = os.path.normpath(os.path.join(parent_dirpath, new_filename))
    if new_path != path:
        try:
            os.rename(path, new_path)
        except PermissionError:  # 如果文件被占用，则返回False
            return False

    # 再进行移动
    try:
        finally_path = shutil.move(new_path, target_folder)
    except PermissionError:  # 如果文件被占用，则返回False
        return False

    return os.path.normpath(finally_path)
