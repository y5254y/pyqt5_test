import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon



class MyWidge(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()


	def initUI(self):
		btn = QPushButton(QIcon("pen.ico"), "zk", self)
		btn.setToolTip("test tooltip")
		btn.setGeometry(50, 50, 50, 50)
		#btn.move(50, 50)



		self.setGeometry(20, 20, 200, 200)
		self.setWindowTitle("icon test")
		self.setWindowIcon(QIcon("pen.ico"))
		self.show()



if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = MyWidge()
	sys.exit(app.exec_())
