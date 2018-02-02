import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton(QIcon("pen.ico"), "zk", self)
        # 事件绑定
        # btn.clicked.connect(QCoreApplication.instance().quit)

        btn.setToolTip("test tooltip")
        btn.setGeometry(50, 50, 50, 50)
        # btn.move(50, 50)
        # 居中
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


        #self.setGeometry(20, 20, 200, 200)
        self.setWindowTitle("icon test")
        self.setWindowIcon(QIcon("pen.ico"))
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Message", "要退出吗？", QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())
