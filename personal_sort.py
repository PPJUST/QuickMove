"""
1. 制作思路
在字符串的每一个字符前按字符的优先级添加ABCDE等前缀，连续的数字字符先合并后再添加前缀，最后使用natsort库添加key、alg后排序。

2. 目前存在的问题
"-"、"."的排序有问题：Windows系统下，"1-"会排序在"1_"前，但是"1_1"会排序在"1=1"前。本模块按字符排序的方法没有解决这个问题。
只排序了部分字符
"""

import os
import natsort
import locale
import re


def windows_sorted(dirpath_or_filelist: str or list, model: str) -> list:
    """输入路径、模式，返回Windows排序规则的列表

    输入:dirpath_or_filelist, model

    dirpath_or_filelist：目标文件夹路径，str类型；或者一个文件列表，list类型

    model：处理模式（'file'：排序文件；'folder'：排序文件夹；'both'：排序文件和文件夹）

    返回：排序后的列表；如果路径、处理模式不正确则返回提示文本

    """
    fullpath_files_list = []  # 设置一个空列表变量
    if type(dirpath_or_filelist) is str:
        dirpath = dirpath_or_filelist

        # 遍历路径文件
        if os.path.exists(dirpath) and os.path.isdir(dirpath):
            files_list = os.listdir(dirpath)

            # 组合完整路径
            for i in files_list:
                fullpath_files_list.append(os.path.join(dirpath, i))
        else:
            return "路径不存在或者不是文件夹"
    elif type(dirpath_or_filelist) is list:
        fullpath_files_list = dirpath_or_filelist
    else:
        return "输入变量的格式错误，不是文件夹路径或者文件列表"

    # 分离文件与文件夹
    fullpath_files = []
    fullpath_folders = []
    for i in fullpath_files_list:
        if os.path.isfile(i):
            fullpath_files.append(i)
        else:
            fullpath_folders.append(i)

    # 按model传递参数
    if model == 'file':
        result = run_sorted_file(fullpath_files)
        return result
    elif model == 'folder':
        result = run_sorted_folder(fullpath_folders)
        return result
    elif model == 'both':
        result1 = run_sorted_folder(fullpath_folders)
        result2 = run_sorted_file(fullpath_files)
        result = result1 + result2
        return result
    else:
        return 'model设置不正确，可用项为file/folder/both'


def run_sorted_file(fullpath_files):
    # 给每个字符前加前缀，取决于优先级
    add_prefix_files = []
    files_new_name_match_old_name = {}
    for i in fullpath_files:
        filename = os.path.split(os.path.splitext(i)[0])[1]
        suffix = os.path.splitext(i)[1]
        add_prefix_filename = str_add_prefix(filename) + suffix
        add_prefix_files.append(add_prefix_filename)
        files_new_name_match_old_name[add_prefix_filename] = filename + suffix

    # 排序列表
    locale.setlocale(locale.LC_ALL, '')
    sort_key = natsort.natsort_keygen()
    add_prefix_files = natsort.natsorted(add_prefix_files, key=sort_key,
                                         alg=natsort.ns.LOCALE | natsort.ns.IC | natsort.ns.PATH | natsort.ns.COMPATIBILITYNORMALIZE)

    # 列表匹配字典，还原原始文件名
    sort_files_list = []
    for i in add_prefix_files:
        sort_files_list.append(files_new_name_match_old_name[i])

    return sort_files_list


def run_sorted_folder(fullpath_folders):
    # 给每个字符前加前缀，取决于优先级
    add_prefix_folders = []
    folders_new_name_match_old_name = {}
    for i in fullpath_folders:
        filename = os.path.split(i)[1]
        add_prefix_filename = str_add_prefix(filename)
        add_prefix_folders.append(add_prefix_filename)
        folders_new_name_match_old_name[add_prefix_filename] = filename

    # 排序列表
    locale.setlocale(locale.LC_ALL, '')
    sort_key = natsort.natsort_keygen()
    add_prefix_folders = natsort.natsorted(add_prefix_folders, key=sort_key,
                                           alg=natsort.ns.LOCALE | natsort.ns.IC | natsort.ns.PATH | natsort.ns.COMPATIBILITYNORMALIZE)

    # 列表匹配字典，还原原始文件名
    sort_folders_list = []
    for i in add_prefix_folders:
        sort_folders_list.append(folders_new_name_match_old_name[i])

    return sort_folders_list


def str_add_prefix(filename: str) -> str:
    # 输入字符串，返回按优先级添加ABCDEFG的新字符串（数字合并后添加前缀）
    # 空格AA判断，==' '
    prefix_auto_dict = {
        "'": 'BA',
        '-': 'BB',
        '—': 'BC',
        '!': 'BD',
        '！': 'BE',
        '#': 'BF',
        '$': 'BG',
        '%': 'BH',
        '&': 'BI',
        '(': 'BJ',
        '（': 'BK',
        ')': 'BL',
        '）': 'BM',
        ',': 'BN',
        '，': 'BO',
        '、': 'BP',
        '.': 'BQ',
        '。': 'BR',
        '：': 'BS',
        ';': 'BT',
        '；': 'BU',
        '？': 'BV',
        '@': 'BW',
        '[': 'BX',
        ']': 'BY',
        '^': 'BZ',
        '_': 'CA',
        '`': 'CB',
        '{': 'CC',
        '}': 'CD',
        '~': 'CE',
        '‘': 'CF',
        '’': 'CG',
        '“': 'CH',
        '”': 'CI',
        '《': 'CJ',
        '》': 'CK',
        '￥': 'CL',
        '「': 'CM',
        '」': 'CN',
        '【': 'CO',
        '】': 'CP',
        '+': 'CQ',
        '=': 'CR',
        '·': 'CS',
        '…': 'CT',
    }
    # 数字DA判断 .isdigit()
    # 字母DB判断 .isalpha()
    # 其余字符EA，例如中文、日文、韩文

    # 使用正则分离字符串中的数字与其他字符
    # 230407的分组方法
    # split_digit_filename = [i for i in re.split(r'(\d+)', filename) if i]  # 使用正则分离数字与其他字符
    split_digit_filename = [i for i in re.split(r'([^\d.]+)', filename) if i]
    new_split_digit_filename = []
    for i in split_digit_filename:  # 分离有多个小数点的列表元素（如果有多个小数点，则以第二个小数点为界分割）
        if re.match(r'^\d+(\.\d*)*$', i):  # 如果都是数字与小数点且以数字开头
            if i.count('.') == 1:  # 如果只出现1次
                new_split_digit_filename.append(i)
            else:  # 如果出现多次
                temp_split = [x for x in re.split(r'(\d+\.\d+)', i) if x]  # 分离小数，后面取第1个小数，其他的按.切割
                split_float = temp_split[0]  # 取第一个小数
                split_other = temp_split[1:]  # 其他内容
                split_other_join = ''.join(split_other)  # 合并其他内容
                split_other_join_split = [y for y in re.split(r'(\d+)', split_other_join) if y]  # 切割合并后的其他内容
                new_split_digit_filename.append(split_float)
                new_split_digit_filename += split_other_join_split
        else:
            temp_split = [z for z in re.split(r'(\d+)', i) if z]  # 再次分离，防止有.开头的
            new_split_digit_filename += temp_split
    split_digit_filename = new_split_digit_filename  # 还原回去

    new_filename = ''
    for x in split_digit_filename:
        if re.match(r'^\d+(.\d+)?$', x):  # 如果都是数字与小数点。之前用的x.isdigit()，不再使用
            new_filename += "DA" + x
        else:
            for i in x:
                if i == ' ':
                    new_filename += "AA" + i
                elif i in prefix_auto_dict:
                    new_filename += prefix_auto_dict[i] + i
                elif i.isdigit():
                    new_filename += "DA" + i
                elif i.isalpha():
                    new_filename += "DB" + i
                else:
                    new_filename += "EA" + i
    return new_filename
