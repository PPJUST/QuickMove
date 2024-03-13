# 分析需要整理的文件夹的相关方法
import os

from module import function_config, function_windows_sort, function_normal

"""文件夹分析逻辑：
| 逻辑   | 文件模式                   | 文件夹模式                      |
|------|------------------------|----------------------------|
| 单层下级 | 提取文件夹中的第一层文件（不在子文件夹中的） | 提取文件夹中的第一层子文件夹（内部不存在子文件夹的） |
| 全部层级 | 提取所有文件                 | 提取所有子文件夹（内部不存在子文件夹的）       |
"""


def extract():
    """提取对应层级的文件或文件夹"""
    # 读取设置
    analyse_dirpath = function_config.get_analyse_dirpath()
    mode_move = function_config.get_setting_mode_move()
    mode_walk = function_config.get_setting_mode_walk()
    # 提取文件或文件夹
    if mode_move == 'file' and mode_walk == 'single':
        extract_paths = _extract_files_single(analyse_dirpath)
    elif mode_move == 'file' and mode_walk == 'all':
        extract_paths = _extract_files_all(analyse_dirpath)
    elif mode_move == 'folder' and mode_walk == 'single':
        extract_paths = _extract_dirs_single(analyse_dirpath)
    elif mode_move == 'folder' and mode_walk == 'all':
        extract_paths = _extract_dirs_all(analyse_dirpath)
    else:
        extract_paths = []
    # 排序列表
    extract_paths = function_windows_sort.sort_list(extract_paths)

    return extract_paths


def _extract_files_single(parent_dirpath: str):
    """提取单层文件"""
    listdir = os.listdir(parent_dirpath)
    paths = [os.path.normpath(os.path.join(parent_dirpath, i)) for i in listdir]
    files = [i for i in paths if os.path.isfile(i)]
    files_unhidden = [i for i in files if not function_normal.is_hidden_file(i)]

    return files_unhidden


def _extract_files_all(parent_dirpath: str):
    """提取全部文件"""
    files = []
    for dirpath, dirnames, filenames in os.walk(parent_dirpath):
        for j in filenames:
            filepath_join = os.path.normpath(os.path.join(dirpath, j))
            if not function_normal.is_hidden_file(filepath_join):
                files.append(filepath_join)

    return files


def _extract_dirs_single(parent_dirpath: str):
    """提取单层文件夹"""
    listdir = os.listdir(parent_dirpath)
    paths = [os.path.normpath(os.path.join(parent_dirpath, i)) for i in listdir]
    folders = [i for i in paths if os.path.isdir(i)]
    folders_filter = [i for i in folders if not _is_has_child_folder(i)]  # 剔除含有子文件夹的项

    return folders_filter


def _extract_dirs_all(parent_dirpath: str):
    """提取全部文件夹"""
    folders_filter = []
    for dirpath, dirnames, filenames in os.walk(parent_dirpath):
        for j in dirnames:
            dirpath_join = os.path.normpath(os.path.join(dirpath, j))
            if not _is_has_child_folder(dirpath_join):  # 剔除含有子文件夹的项
                folders_filter.append(dirpath_join)

    return folders_filter


def _is_has_child_folder(dirpath):
    """文件夹中是否包含子文件夹"""
    listdir = os.listdir(dirpath)
    paths = [os.path.normpath(os.path.join(dirpath, i)) for i in listdir]
    child_folders = [i for i in paths if os.path.isdir(i)]

    return True if child_folders else False
