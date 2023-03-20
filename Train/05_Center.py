import sys

import PyQt5

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()

    w.setWindowTitle('input')

    label = QLabel('Count', w)
    label.setGeometry(20, 20, 60, 20)

    QLineEdit = QLineEdit(w)
    QLineEdit.setPlaceholderText("Please Input Count")
    QLineEdit.setGeometry(80, 20, 300, 20)

    btn = QPushButton('Commit', w)
    btn.setGeometry(145, 100, 70, 20)

    w.resize(1000, 1000)

    w.move(0, 0)

    center_pointer = QtWidgets.QDesktopWidget().availableGeometry().center()
    x = center_pointer.x()
    y = center_pointer.y()
    # w.move(x-500, y-500)

    w_x, w_y, width, height = w.frameGeometry().getRect()

    w.move(int(x - width / 2), int(y - height / 2))

    w.show()

    app.exec_()
