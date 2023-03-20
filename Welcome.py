import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from Lib.SharedInfo import SharedInfo
from Search import SearchWidget
from SysConfig import ConfigWidget
from UI.UI_welcome import Ui_Form


class WelcomeWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        # self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.ui.btn_enter.clicked.connect(self.click_enter)
        self.ui.btn_config.clicked.connect(self.click_config)

    def click_enter(self):
        self.close()

    def click_config(self):
        self.close()
        SharedInfo.widget_config = ConfigWidget()
        SharedInfo.widget_config.set_isFirst(True)
        SharedInfo.widget_config.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = WelcomeWidget()
    window.show()
    app.exec_()
