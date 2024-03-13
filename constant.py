# 常量

# 文件
CONFIG_FILE = 'config.ini'

# 图标
ICON_ADD = 'icon/icon_add.png'
ICON_ANALYSE = 'icon/icon_analyse.png'
ICON_ASK_FOLDER = 'icon/icon_ask_folder.png'
ICON_CANCEL = 'icon/icon_cancel.png'
ICON_DELETE = 'icon/icon_delete.png'
ICON_MAIN = 'icon/icon_main.ico'
ICON_MOVE = 'icon/icon_move.png'
ICON_OPEN_FOLDER = 'icon/icon_open_folder.png'
ICON_QUIT = 'icon/icon_quit.png'
ICON_RECYCLE_BIN = 'icon/icon_recycle_bin.png'
ICON_SKIP = 'icon/icon_skip.png'
ICON_INFORMATION = 'icon/icon_information.png'
ICON_HOTKEY = 'icon/icon_hotkey.png'
ICON_CLEAR = 'icon/icon_clear.png'

# 配置项
CONFIG_KEYS = {'mode_move': 'file',
               'mode_walk': 'single',
               'auto_open_current': True,
               'auto_open_parent': False,
               'reconfirm_rename': False,
               'rename_pattern': '',
               'target_dir_count': 3,
               'target_dirpath_1': '',
               'target_dirpath_2': '',
               'target_dirpath_3': '',
               'target_dirpath_4': '',
               'target_dirpath_5': '',
               'target_dirpath_6': '',
               'target_dirpath_7': '',
               'target_dirpath_8': '',
               'target_dirpath_9': ''
               }

# 其他
RENAME_PATTERN_INFORMATION = """重命名模板说明：

1. 支持的元素
1.1 原始文件名(不含文件后缀)：以 * 表示
1.2 父文件夹名：以 < 表示
1.3 目标文件夹名：以 > 表示
1.3 顺序数字编号(按当前进度数字)：以 ? 表示
1.4 一般字符：正常输入即可

2. 其他说明
2.1 如果重命名结果不符合Windows文件名命名规则，则会进行提示
"""

ERROR_STYLESHEET = 'border: 1px solid red;'
