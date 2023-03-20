import sys

import PyQt5

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

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
    btn.setGeometry(145,100,70,20)

    w.show()

    app.exec_()