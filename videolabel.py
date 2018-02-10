# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtGui

class VideoLabel(QLabel):
    clicked = pyqtSignal(QtGui.QMouseEvent)
    def __init__(self, parent):
        super().__init__(parent)

    def mouseMoveEvent(self, ev: QtGui.QMouseEvent):
        pass
    def mousePressEvent(self, event):
        self.clicked.emit(event)

