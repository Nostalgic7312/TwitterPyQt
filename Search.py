import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from Lib.SharedInfo import SharedInfo
from Searching import SearchingWidget
from UI.ui_search import Ui_Form
from WarningConfigLack import WarningConfigLackWidget


class SearchWidget(QtWidgets.QWidget):

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
        self.ui.pushButton.clicked.connect(self.select_seed_file)

        # 判断是否为空
        self.check_lineEdit()
        self.ui.lineEdit.textChanged.connect(self.check_lineEdit)
        self.ui.lineEdit_2.textChanged.connect(self.check_lineEdit)
        self.ui.lineEdit_3.textChanged.connect(self.check_lineEdit)

    def back_to(self):
        self.close()

    def confirm(self):
        for key in SharedInfo.sys_config:
            if SharedInfo.sys_config[key] == '':
                SharedInfo.widget_warning_config_lack = WarningConfigLackWidget()
                SharedInfo.widget_warning_config_lack.show()
                return
        SharedInfo.widget_searching = SearchingWidget()
        SharedInfo.widget_searching.show()
        self.close()

    def select_seed_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName()
        if fileName:
            self.ui.lineEdit_3.setText(fileName)

    def check_lineEdit(self):
        if self.ui.lineEdit.text() == '' or self.ui.lineEdit_2.text() == '' or self.ui.lineEdit_3.text() == '':
            self.ui.pushButton_confirm.setEnabled(False)
        else:
            self.ui.pushButton_confirm.setEnabled(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = SearchWidget()
    window.show()
    app.exec_()
