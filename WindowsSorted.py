"""以本地本地环境的排序规则进行排序"""
import locale
import os
import re
from typing import Union

"""
思路：
1. 初始化本地环境
2. 遍历所有排序元素，找出其中最长的连续数字字符串，获取其长度x
3. 再次遍历所有排序元素，将其中的连续数字字符串的长度扩展至x（首部加0，不考虑小数点）
4. 将新的排序元素与旧的排序元素一一对应，并建立键值对字典
5. 使用sorted指定key参数对新的排序元素进行排序
6. 将排序后的元素还原
7. 输出排序后的list
"""


def sort_path(dirpath: str, order: str = 'ASC', filetype: str = 'both', depth: int = 0) -> list:
    """排序指定路径中的文件/文件夹
    传参：dirpath 文件夹路径
    order 排序类型，'ASC'升序或'DESC'降序
    filetype 排序的文件类型，'file'文件或'folder'文件夹或'both'两者
    depth 遍历的层级深度，默认为0（最大层）
    返回值：path_sorted 根据参数返回不同的完整路径list"""
    path_sorted = [dirpath]  # 存放最终结果
    current_listdir_sorted_folder = [dirpath]  # 当前层级中的文件夹
    current_listdir_sorted_folder_copy = current_listdir_sorted_folder.copy()  # 用于递归
    if depth == 0:
        depth = 100

    current_depth = 0
    while current_depth < depth and current_listdir_sorted_folder:
        current_depth += 1
        for path in current_listdir_sorted_folder_copy:
            current_listdir_sorted = __sort_path_listdir(path, order=order, filetype=filetype)
            current_index = path_sorted.index(path)
            path_sorted[current_index + 1:current_index + 1] = current_listdir_sorted  # 利用切片插入列表元素（不能用insert）
            current_listdir_sorted_folder.remove(path)
            current_listdir_sorted_folder += [i for i in current_listdir_sorted if os.path.isdir(i)]
        current_listdir_sorted_folder_copy = current_listdir_sorted_folder.copy()  # 更新用于遍历的列表

    # 删除一开始赋值的多余的项目
    path_sorted.remove(dirpath)
    # 额外处理文件类型为file时的情况
    if filetype == 'file':
        path_sorted = [i for i in path_sorted if os.path.isfile(i)]

    return path_sorted


def __sort_path_listdir(dirpath: str, order: str = 'ASC', filetype: str = 'both') -> Union[SystemExit, list]:
    """排序指定路径中的文件/文件夹（仅第1层下级目录），并返回完整路径list
    传参：dirpath 文件夹路径
    order 排序类型，'ASC'升序或'DESC'降序
    filetype 排序的文件类型，'file'文件或'folder'文件夹或'both'两者
    返回值：listdir_sorted 根据参数返回不同的完整路径list"""
    listdir = os.listdir(dirpath)
    listdir_fullpath = [os.path.normpath(os.path.join(dirpath, i)) for i in listdir]
    listdir_fullpath_folder = [i for i in listdir_fullpath if os.path.isdir(i)]
    listdir_fullpath_file = [i for i in listdir_fullpath if os.path.isfile(i)]

    list_sorted_fullpath_folder = sort_list(listdir_fullpath_folder, order=order)
    list_sorted_fullpath_file = sort_list(listdir_fullpath_file, order=order)

    if filetype.lower() in ['both', 'file']:  # 如果排序类型是file也要返回整个list，但之后要删除folder项
        listdir_sorted = list_sorted_fullpath_folder + list_sorted_fullpath_file
    elif filetype.lower() == 'folder':
        listdir_sorted = list_sorted_fullpath_folder
    else:
        return SystemExit('传入参数错误，请检查！')

    return listdir_sorted


def sort_list(list_origin: list, order: str = 'ASC') -> Union[list, SystemExit]:
    """排序列表list
    传参：
    list_origin 原始的list
    order 排序类型，'ASC'升序或'DESC'降序
    返回值：list_sorted 排序后的list"""
    # 初始化本地环境
    locale.setlocale(locale.LC_ALL, '')

    # 转换list
    dict_convert = __convert_list(list_origin)
    list_convert = dict_convert.keys()

    # 使用sorted函数对转换后的list进行排序
    list_convert_sorted = sorted(list_convert, key=locale.strxfrm)

    # 还原原始list
    list_sorted = []
    for item in list_convert_sorted:
        value_list = dict_convert[item]  # 提取值
        value_list = sorted(value_list)  # 内部元素排序
        list_sorted += value_list

    # 按升降序参数返回对应list
    if order.upper() == 'ASC':
        return list_sorted
    elif order.upper() == 'DESC':
        return list_sorted[::-1]
    else:
        return SystemExit('传入参数错误，请检查！')


def __convert_list(list_origin: list) -> dict:
    """对传入的list进行处理，处理内部元素中的连续数字字符串
    传参：list_origin 原始的list
    返回值：dict_convert 转换后的dict，键为新元素，值为原始元素的list（用于处理01、001补0后重复的情况）"""
    # 遍历内部元素，利用正则提取所有连续数字字符串，最后得到其中最长的数字字符串长度
    longest_length = 0  # 最长的连续数字字符串长度
    pattern = r'(\d+)'
    for item in list_origin:
        numbers = re.findall(pattern, item)  # 提取数字字符串
        for i in numbers:
            if len(i) > longest_length:
                longest_length = len(i)

    dict_convert = dict()  # 转换后的dict，键为新元素，值为原始元素的list（用于处理01、001补0后重复的情况）
    # 重新遍历内部元素，利用正则将数字字符串补0扩展长度
    for item in list_origin:
        item_split = re.split(pattern, item)  # 分离数字字符串
        item_convert = ''  # 转换后的item
        for i in item_split:
            if i.isdigit():
                item_convert += i.zfill(longest_length)  # 对数字补0
            else:
                item_convert += i
        if item_convert not in dict_convert:
            dict_convert[item_convert] = []
        dict_convert[item_convert].append(item)

    return dict_convert
