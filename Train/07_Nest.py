import sys

from PyQt5 import QtWidgets


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        container = QtWidgets.QVBoxLayout()

        hobby_box = QtWidgets.QGroupBox("Hobby")
        v_layout = QtWidgets.QVBoxLayout()
        btn1 = QtWidgets.QRadioButton('Smoke')
        btn2 = QtWidgets.QRadioButton('Fire')
        btn3 = QtWidgets.QRadioButton('Drunk')
        v_layout.addWidget(btn3)
        v_layout.addWidget(btn2)
        v_layout.addWidget(btn1)
        hobby_box.setLayout(v_layout)

        gender_box=QtWidgets.QGroupBox("Gender")
        h_layout=QtWidgets.QHBoxLayout()
        btn4=QtWidgets.QRadioButton('male')
        btn5=QtWidgets.QRadioButton('female')
        h_layout.addWidget(btn4)
        h_layout.addWidget(btn5)
        gender_box.setLayout(h_layout)

        container.addWidget(hobby_box)
        container.addWidget(gender_box)

        self.setLayout(container)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec_()
