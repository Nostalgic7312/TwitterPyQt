import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl, QFileInfo

from Lib.SharedInfo import SharedInfo
from Search import SearchWidget
from SysConfig import ConfigWidget

from test_web import Ui_Form


class MainWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.widget_browser.load(QUrl(QFileInfo('../html/force.html').absoluteFilePath()))

        # 调整widget_browser的大小
        self.ui.widget_browser.resize(500, 500)
        # 调整widget_browser的位置
        self.ui.widget_browser.move(50, 50)
        # 调整widget_browser的透明度
        self.ui.widget_browser.setWindowOpacity(0.5)
        # 调整widget_browser的背景色
        self.ui.widget_browser.setStyleSheet("background-color: rgb(255, 255, 255);")



if __name__ == '__main__':
    sys = QtWidgets.QApplication(sys.argv)
    w = MainWidget()
    w.show()
    sys.exec_()
