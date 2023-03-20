import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from Lib.SharedInfo import SharedInfo
from UI.ui_warning_config_lack import Ui_Form
from SysConfig import ConfigWidget

class WarningConfigLackWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.ui.pushButton_2.clicked.connect(self.back)
        self.ui.pushButton.clicked.connect(self.to_sys_config)

    def back(self):
        self.close()

    def to_sys_config(self):
        self.close()

        SharedInfo.sys_config = ConfigWidget()
        SharedInfo.sys_config.set_isFirst(False)
        SharedInfo.sys_config.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = WarningConfigLackWidget()
    window.show()
    app.exec_()
