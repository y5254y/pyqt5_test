# -*- coding: utf-8 -*-

BlockNum = 4



NoShape = 0

"""
   .
 . .
 .
"""
ZShape = 1

"""
  .
  . .
    .
"""
SShape = 2
LineShape = 3

"""
   .
 . . .
"""
TShape = 4
SquareShape = 5
"""
 .
 .
 . .
"""
LShape = 6

"""
   .
   .
 . .
"""
MirroredLShape = 7


class Shape:
    coordinates_table = (
        ((0, 0), (0, 0), (0, 0), (0, 0)),
        ((0, -1), (0, 0), (-1, 0), (-1, 1)),
        ((0, -1), (0, 0), (1, 0), (1, 1)),
        ((0, -1), (0, 0), (0, 1), (0, 2)),
        ((-1, 0), (0, 0), (1, 0), (0, 1)),
        ((0, 0), (1, 0), (0, 1), (1, 1)),
        ((-1, -1), (0, -1), (0, 0), (0, 1)),
        ((1, -1), (0, -1), (0, 0), (0, 1))
    )

    def __init__(self):
        self.coordinates = [[0, 0] for i in range(BlockNum)]
        self.theShape = NoShape

    def set_shape(self, shape):
        table = Shape.coordinates_table[shape]
        for i in range(BlockNum):
            for j in range(2):
                self.coordinates[i][j] = table[i][j]
        self.theShape = shape

    def get_minX(self):
        the_value = self.coordinates[0][0]
        for i in range(BlockNum):
            the_value = min(the_value, self.coordinates[i][0])

        return the_value

    def get_maxX(self):
        the_value = self.coordinates[0][0]
        for i in range(BlockNum):
            the_value = max(the_value, self.coordinates[i][0])

        return the_value

    def get_minY(self):
        the_value = self.coordinates[0][1]
        for i in range(BlockNum):
            the_value = min(the_value, self.coordinates[i][1])

        return the_value

    def get_maxY(self):
        the_value = self.coordinates[0][1]
        for i in range(BlockNum):
            the_value = max(the_value, self.coordinates[i][1])

        return the_value

    # 每次都左向（顺时针）转动
    # 每个小方格x为原来的y, y为原来的-x
    def rotate(self):
        if self.theShape == NoShape:
            return self

        result = Shape()
        result.theShape = self.theShape

        for i in range(BlockNum):
            result.coordinates[i][0] = self.coordinates[i][1]
            result.coordinates[i][1] = -self.coordinates[i][0]
        return result






