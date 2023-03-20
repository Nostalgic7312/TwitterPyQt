import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from Lib.SharedInfo import SharedInfo
from MainWindow import MainWindow
from SysConfig import ConfigWidget
from Welcome import WelcomeWidget


if __name__ == '__main__':
    # 支持高分辨率，确保与QtDesigner设计一致
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)  # 创建GUI应用程序

    SharedInfo.window_main = MainWindow()  # 创建主窗体
    SharedInfo.window_main.show()  # 显示主窗体

    SharedInfo.widget_welcome = WelcomeWidget()
    SharedInfo.widget_welcome.show()

    app.exit(app.exec())
