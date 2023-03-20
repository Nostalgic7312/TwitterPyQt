import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal


class MyWidget(QtWidgets.QWidget):
    my_signal = pyqtSignal(str)

    def __init__(self):
        super(MyWidget, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(600, 600)

        layout = QtWidgets.QVBoxLayout()

        btn = QtWidgets.QPushButton("Start", self)
        btn.clicked.connect(self.check)
        self.my_signal.connect(self.my_slot)
        layout.addStretch(2)
        layout.addWidget(btn)
        layout.addStretch(1)

        self.setLayout(layout)

    def check(self):
        for i, ip in enumerate([f"192.168.1.{x}" for x in range(1, 255)]):
            msg = f'Checking:{ip}'
            if i % 5 == 0:
                self.my_signal.emit(msg + "  发现漏洞")
            else:
                self.my_signal.emit(msg)

    def my_slot(self, msg):
        print(msg)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MyWidget()
    w.show()
    app.exec_()
