import ctypes

import WindowsSorted


def walk_path(path: str, model: str) -> list:
    """遍历传入路径中的文件/文件夹
    model:file, folder, both"""

    def check_hidden(t_path: str):
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

        return is_hidden(t_path)

    if model == 'file':
        # 遍历路径中的所有文件
        files_list = WindowsSorted.sort_path(path, filetype='file', depth=1)
        no_hidden_filepath_list = []
        for i in files_list:
            if not check_hidden(i):  # 排除隐藏文件
                no_hidden_filepath_list.append(i)
        return no_hidden_filepath_list
    elif model == 'folder':
        # 遍历路径中的所有文件夹
        folders_list = WindowsSorted.sort_path(path, filetype='folder', depth=1)
        no_hidden_folders_list = []
        for i in folders_list:
            if not check_hidden(i):  # 排除隐藏文件
                no_hidden_folders_list.append(i)
        return no_hidden_folders_list


def print_function_info(model: str = 'current'):
    """打印当前/上一个执行的函数信息
    传参：model 'current'/'last'"""
    import time
    import inspect

    if model == 'current':
        print(time.strftime('%H:%M:%S ', time.localtime()),
              inspect.getframeinfo(inspect.currentframe().f_back).function)
    elif model == 'last':
        print(time.strftime('%H:%M:%S ', time.localtime()),
              inspect.getframeinfo(inspect.currentframe().f_back.f_back).function)
