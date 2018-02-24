# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QFrame, QApplication
from PyQt5.QtCore import QBasicTimer, Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QColor
import sys
from ShapeManager import *


class GameView(QFrame):
    update_signal = pyqtSignal()
    def __init__(self, parent):
        super().__init__(parent)

        self.is_start = False
        self.is_pause = False
        self.speed = 150   # ms  , 定时器内处理下落，每speed ms 处理一次
        self.timer = QBasicTimer()

        self.shape_manger = ShapeManager(self.update_signal)

        self.update_signal.connect(self.update_ui)


    def update_ui(self):
        self.update()

    def start_game(self):
        if self.is_pause:
            return
        self.is_start = True

        self.shape_manger.create_shape()
        self.timer.start(self.speed, self)

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.shape_manger.down_one_line()
        else:
            super(GameView, self).timerEvent(event)

    def keyPressEvent(self, event):
        if not self.is_start or self.shape_manger.curShape == NoShape:
            super(GameView, self).keyPressEvent(event)
            return
        key = event.key()

        if key == Qt.Key_P:
            self.is_pause = not self.is_pause
            return
        if self.is_pause:
            return
        if key == Qt.Key_Right:
            pass
        if key == Qt.Key_Left:
            pass

    def paintEvent(self, event):
        painter = QPainter(self)

        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]




        # 游戏区域大小
        rect = self.contentsRect()

        # 组成Shpae的方块的大小
        block_width = self.contentsRect().width()//Col
        block_height = self.contentsRect().height()//Row

        # 画游戏区现有的
        for i in range(Row):
            for j in range(Col):
                shape = self.shape_manger.get_block(j, i)
                if shape != NoShape:
                    color = QColor(colorTable[shape])
                    painter.fillRect(rect.left() + j*block_width,
                                    rect.bottom() - i*block_height, block_width, block_height, color)

        # 画当前的shape
        if self.shape_manger.curShape.theShape != NoShape:
            for i in range(BlockNum):
                x = self.shape_manger.curX + self.shape_manger.curShape.coordinates[i][0]
                y = self.shape_manger.curY + self.shape_manger.curShape.coordinates[i][1]
                color = QColor(colorTable[self.shape_manger.curShape.theShape])
                painter.fillRect(rect.left() + x * block_width,
                                 rect.bottom() - y * block_height, block_width, block_height, color)










if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = GameView(None)
    test.start_game()


    sys.exit(app.exec_())