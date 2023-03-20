import sys

import PyQt5

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()

    w.setWindowTitle('QLabel')

    label = QLabel("Message", w)

    label.setGeometry(20,0,300,300)
    w.show()

    app.exec_()
