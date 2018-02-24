# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
import sys
from GameView import *
#from ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

       # self.ui = Ui_MainWindow()
        #self.ui.setupUi(self)
        self.view = GameView(self)
        self.setCentralWidget(self.view)
        self.view.start_game()

        self.resize(180, 380)
        # 窗体居中显示
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,
            (screen.height()-size.height())/2)
        self.show()


app = QApplication(sys.argv)
test = MainWindow()
sys.exit(app.exec_())