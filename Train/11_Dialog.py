import sys

from PyQt5 import QtWidgets


class MyDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(600, 600)
        self.setWindowTitle("Comfirm")
        ok_btn = QtWidgets.QPushButton('Comfirm', self)
        ok_btn.setGeometry(300, 300, 100, 30)
        # self.setCentralWidget(layout)
        x, y, w, h = ok_btn.frameGeometry().getRect()

        ok_btn.move(int(300 - w / 2), int(300 - h / 2))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    w = MyDialog()
    w.show()
    app.exec_()
