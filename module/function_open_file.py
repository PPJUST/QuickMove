# 打开文件的相关方法
import os

from module import function_windows_sort
from module.function_normal import is_hidden_file


def open_file(path):
    """打开文件/文件夹中第一个文件"""
    if os.path.isdir(path):
        _open_first_file_in_folder(path)
    else:
        os.startfile(path)


def open_path(path):
    """打开指定路径，文件为所在文件夹，文件夹为其自身"""
    if os.path.isdir(path):
        os.startfile(path)
    else:
        os.startfile(os.path.dirname(path))


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
