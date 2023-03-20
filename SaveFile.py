import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from Lib.SharedInfo import SharedInfo
from UI.ui_save_file import Ui_Form


class SaveFileWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        # self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.ui.pushButton_2.clicked.connect(self.confirm)

    def confirm(self):
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = SaveFileWidget()
    window.show()
    app.exec_()
