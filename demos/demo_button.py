import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout
from MangoUI import Button

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.width = 150
        self.height = 150
        self.xPos = 500
        self.yPos = 500
        self.initUI()

    def initUI(self):
        self.setGeometry(self.xPos, self.yPos, self.width, self.height)
        self.vBoxLayout = QVBoxLayout()
        
        self.button = Button(
            borderWidth = 1,
            borderRadius = 4,
        )
        self.button.setText('Default Button')
        self.vBoxLayout.addWidget(self.button)

        self.blueButton = Button(
            primaryColor  = (17, 46, 133),
            secondaryColor = (202, 209, 232),
            borderWidth = 1,
            borderRadius = 4,
        )
        self.blueButton.setText('Blue Button')
        self.vBoxLayout.addWidget(self.blueButton)

        self.redButton = Button(
            primaryColor  = (171, 3, 3),
            secondaryColor = (247, 173, 173),
            borderWidth = 1,
            borderRadius = 4,
        )
        self.redButton.setText('Red Button')
        self.vBoxLayout.addWidget(self.redButton)

        self.centralWidget = QWidget(self)
        self.centralWidget.setLayout(self.vBoxLayout)
        self.setCentralWidget(self.centralWidget)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = Window()
    sys.exit(app.exec_())