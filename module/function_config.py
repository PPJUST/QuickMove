# 配置文件相关方法
import configparser
import os

from constant import CONFIG_FILE, CONFIG_KEYS


def check_default_config():
    """检查配置文件"""
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w', encoding='utf-8'):
            pass

    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')

    try:
        config.get('DEFAULT', 'config')
    except configparser.NoOptionError:  # 如果DEFAULT项不存在则报错
        config.set('DEFAULT', 'config', '默认')
        config.set('DEFAULT', 'analyse_dirpath', '')
        for i in range(1, 10):
            config.set('DEFAULT', f'hotkey_move_{i}', f'<ctrl>+<{i + 96}>')  # 临时快捷键 右ctrl+小数字键盘0~9
        config.write(open(CONFIG_FILE, 'w', encoding='utf-8'))

    if not config.sections():
        config.add_section('默认')
        for key, value in CONFIG_KEYS.items():
            config.set('默认', key, str(value))
        config.write(open(CONFIG_FILE, 'w', encoding='utf-8'))


def get_default_section():
    """获取默认配置项"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    section = config.get('DEFAULT', 'config')
    return section


def set_default_section(section: str):
    """修改默认配置项"""
    # 由于qt下拉框绑定了该函数，导致下拉框清空时会调用该函数，导致添加一个空的section[]，需要单独判断排除
    if section:
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE, encoding='utf-8')
        config.set('DEFAULT', 'config', section)
        config.write(open(CONFIG_FILE, 'w', encoding='utf-8'))

        if section not in config:
            add_section(section)


def get_analyse_dirpath():
    """获取当前处理的文件夹路径"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    section = config.get('DEFAULT', 'analyse_dirpath')
    return section


def set_analyse_dirpath(path: str):
    """修改当前处理的文件夹路径"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    config.set('DEFAULT', 'analyse_dirpath', path)
    config.write(open(CONFIG_FILE, 'w', encoding='utf-8'))


def get_move_hotkey(index):
    """获取对应的移动快捷键"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    hotkey = config.get('DEFAULT', f'hotkey_move_{str(index)}')
    return hotkey


def set_move_hotkey(index, hotkey):
    """修改当前处理的文件夹路径"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    config.set('DEFAULT', f'hotkey_move_{str(index)}', str(hotkey))
    config.write(open(CONFIG_FILE, 'w', encoding='utf-8'))


def is_has_section(section: str):
    """检查是否已存在该配置项"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    return section in config


def add_section(section: str):
    """添加配置项"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    config.set('DEFAULT', 'config', section)
    config.add_section(section)
    for key, value in CONFIG_KEYS.items():
        config.set(section, key, str(value))

    config.write(open(CONFIG_FILE, 'w', encoding='utf-8'))


def delete_section(section: str):
    """删除配置项"""
    if not section:
        return
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    # 删除
    config.remove_section(section)
    # 修改默认项
    sections = config.sections()
    if sections:
        config.set('DEFAULT', 'config', sections[0])
        config.write(open(CONFIG_FILE, 'w', encoding='utf-8'))
    else:  # 如果删除后无其他配置项，则新增默认项
        config.write(open(CONFIG_FILE, 'w', encoding='utf-8'))
        check_default_config()


def get_sections():
    """获取所有设置项"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    sections = config.sections()
    return sections


def get_value_of_key(key: str):
    """获取默认配置项某个key的value"""
    default_section = get_default_section()

    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    value = config.get(default_section, key)

    return value


def set_value_of_key(key: str, value: str):
    """修改默认配置项某个key的value"""
    default_section = get_default_section()

    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    config.set(default_section, key, str(value))
    config.write(open(CONFIG_FILE, 'w', encoding='utf-8'))


def get_setting_mode_move():
    return get_value_of_key('mode_move')


def set_setting_mode_move(value):
    set_value_of_key('mode_move', value)


def get_setting_mode_walk():
    return get_value_of_key('mode_walk')


def set_setting_mode_walk(value):
    set_value_of_key('mode_walk', value)


def get_setting_auto_open_file():
    return get_value_of_key('auto_open_file') == 'True'


def set_setting_auto_open_file(value):
    set_value_of_key('auto_open_file', value)


def get_setting_auto_open_path():
    return get_value_of_key('auto_open_path') == 'True'


def set_setting_auto_open_path(value):
    set_value_of_key('auto_open_path', value)


def get_setting_reconfirm_rename():
    return get_value_of_key('reconfirm_rename') == 'True'


def set_setting_reconfirm_rename(value):
    set_value_of_key('reconfirm_rename', value)


def get_setting_rename_pattern():
    return get_value_of_key('rename_pattern')


def set_setting_rename_pattern(value):
    set_value_of_key('rename_pattern', value)


def get_setting_target_dir_count():
    return int(get_value_of_key('target_dir_count'))


def set_setting_target_dir_count(value):
    set_value_of_key('target_dir_count', value)


def get_setting_target_dirpath(index):
    return get_value_of_key(f'target_dirpath_{str(index)}')


def set_setting_target_dirpath(index, value):
    set_value_of_key(f'target_dirpath_{str(index)}', value)
