# 更新日期：20230407

import os
import natsort
import re


def windows_sorted(path: str, files_list: list):
    """输入路径、文件列表，返回Windows排序规则的列表"""
    # 整合完整路径
    fullpath_files_list = []
    for i in files_list:
        fullpath_files_list.append(os.path.join(path, i))

    # 分离文件与文件夹
    fullpath_files = []
    fullpath_folders = []
    for i in fullpath_files_list:
        if os.path.isfile(i):
            fullpath_files.append(i)
        else:
            fullpath_folders.append(i)

    # 给每个字符前加前缀，取决于优先级
    add_prefix_files = []
    files_new_name_match_old_name = {}
    add_prefix_folders = []
    folders_new_name_match_old_name = {}
    for i in fullpath_files:
        filename = os.path.split(os.path.splitext(i)[0])[1]
        suffix = os.path.splitext(i)[1]
        add_prefix_filename = str_add_prefix(filename) + suffix
        add_prefix_files.append(add_prefix_filename)
        files_new_name_match_old_name[add_prefix_filename] = filename + suffix
    for i in fullpath_folders:
        filename = os.path.split(i)[1]
        add_prefix_filename = str_add_prefix(filename)
        add_prefix_folders.append(add_prefix_filename)
        folders_new_name_match_old_name[add_prefix_filename] = filename

    # 排序列表
    add_prefix_files = natsort.natsorted(add_prefix_files, alg=natsort.ns.LOCALE | natsort.ns.IC | natsort.ns.PATH | natsort.ns.COMPATIBILITYNORMALIZE)
    add_prefix_folders = natsort.natsorted(add_prefix_folders, alg=natsort.ns.LOCALE | natsort.ns.IC | natsort.ns.PATH | natsort.ns.COMPATIBILITYNORMALIZE)

    # 列表匹配字典，还原原始文件名
    sort_files_list = []
    sort_folders_list = []
    for i in add_prefix_files:
        sort_files_list.append(files_new_name_match_old_name[i])
    for i in add_prefix_folders:
        sort_folders_list.append(folders_new_name_match_old_name[i])

    # 连接最终结果
    finally_sort_list = sort_folders_list + sort_files_list

    return finally_sort_list


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
        '【': 'CM',
        '】': 'CN',
        '+': 'CO',
        '=': 'CP',
        '·': 'CQ',
        '…': 'CR',
    }
    # 数字DA判断 .isdigit()
    # 字母DB判断 .isalpha()
    # 其余字符EA，例如中文、日文、韩文

    split_digit_filename = [i for i in re.split(r'(\d+)', filename) if i]  # 使用正则分离数字与其他字符
    new_filename = ''
    for x in split_digit_filename:
        if x.isdigit():
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
