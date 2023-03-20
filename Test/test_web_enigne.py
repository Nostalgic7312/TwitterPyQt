import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import  QWebEngineView


class MainWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(1500, 1000)
        self.setStyleSheet('background-color:rgba(255,255,255,.5)')
        self.browser = QWebEngineView(self)
        self.browser.resize(1500, 1000)
        self.browser.load(QUrl('../html/force.html'))


if __name__ == '__main__':
    sys = QtWidgets.QApplication(sys.argv)
    w = MainWidget()
    w.show()
    sys.exec_()
