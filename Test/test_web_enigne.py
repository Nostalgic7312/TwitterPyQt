import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import  QWebEngineView


class MainWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.resize(1600, 900)
        self.setStyleSheet('background-color:rgba(255,255,255,.5)')
        self.browser = QWebEngineView(self)
        self.browser.resize(1600, 900)
        self.browser.load(QUrl('file:///D:/PyCharm 2022.1.3/PythonProject/TwitterPyQt/html/force.html'))


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    sys = QtWidgets.QApplication(sys.argv)
    w = MainWidget()
    w.show()
    sys.exec_()
