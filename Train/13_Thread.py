import json
import sys
import time

import requests
from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *


class LoginThread(QThread):
    start_login_signal = pyqtSignal(str)

    def __init__(self, login_status_signal):
        super(LoginThread, self).__init__()
        self.start_login_signal.connect(self.login_thread)
        self.login_status_signal = login_status_signal

    def login_thread(self, msg):
        print(msg)
        # r = requests.post(url='http://127.0.0.1:3000/posts')
        # print(r.__dict__)
        self.login_status_signal.emit('登录成功')

    def run(self):
        while (True):
            print("Thread Runing")
            time.sleep(1)


class MyWindow(QWidget):
    login_status_signal = pyqtSignal(str)

    def __init__(self):
        super(MyWindow, self).__init__()
        self.init_ui()
        self.login_status_signal.connect(self.login_status)

    def init_ui(self):
        self.ui = uic.loadUi('./Thread.ui')
        self.ui.resize(950, 600)

        self.label_username = self.ui.label_username
        self.label_password = self.ui.label_password
        self.lineEdit_username = self.ui.lineEdit_username
        self.lineEdit_password = self.ui.lineEdit_password
        self.pushButton_login = self.ui.pushButton_login
        self.pushButton_Forget = self.ui.pushButton_Forget
        self.textBrowser = self.ui.textBrowser

        self.pushButton_login.clicked.connect(self.login)
        self.login_thread = LoginThread(self.login_status_signal)
        self.login_thread.start()

    def login(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        self.login_thread.start_login_signal.emit(json.dumps({'username': username, 'password': password}))

    def login_status(self, status):
        self.textBrowser.setText(status)
        self.textBrowser.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.ui.show()
    app.exec_()
