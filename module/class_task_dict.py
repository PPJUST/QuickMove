# 任务清单，用于处理索引、执行具体文件操作等
import os

from module import function_normal, function_rename_pattern, function_open_file, function_config


class TaskDict(dict):
    def __init__(self):
        super().__init__()
        self.current_index = 0  # 当前索引号，0代表空或超限
        self.current_path = None  # 当前索引对应的文件路径
        self.count = 0  # 任务总数

    def set_task(self, paths: list):
        """添加任务清单"""
        if paths:
            self.clear()
            for index, path in enumerate(paths, start=1):
                self[index] = {'operation': 'tbd',
                               'origin_path': path,
                               'moved_path': None}
            self.current_index = 1
            self.current_path = None
            self.count = len(self)
            self.current_path = self[self.current_index]['origin_path']
            # 是否自动打开
            self._auto_open()
        else:
            self.clear()
            self.current_index = 0
            self.current_path = None
            self.count = 0

    def operation_delete(self):
        """对当前索引对应的文件执行删除操作"""
        # 执行操作
        is_succeed = function_normal.delete_file(self.current_path)
        if not is_succeed:  # 如果操作失败，则直接返回
            return False

        # 修改字典数据（删除+重新排列）
        self.pop(self.current_index)
        resort_dict = {}
        for key, value in self.items():
            if key < self.current_index:
                resort_dict[key] = value
            else:
                resort_dict[key - 1] = value
        self.clear()
        self.update(resort_dict)
        # 检查是否超限
        self.count = len(self)
        if self.current_index > self.count:
            self.current_index = self.count
        self.current_path = self[self.current_index]['origin_path']

        # 是否自动打开
        self._auto_open()

        return True

    def operation_move(self, target_folder: str):
        """对当前索引对应的文件执行移动操作"""
        # 执行操作
        target_filetitle = function_rename_pattern.create_new_filetitle(self.current_path, target_folder,
                                                                        self.current_index)
        new_path = function_normal.move_file(self.current_path, target_filetitle, target_folder)
        if not new_path:
            return False

        # 修改字典数据
        self._set_operation('move')
        self[self.current_index]['moved_path'] = new_path
        self._to_next()

        # 是否自动打开
        self._auto_open()

        return new_path

    def operation_skip(self):
        """对当前索引对应的文件执行跳过操作"""
        self._set_operation('skip')
        self._to_next()

        # 是否自动打开
        self._auto_open()

    def operation_cancel(self):
        """在当前索引位置执行撤销操作，退回上一个索引"""
        # 回退索引
        self._to_previous()
        last_operation = self[self.current_index]['operation']
        # 如果是撤销移动操作，则将新文件移回原路径
        if last_operation == 'move':
            origin_path = self[self.current_index]['origin_path']
            moved_path = self[self.current_index]['moved_path']
            origin_parent_dir = os.path.dirname(origin_path)
            if os.path.isdir(moved_path):
                target_filetitle = os.path.basename(origin_path)
            else:
                target_filetitle = os.path.basename(os.path.splitext(origin_path)[0])
            new_path = function_normal.move_file(moved_path, target_filetitle, origin_parent_dir)
            if new_path != origin_path:
                self[self.current_index]['origin_path'] = new_path
        # 修改操作状态（除删除外）
        if last_operation != 'delete':
            self[self.current_index]['operation'] = 'tbd'

        # 是否自动打开
        self._auto_open()

    def _auto_open(self):
        """根据设置自动打开文件/文件夹"""
        if self.current_path and os.path.exists(self.current_path):
            is_open_current = function_config.get_setting_auto_open_file()
            if is_open_current:
                function_open_file.open_file(self.current_path)

            is_open_parent = function_config.get_setting_auto_open_path()
            if is_open_parent:
                function_open_file.open_path(self.current_path)

    def _set_operation(self, operation: str):
        """设置当前索引对应的字典的key"""
        self[self.current_index]['operation'] = operation

    def _to_next(self):
        """切换到下一个索引"""
        if self.current_index == 0:
            pass
        elif self.current_index < self.count:
            self.current_index += 1
            self.current_path = self[self.current_index]['origin_path']
        else:
            self.current_index = 0
            self.current_path = None

    def _to_previous(self):
        """切换到上一个索引"""
        if self.current_index == 0:
            self.current_index = self.count
            self.current_path = self[self.current_index]['origin_path']
        elif self.current_index == 1:
            pass
        else:
            self.current_index -= 1
            self.current_path = self[self.current_index]['origin_path']

    def _is_deleted(self):
        """检查当前索引文件是否已经删除"""
        if self[self.current_index]['operation'] == 'delete':
            return True
        else:
            return False
