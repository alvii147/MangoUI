import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPalette
from QSharpTools import SharpButton, SharpCanvas

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.width = 800
        self.height = 600
        screenSizeX = 1920
        screenSizeY = 1080
        self.xPos = int((screenSizeX/2) - (self.width/2))
        self.yPos = int((screenSizeY/2) - (self.height/2))
        self.initUI()

    def initUI(self):
        self.setGeometry(self.xPos, self.yPos, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.setWindowTitle("Test Window")

        self.button = SharpButton(self)
        self.button.move(100, 100)
        self.button.setText("Copy")
        self.button.clicked.connect(self.sayHello)

        self.normalButton = QPushButton(self)
        self.normalButton.move(200, 200)
        self.normalButton.setText("IDK")

        self.can = SharpCanvas(self)
        self.can.move(100, 100)
        self.can.resize(200, 200)

        self.show()

    def sayHello(self):
        print("button pressed")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = Window()
    sys.exit(app.exec_())