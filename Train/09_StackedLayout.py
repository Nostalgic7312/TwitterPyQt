import sys

from PyQt5 import QtWidgets


class Window1(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        QtWidgets.QLabel('Window1', self)


class Window2(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        QtWidgets.QLabel('Window2', self)


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.create_stacked_layout()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Stack")
        self.resize(300, 300)
        container = QtWidgets.QVBoxLayout()

        widget = QtWidgets.QWidget()
        widget.setLayout(self.stacked_layout)
        # widget.setStyleSheet('background-color:steelblue;')

        btn1 = QtWidgets.QPushButton("Win1")
        btn2 = QtWidgets.QPushButton("Win2")
        btn1.clicked.connect(self.btn1_clicked)
        btn2.clicked.connect(self.btn2_clicked)

        container.addWidget(widget)
        container.addWidget(btn1)
        container.addWidget(btn2)

        self.setLayout(container)

    def create_stacked_layout(self):
        self.stacked_layout = QtWidgets.QStackedLayout()
        win1 = Window1()
        win2 = Window2()
        self.stacked_layout.addWidget(win1)
        self.stacked_layout.addWidget(win2)

    def btn1_clicked(self):
        self.stacked_layout.setCurrentIndex(0)

    def btn2_clicked(self):
        self.stacked_layout.setCurrentIndex(1)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec_()
