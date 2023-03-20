import json
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from Lib.SharedInfo import SharedInfo
from UI.ui_sys_config import Ui_Form


class ConfigWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
        print('config')

    def init_ui(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        # self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.ui.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.init_lineEdit()
        self.ui.pushButton_return.clicked.connect(self.back_to_first)
        self.ui.pushButton_confirm.clicked.connect(self.confirm)

        # 通过按钮访问文件
        self.ui.pushButton.clicked.connect(self.save_file_outline)
        self.ui.pushButton_2.clicked.connect(self.save_file_result)

        self.valify_lineEdit()
        # 监听输入框事件判断是否为空
        self.ui.lineEdit_1.textChanged.connect(self.valify_lineEdit)
        self.ui.lineEdit_2.textChanged.connect(self.valify_lineEdit)
        self.ui.lineEdit_3.textChanged.connect(self.valify_lineEdit)
        self.ui.lineEdit_4.textChanged.connect(self.valify_lineEdit)
        self.ui.lineEdit_5.textChanged.connect(self.valify_lineEdit)
        self.ui.lineEdit_6.textChanged.connect(self.valify_lineEdit)
        self.ui.lineEdit_7.textChanged.connect(self.valify_lineEdit)

    def back_to_first(self):
        SharedInfo.widget_welcome.show()
        self.close()

    def back_to(self):
        self.close()

    def confirm(self):
        SharedInfo.sys_config['vpn_port'] = self.ui.lineEdit_1.text()
        SharedInfo.sys_config['database_account'] = self.ui.lineEdit_2.text()
        SharedInfo.sys_config['database_pwd'] = self.ui.lineEdit_3.text()
        SharedInfo.sys_config['twitter_dev_account'] = self.ui.lineEdit_4.text()
        SharedInfo.sys_config['chatgpt_account'] = self.ui.lineEdit_5.text()
        SharedInfo.sys_config['offline_file_path'] = self.ui.lineEdit_6.text()
        SharedInfo.sys_config['result_save_path'] = self.ui.lineEdit_7.text()
        sys_config_json = json.dumps(SharedInfo.sys_config)
        

        self.close()

    def set_isFirst(self, isFirst):
        if not isFirst:
            self.ui.pushButton_return.clicked.disconnect(self.back_to_first)
            self.ui.pushButton_return.clicked.connect(self.back_to)

    # 选择离线文件路径
    def save_file_outline(self):
        fileName = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if fileName:
            self.ui.lineEdit_6.setText(fileName)

    # 选择结果保存路径
    def save_file_result(self):
        fileName = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if fileName:
            self.ui.lineEdit_7.setText(fileName)

    # 初始化输入框内容
    def init_lineEdit(self):
        self.ui.lineEdit_1.setText(SharedInfo.sys_config['vpn_port'])
        self.ui.lineEdit_2.setText(SharedInfo.sys_config['database_account'])
        self.ui.lineEdit_3.setText(SharedInfo.sys_config['database_pwd'])
        self.ui.lineEdit_4.setText(SharedInfo.sys_config['twitter_dev_account'])
        self.ui.lineEdit_5.setText(SharedInfo.sys_config['chatgpt_account'])
        self.ui.lineEdit_6.setText(SharedInfo.sys_config['offline_file_path'])
        self.ui.lineEdit_7.setText(SharedInfo.sys_config['result_save_path'])

    def valify_lineEdit(self):
        if not (
                self.ui.lineEdit_1.text() != '' and self.ui.lineEdit_2.text() != '' and self.ui.lineEdit_3.text() != '' and self.ui.lineEdit_4.text() != '' and self.ui.lineEdit_5.text() != '' and self.ui.lineEdit_6.text() != '' and self.ui.lineEdit_7.text() != ''):
            self.ui.pushButton_confirm.setEnabled(False)
        else:
            self.ui.pushButton_confirm.setEnabled(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ConfigWidget()
    window.show()
    app.exec_()
