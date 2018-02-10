# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.uic import loadUi
import cv2
from ui_test import Ui_MainWindow



class TestUI(QMainWindow, Ui_MainWindow):
    frame_signal = pyqtSignal(QImage)

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)




        self.__video_thread = VideoThread("rtsp://172.16.1.87", self.frame_signal)
        self.__video_thread.start()



        #loadUi("test.ui", self)
        # btn = QPushButton(self)
        # lbl = QLabel(self)
        # self.setMouseTracking(True)
        #
        #
        # #self.label.mouseReleaseEvent.connect(self.mouseClick_label)
        #
        self.frame_signal.connect(self.video_play)
        # self.pushButton.clicked.connect(self.mouseClick_label)
        self.ui.label.clicked.connect(self.mouseClick_label)

        self.move(100, 100)
        self.show()


    def mouseClick_label(self, event):
        print(event.pos())
        print(360/self.ui.label.height())

        x = event.pos().x() * 480/self.ui.label.width()
        y = event.pos().y() * 360/self.ui.label.height()
        print(y)
        self.__video_thread.list_point.append((int(x), int(y)))



    def video_play(self, sender):
        pixmap = QPixmap().fromImage(sender)
        pixmap2 = pixmap.scaled(self.ui.label.width(), self.ui.label.height())

        self.ui.label.setPixmap(pixmap2)
        self.ui.label_2.setPixmap(pixmap)



class VideoThread(QThread):
    def __init__(self, video_url, sig):
        super().__init__()
        self.__video_url = video_url
        self.__sig = sig
        self.list_point = []


    def run(self):

        video_capture = cv2.VideoCapture(self.__video_url)
        success, frame = video_capture.read()
        while success:
            frame = cv2.resize(frame, (480, 360))

            last_point = None
            if len(self.list_point) >= 1:
                last_point = self.list_point[0]
            for point in self.list_point:
                if point != last_point:
                    cv2.line(frame, last_point, point, (255, 0, 0), 5)
                    last_point = point
            height, width, fps = frame.shape
            bytesPerLine = 3*width
            cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)
            #cv2.line()
            image = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
            #image = QImage("pen.ico")
            success, frame = video_capture.read()
            self.__sig.emit(image)








if __name__ == "__main__":
    app = QApplication(sys.argv)

    test_ui = TestUI()

    sys.exit(app.exec_())