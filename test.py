import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from MangoUI import Button
from MangoUI import Canvas

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.width = 800
        self.height = 600
        screenSizeX = 1920
        screenSizeY = 1080
        self.xPos = int((screenSizeX/2) - (self.width/2))
        self.yPos = -800
        self.initUI()

    def initUI(self):
        self.setGeometry(self.xPos, self.yPos, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.setWindowTitle('Test Window')
        self.setStyleSheet(f'''
            background-color: rgb(255, 255, 255);
        ''')

        self.clearButton = Button(self)
        self.clearButton.move(20, 20)
        self.clearButton.resize(100, 30)
        self.clearButton.setText('Clear')
        self.clearButton.clicked.connect(self.clearCanvas)
        self.clearButton.setPrimaryColor((0, 0, 51))
        self.clearButton.setSecondaryColor((204, 204, 255))
        self.clearButton.setParentBackgroundColor((255, 255, 255))
        self.clearButton.setBorder(borderRadius = 9)

        self.canvas = Canvas(self, width = 450, height = 450, canvasColor = (230, 230, 255))
        self.canvas.move(300, 20)

        self.show()

    def clearCanvas(self):
        self.canvas.clearCanvas()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = Window()
    sys.exit(app.exec_())