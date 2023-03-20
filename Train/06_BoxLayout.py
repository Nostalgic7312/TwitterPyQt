import sys
from PyQt5 import QtWidgets


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.setWindowTitle('QVBoxLayout')

        layout = QtWidgets.QVBoxLayout()

        btn1 = QtWidgets.QPushButton('one')
        btn2 = QtWidgets.QPushButton('two')
        btn3 = QtWidgets.QPushButton('three')

        layout.addStretch(1)
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addStretch(2)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec_()
