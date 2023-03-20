import sys

from PyQt5 import QtWidgets


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Calculator")
        data = {
            0: ['7', '8', '9', '+', '('],
            1: ['4', '5', '6', '-', ')'],
            2: ['1', '2', '3', '*', '<-'],
            3: ['0', '.', '=', '/', 'C']
        }

        layout = QtWidgets.QVBoxLayout()

        edit = QtWidgets.QLineEdit()
        edit.setPlaceholderText("Please")
        layout.addWidget(edit)

        grid_layout = QtWidgets.QGridLayout()
        for line_number,line_data in data.items():
            for col_number,number in enumerate(line_data):
                btn=QtWidgets.QPushButton(number)
                grid_layout.addWidget(btn,line_number,col_number)


        layout.addLayout(grid_layout)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec_()
