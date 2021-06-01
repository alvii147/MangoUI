import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

from MangoUI import Canvas

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.width = 150
        self.height = 150
        self.xPos = 600
        self.yPos = 400
        self.initUI()

    def initUI(self):
        self.setGeometry(self.xPos, self.yPos, self.width, self.height)
        self.vBoxLayout = QVBoxLayout()

        self.canvas = Canvas(
            width = 150,
            height = 150,
            penColor = (21, 21, 21),
            canvasColor = (245, 177, 66),
            strokeWidth = 5,
            borderWidth = 2,
            borderColor = (21, 21, 21)
        )
        self.vBoxLayout.addWidget(self.canvas, alignment = Qt.AlignCenter)

        self.centralWidget = QWidget(self)
        self.centralWidget.setLayout(self.vBoxLayout)
        self.setCentralWidget(self.centralWidget)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = Window()
    sys.exit(app.exec_())