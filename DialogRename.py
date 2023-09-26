from typing import Tuple

from PySide2.QtWidgets import QDialog

from ui_DialogRename import Ui_Dialog


class DialogRename(QDialog):
    def __init__(self, add_prefix: str, filename: str, add_suffix: str, file_suffix: str):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # 初始化
        self.add_prefix = add_prefix
        self.filename = filename
        self.add_suffix = add_suffix
        self.file_suffix = file_suffix

        # 写入ui
        self.ui.lineEdit_add_prefix.setText(add_prefix)
        self.ui.lineEdit_filename.setText(filename)
        self.ui.lineEdit_add_suffix.setText(add_suffix)
        self.ui.lineEdit_file_suffix.setText(file_suffix)

        # 连接信号
        self.ui.buttonBox.accepted.connect(self.return_filename)
        self.ui.buttonBox.rejected.connect(self.reject)

        self.ui.lineEdit_filename.textChanged.connect(self.change_text)
        self.ui.lineEdit_add_prefix.textChanged.connect(self.change_text)
        self.ui.lineEdit_add_suffix.textChanged.connect(self.change_text)
        self.ui.lineEdit_file_suffix.textChanged.connect(self.change_text)

    def change_text(self):
        self.add_prefix = self.ui.lineEdit_add_prefix.text()
        self.filename = self.ui.lineEdit_filename.text()
        self.add_suffix = self.ui.lineEdit_add_suffix.text()
        self.file_suffix = self.ui.lineEdit_file_suffix.text()

    def return_filename(self) -> Tuple[str, str, str, str]:
        if self.exec_() == QDialog.Accepted:
            return self.add_prefix, self.filename, self.add_suffix, self.file_suffix
