# -*- coding: utf-8 -*-
import random
from Shape import *

Col = 10
Row = 22


class ShapeManager:
    def __init__(self, signal):
        self.signal = signal
        self.curX = 0
        self.curY = 0
        self.curShape = Shape()  # 当前Shape
        self.isCurShapeDropped = False  # 当前shape是否落下完成
        self.board = []  # 游戏区域  Col * Row

        self.num_lines_removed = 0   # 消除的行数

        self.clear_board()

    def clear_board(self):
        for i in range(Col*Row):
            self.board.append(NoShape)

    # 获得指定位置的方块
    def get_block(self, x, y):
        return self.board[y*Col + x]

    def set_block(self, x, y, shape_type):
        self.board[y*Col + x] = shape_type

    def create_shape(self):
        self.curShape.set_shape(random.randint(1, 7))
        self.curX = Col//2 + 1
        self.curY = Row - 1 + self.curShape.get_minY()
        if not self.move_shape(self.curShape, self.curX, self.curY):
            self.curShape.set_shape(NoShape)

    def move_shape(self, new_shape, new_x, new_y):
        for i in range(BlockNum):
            x = new_x + new_shape.coordinates[i][0]
            y = new_y - new_shape.coordinates[i][1]

            # 检查 边界
            if x < 0 or x >= Col or y < 0 or y >= Row:
                return False

            # 检查 是否有其它 方块
            if self.get_block(x, y) != NoShape:
                return False

            # 可以移动
        self.curShape = new_shape
        self.curX = new_x
        self.curY = new_y

        self.signal.emit() # 给界面发个自定义消息

        return True

    # 下落一行
    def down_one_line(self):
        if not self.move_shape(self.curShape, self.curX, self.curY - 1):
            self.process_dropped()

    # 下落到底
    def down_end(self):
        newY = self.curY

        while newY > 0:
            if not self.move_shape(self.curShape, self.curX, self.curY - 1):
                break
            newY -= 1
        self.process_dropped()

    # 落到最下面后的处理
    def process_dropped(self):
        for i in range(BlockNum):
            x = self.curX + self.curShape.coordinates[i][0]
            y = self.curY - self.curShape.coordinates[i][1]
            self.set_block(x, y, self.curShape.theShape)
        self.remove_lines()

    def remove_lines(self):
        num_full_lines = 0
        row_to_remove = []  # 保存需要消除的行号

        for i in range(Row):
            n = 0
            for j in range(Col):
                if self.get_block(j, i) != NoShape:
                    n += 1
            if n == Col:
                row_to_remove.append(i)
        for m in row_to_remove:
            for i in range(Row):
                for j in range(Col):
                    self.set_block(j, i, self.get_block(j, i + 1))  # 把上面一行的赋值给下面。

        num_full_lines = num_full_lines + len(row_to_remove)

        if num_full_lines > 0:
            self.num_lines_removed += num_full_lines
            self.signal.emit()

        # 再创建个新shape
        self.create_shape()







            