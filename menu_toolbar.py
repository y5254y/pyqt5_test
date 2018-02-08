# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QMenu
from PyQt5.QtGui import QIcon


class MyWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # exitAct = QAction(QIcon("pen.ico"), "&Exit", self)
        # exitAct.setShortcut("Ctrl+Q")
        # exitAct.setStatusTip("退出")
        # exitAct.triggered.connect(qApp.quit)
        #
        # menubar = self.menuBar()
        # menubar.addMenu("&File")
        # menubar.addAction(exitAct)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        newAct = QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)


        self.statusBar().showMessage("准备..")
        #self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("statusbar")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    wnd = MyWindows()

    sys.exit(app.exec_())