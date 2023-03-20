import sys

from PyQt5 import QtWidgets

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(600,600)
        menu=self.menuBar()

        file_menu=menu.addMenu('File')
        file_menu.addAction('New')
        file_menu.addAction('Open')
        file_menu.addAction('Save')

        edit_menu=menu.addMenu('Edit')
        edit_menu.addAction('Copy')
        edit_menu.addAction('V')
        edit_menu.addAction('X')


        label=QtWidgets.QLabel("HelloWorld")
        label.setStyleSheet('font-size:30px;font-weight:400;')
        label.setGeometry(300,300,100,100)

        self.setCentralWidget(label)
        # self.setCentralWidget(layout)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    # w=QtWidgets.QWidget()
    #
    # w.show()

    w = MyWindow()

    w.show()
    app.exec_()
