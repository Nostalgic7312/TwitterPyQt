import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSettings
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMenuBar, QMenu,
                             QAction, QPlainTextEdit, QStyle, QFileDialog,
                             QMessageBox, QToolBar, QStatusBar, QLabel)


class DemoNotepad(QMainWindow):
    def __init__(self, parent=None):
        super(DemoNotepad, self).__init__(parent)
        # 设置窗口标题
        self.setWindowTitle('实战 Qt for Python: QSettings 演示-记事本')
        # 设置窗口大小
        self.resize(480, 360)
        self.path = None
        self.initUi()

    def initUi(self):

        # 设置一个文本编辑器作为中心小部件
        self.txtEditor = QPlainTextEdit(self)
        self.setCentralWidget(self.txtEditor)
        self.initRecentFileList()
        # 创建菜单条和工具条使用的Action
        self.initActions()
        # 初始化菜单条
        self.initMenuBar()
        # 初始化化工具条
        self.initToolBar()
        # 初始化状态条
        self.initStatusBar()

    def initActions(self):
        style = QApplication.style()

        # 新建文件
        self.aFileNew = QAction('新建(&N)', self)
        # 添加一个图标
        self.aFileNew.setIcon(style.standardIcon(QStyle.SP_FileIcon))
        # 添加快捷键
        self.aFileNew.setShortcut(Qt.CTRL + Qt.Key_N)
        self.aFileNew.setToolTip('新建一个文本文件')
        # self.aFileNew.setStatusTip('test')
        self.aFileNew.triggered.connect(self.onFileNew)

        # 打开文件
        self.aFileOpen = QAction('打开(&O)...', self)
        self.aFileOpen.setIcon(style.standardIcon(QStyle.SP_DialogOpenButton))
        self.aFileOpen.setShortcut(Qt.CTRL + Qt.Key_O)
        self.aFileOpen.setToolTip('打开一个文本文件')
        self.aFileOpen.triggered.connect(self.onFileOpen)

        # 保存
        self.aFileSave = QAction('保存(&S)', self)
        self.aFileSave.setIcon(style.standardIcon(QStyle.SP_DialogSaveButton))
        self.aFileSave.setShortcut(Qt.CTRL + Qt.Key_S)
        self.aFileSave.setToolTip('保存文本文件')
        self.aFileSave.triggered.connect(self.onFileSave)

        # 另存为
        self.aFileSaveAs = QAction('另存为(&A)...', self)
        self.aFileSaveAs.triggered.connect(self.onFileSaveAs)

        # 退出
        self.aFileExit = QAction('退出(&X)', self)
        self.aFileExit.triggered.connect(self.close)

        # 撤销编辑
        self.aEditUndo = QAction('撤销(&U)', self)
        self.aEditUndo.setShortcut(Qt.CTRL + Qt.Key_Z)
        self.aEditUndo.triggered.connect(self.txtEditor.undo)

        # 恢复编辑
        self.aEditRedo = QAction('恢复(&R)', self)
        self.aEditRedo.setShortcut(Qt.CTRL + Qt.Key_Y)
        self.aEditUndo.triggered.connect(self.txtEditor.redo)

        # 剪切操作
        self.aEditCut = QAction('剪切(&T)', self)
        self.aEditCut.setShortcut(Qt.CTRL + Qt.Key_X)
        self.aEditCut.triggered.connect(self.txtEditor.cut)

        # 复制操作
        self.aEditCopy = QAction('复制(&C)', self)
        self.aEditCopy.setShortcut(Qt.CTRL + Qt.Key_C)
        self.aEditCopy.triggered.connect(self.txtEditor.copy)

        # 粘贴操作
        self.aEditPaste = QAction('粘贴(&P)', self)
        self.aEditPaste.setShortcut(Qt.CTRL + Qt.Key_V)
        self.aEditPaste.triggered.connect(self.txtEditor.paste)

        # 删除操作
        self.aEditDel = QAction('删除(&L)', self)
        self.aEditDel.setShortcut(Qt.Key_Delete)
        self.aEditDel.triggered.connect(self.onEditDelete)

        # 全选操作
        self.aEditSelectAll = QAction('全选(&A)', self)
        self.aEditSelectAll.setShortcut(Qt.CTRL + Qt.Key_A)
        self.aEditSelectAll.triggered.connect(self.txtEditor.selectAll)

        self.aFmtAutoLine = QAction('自动换行(&W)', self)
        self.aFmtAutoLine.setCheckable(True)
        self.aFmtAutoLine.setChecked(True)
        self.aFmtAutoLine.triggered[bool].connect(self.onFormatAutoLine)

        self.aHelpAbout = QAction('关于(&A)...', self)
        self.aHelpAbout.triggered.connect(self.onHelpAbout)

    def initMenuBar(self):
        menuBar = self.menuBar()
        self.fileMenu = menuBar.addMenu('文件(&F)')
        editMenu = menuBar.addMenu('编辑(&E)')
        formatMenu = menuBar.addMenu('格式(&O)')
        helpMenu = menuBar.addMenu('帮助(&H)')

        # ==== 文件操作部分 ==== #
        self.fileMenu.addAction(self.aFileNew)
        self.fileMenu.addAction(self.aFileOpen)
        self.fileMenu.addAction(self.aFileSave)
        self.fileMenu.addAction(self.aFileSaveAs)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.aFileExit)

        self.updateRecentFileMenu()

        # ==== 编辑部分 ==== #
        editMenu.addAction(self.aEditUndo)
        editMenu.addAction(self.aEditRedo)
        editMenu.addSeparator()
        editMenu.addAction(self.aEditCut)
        editMenu.addAction(self.aEditCopy)
        editMenu.addAction(self.aEditPaste)
        editMenu.addAction(self.aEditDel)
        editMenu.addSeparator()
        editMenu.addAction(self.aEditSelectAll)
        # 当编辑栏的菜单对象被点击时, 在状态栏显示信息
        editMenu.triggered[QAction].connect(self.onProcessTrigger)

        # ==== 格式设置部分 ==== #
        formatMenu.addAction(self.aFmtAutoLine)

        # ==== 帮助部分 ==== #
        helpMenu.addAction(self.aHelpAbout)

    def initToolBar(self):
        toolBar = self.addToolBar('')
        toolBar.addAction(self.aFileNew)
        toolBar.addAction(self.aFileOpen)
        toolBar.addAction(self.aFileSave)

    def initStatusBar(self):
        self.statusBar = QStatusBar(self)
        # 添加一个显示永久信息的标签控件
        self.info = QLabel(self)
        self.info.setText('实战 Qt for Python')
        self.info.setAlignment(Qt.AlignRight)
        self.statusBar.addPermanentWidget(self.info)
        self.setStatusBar(self.statusBar)

    def msgCritical(self, strInfo):
        dlg = QMessageBox(self)
        dlg.setIcon(QMessageBox.Critical)
        dlg.setText(strInfo)
        dlg.show()

    def onFileNew(self):
        self.txtEditor.clear()

    def onFileOpen(self):
        path, _ = QFileDialog.getOpenFileName(self, '打开文件', '', '文本文件 (*.txt)')
        if path:
            if self.loadFile(path):
                # 添加到最近打开的菜单列表中
                self.updateRecentFiles(path)

    # 加载文件
    def loadFile(self, path):
        try:
            with open(path, 'r') as f:
                text = f.read()
        except Exception as e:
            self.msgCritical(str(e))
            return False
        else:
            self.path = path
            self.txtEditor.setPlainText(text)
            self.statusBar.showMessage('打开文件 ' + path, 5000)
            return True

    def onFileSave(self):
        if self.path is None:
            return self.onFileSaveAs()
        self._saveToPath(self.path)

    def onFileSaveAs(self):
        path, _ = QFileDialog.getSaveFileName(self, '保存文件', '', '文本文件 (*.txt)')
        if not path:
            return
        self._saveToPath(path)

    def _saveToPath(self, path):
        text = self.txtEditor.toPlainText()
        try:
            with open(path, 'w') as f:
                f.write(text)
        except Exception as e:
            self.msgCritical(str(e))
        else:
            self.path = path

    def onEditDelete(self):
        tc = self.txtEditor.textCursor()
        # tc.select(QtGui.QTextCursor.BlockUnderCursor) 这样删除一行
        tc.removeSelectedText()

    def onFormatAutoLine(self, autoLine):
        if autoLine:
            self.txtEditor.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        else:
            self.txtEditor.setLineWrapMode(QPlainTextEdit.NoWrap)

    def onHelpAbout(self):
        QMessageBox.information(self, '实战 Qt for Python', 'PyQt5实现的文本编辑器演示版')

    def onProcessTrigger(self, action):
        self.statusBar.showMessage(action.text() + ' 菜单项被点击了', 3000)

    # 初始化最近文件列表信息
    def initRecentFileList(self):
        # 创建一个配置对象
        # 方式一：
        # self.settings = QSettings('Qt-for-Python', 'My notePad')
        # 方式二：
        self.settings = QSettings('config.ini', QSettings.IniFormat)

        # 加载最近文件
        self.recentFiles = self.settings.value('FileList/recentFiles') or []

        # 添加最近文件菜单行为
        self.maxNumRecentFiles = 4  # 最多四个最近的文件
        self.recentFileActions = []
        for i in range(self.maxNumRecentFiles):
            self.recentFileActions.append(QAction(self))

    # 更新最近文件列表菜单
    def updateRecentFileMenu(self):
        # 先移除添加的行为
        for action in self.recentFileActions:
            self.fileMenu.removeAction(action)

        # 移除退出菜单项
        self.fileMenu.removeAction(self.aFileExit)
        # 移除多余的

        # 最近文件
        for i, fname in enumerate(self.recentFiles):
            action = self.recentFileActions[i]
            action.setText(fname)
            action.setToolTip('最近打开的文件')
            action.setData(fname)  # 保存数据
            action.triggered.connect(self.loadRecentFile)
            self.fileMenu.addAction(action)

        # 恢复退出菜单项
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.aFileExit)

    # 更新最近文件
    def updateRecentFiles(self, fname):
        if fname not in self.recentFiles:
            self.recentFiles.insert(0, fname)
            if len(self.recentFiles) > self.maxNumRecentFiles:
                self.recentFiles.pop()

            # 更新菜单
            self.updateRecentFileMenu()

            # 保存更新后最近菜单列表
            self.settings.setValue('FileList/recentFiles', self.recentFiles)

    def loadRecentFile(self):
        sender = self.sender()
        if isinstance(sender, QAction):
            fname = sender.data()  # 取出保存的数据
            self.loadFile(fname)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoNotepad()
    window.show()
    sys.exit(app.exec())