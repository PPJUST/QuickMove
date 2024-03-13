# 打开文件的相关方法
import os

from module import function_windows_sort
from module.function_normal import is_hidden_file


def open_path(path):
    """打开文件/文件夹中第一个文件"""
    if os.path.isdir(path):
        _open_first_file_in_folder(path)
    else:
        os.startfile(path)


def open_parent_folder(path):
    """打开指定文件/文件夹的父文件夹"""
    parent_folder = os.path.dirname(path)
    os.startfile(parent_folder)


def _open_first_file_in_folder(folder_path: str):
    """打开指定文件夹中的第一个文件（非隐藏）"""
    files = function_windows_sort.sort_path(folder_path, filetype='file', depth=1)
    files_unhidden = [i for i in files if not is_hidden_file(i)]

    if files_unhidden:
        first_file = files_unhidden[0]
        os.startfile(first_file)
        return first_file
    else:
        return None
