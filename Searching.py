import sys
import time

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QThread

import SaveFile
from Lib.SharedInfo import SharedInfo
from UI.ui_searching import Ui_Form


class SearchingWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        # self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        self.ui.pushButton_return.clicked.connect(self.back_to)
        self.ui.pushButton_confirm.clicked.connect(self.confirm)
        self.ui.progressBar.setRange(1, 100)
        self.ui.progressBar.setValue(1)

        self.set_loader()

    def back_to(self):
        SharedInfo.widget_search.show()
        self.close()

    def confirm(self):
        # TODO
        self.close()

    def set_loader(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.load_progress_bar)
        self.timer.start(100)

    def load_progress_bar(self):
        self.ui.progressBar.setValue(self.ui.progressBar.value() + 1)
        if self.ui.progressBar.value() >= 100:
            self.open_table_main()
            self.timer.stop()

    def open_table_main(self):
        SharedInfo.widget_save_file = SaveFile.SaveFileWidget()
        SharedInfo.widget_save_file.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = SearchingWidget()
    window.show()
    app.exec_()
