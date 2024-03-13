# 重命名模板的方法
import os

from module import function_config


def create_new_filetitle(path: str, target_folder: str, index: int):
    """根据重命名模板生成新文件名（不含后缀）"""
    # 读取模板
    rename_pattern = function_config.get_setting_rename_pattern()

    # 提取关键词
    # 父文件夹名
    parent_dirname = os.path.basename(os.path.dirname(path))
    # 原始文件名和后缀名
    if os.path.isdir(path):
        origin_filetitle = os.path.basename(path)
    else:
        origin_filetitle = os.path.basename(os.path.splitext(path)[0])
    # 目标文件夹名
    target_dirname = os.path.basename(target_folder)
    # 顺序编号
    sequence_number = str(index)

    # 替换关键词
    if rename_pattern:
        new_filename = rename_pattern
        new_filename = new_filename.replace('*', origin_filetitle)
        new_filename = new_filename.replace('<', parent_dirname)
        new_filename = new_filename.replace('>', target_dirname)
        new_filename = new_filename.replace('?', sequence_number)

        return new_filename
    else:
        return origin_filetitle


def get_pattern_chs():
    """获取转换后的重命名模板"""
    # 读取模板
    rename_pattern = function_config.get_setting_rename_pattern()
    # 替换关键词
    if rename_pattern:
        pattern_chs = rename_pattern
        pattern_chs = pattern_chs.replace('*', '[原文件名]')
        pattern_chs = pattern_chs.replace('<', '[父目录名]')
        pattern_chs = pattern_chs.replace('>', '[目标文件夹名]')
        pattern_chs = pattern_chs.replace('?', '[索引数字]')
        pattern_chs += '[后缀名]'

        return pattern_chs
    else:
        return '[原文件名][后缀名]'
