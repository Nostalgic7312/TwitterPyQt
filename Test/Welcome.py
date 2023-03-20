import sys

import PyQt5

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from pyqt5_plugins.examplebuttonplugin import QtGui


class WelcomeWidget(QtWidgets.QWidget):
    def __init__(self, signal):
        super().__init__()
        self.signal=signal
        self.init_ui()

    def init_ui(self):
        self.resize(400, 300)
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        v_layout = QtWidgets.QVBoxLayout()

        self.label_welcome = QtWidgets.QLabel('组织机构成员发现系统')
        self.label_welcome.setAlignment(Qt.AlignCenter)
        self.label_welcome.setStyleSheet('font-size:25px')
        v_layout.addStretch(1)
        v_layout.addWidget(self.label_welcome)

        self.label_version = QtWidgets.QLabel('v.1.0')
        self.label_version.setAlignment(Qt.AlignCenter)
        v_layout.addStretch(1)
        v_layout.addWidget(self.label_version)

        # 两个按钮标签
        h_layout = QtWidgets.QHBoxLayout()
        btn_enter = QtWidgets.QPushButton('进入')
        btn_enter.clicked.connect(self.click_enter)
        btn_config = QtWidgets.QPushButton('系统配置')
        btn_config.clicked.connect(self.click_config)
        h_layout.addStretch(1)
        h_layout.addWidget(btn_enter)
        h_layout.addStretch(1)
        h_layout.addWidget(btn_config)
        h_layout.addStretch(1)

        v_layout.addStretch(3)
        v_layout.addLayout(h_layout)
        v_layout.addStretch(1)

        self.setLayout(v_layout)

    def click_enter(self):
        self.signal.emit(1)
        # self.setWindowModality(Qt.NonModal)
        self.close()

    def click_config(self):
        self.signal.emit(2)
        self.close()



if __name__ == '__main__':
    sys = QtWidgets.QApplication(sys.argv)

    welcome = WelcomeWidget()

    welcome.show()

    sys.exit(sys.exec_())
