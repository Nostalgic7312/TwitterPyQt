import sys

import PyQt5

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()

    w.setWindowTitle('Button')

    btn = QPushButton('Button')

    btn.setParent(w)

    w.show()

    app.exec_()
