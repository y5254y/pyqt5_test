# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.uic import loadUi
import cv2


class TestUI(QMainWindow):
    frame_signal = pyqtSignal(QImage)
    def __init__(self):
        super().__init__()
        video_thread = VideoThread("rtsp://172.16.1.87", self.frame_signal)
        video_thread.start()



        loadUi("test.ui", self)
        #btn = QPushButton(self)
        #lbl = QLabel(self)
        #lbl.setpi

        self.init_signal()


        self.move(100, 100)
        self.show()

    def init_signal(self):
        self.frame_signal.connect(self.video_play)


    def video_play(self, sender):
        pixmap = QPixmap().fromImage(sender)
        pixmap2 = pixmap.scaled(self.label.width(), self.label.height())

        self.label.setPixmap(pixmap2)
        self.label_2.setPixmap(pixmap)



class VideoThread(QThread):
    def __init__(self, video_url, sig):
        super().__init__()
        self.__video_url = video_url
        self.__sig = sig


    def run(self):

        video_capture = cv2.VideoCapture(self.__video_url)
        success, frame = video_capture.read()
        while success:
            frame = cv2.resize(frame, (480, 360))
            height, width, fps = frame.shape
            bytesPerLine = 3*width
            cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)
            image = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
            #image = QImage("pen.ico")
            success, frame = video_capture.read()
            self.__sig.emit(image)








if __name__ == "__main__":
    app = QApplication(sys.argv)

    test_ui = TestUI()

    sys.exit(app.exec_())