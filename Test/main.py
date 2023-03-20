import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal,Qt
from PyQt5.QtWidgets import QAction
from pyqt5_plugins.examplebuttonplugin import QtGui

import Welcome


class MyMainWindow(QtWidgets.QMainWindow):
    signal_welcome = pyqtSignal(int)

    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.signal_welcome.connect(self.data_welcome)

        self.init_ui()

    def init_ui(self):
        self.resize(1000, 600)
        self.setStyleSheet('background-color:rgba(255,255,255,.5)')
        self.setEnabled(False)
        self.welcome = Welcome.WelcomeWidget(self.signal_welcome)
        self.welcome.show()

    def data_welcome(self, num_page):
        print(num_page)

    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.welcome.destroy()

if __name__ == '__main__':
    sys = QtWidgets.QApplication(sys.argv)

    window = MyMainWindow()

    window.show()

    sys.exec_()
