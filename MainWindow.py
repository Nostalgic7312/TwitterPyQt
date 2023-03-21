import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from Lib.SharedInfo import SharedInfo
from Search import SearchWidget
from SysConfig import ConfigWidget
from UI.UI_MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.show_config)
        self.ui.pushButton_2.clicked.connect(self.show_search)
        self.ui.pushButton.setShortcut(Qt.CTRL + Qt.Key_N)

    def show_config(self):
        SharedInfo.widget_config = ConfigWidget()
        SharedInfo.widget_config.set_isFirst(False)
        SharedInfo.widget_config.show()

    def show_search(self):
        SharedInfo.widget_search = SearchWidget()
        SharedInfo.widget_search.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
