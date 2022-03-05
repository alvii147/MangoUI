import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtCore import Qt, QEasingCurve

from MangoUI import Slider

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.width = 500
        self.height = 500
        self.xPos = 600
        self.yPos = 400
        self.initUI()

    def initUI(self):
        self.setGeometry(self.xPos, self.yPos, self.width, self.height)
        self.vBoxLayout = QVBoxLayout()

        self.slider = Slider(
            slideDirection = Qt.Orientation.Horizontal,
            animationType = QEasingCurve.Type.OutQuad,
            animationDuration = 750,
            wrapAround = False,
        )

        self.label1 = QLabel()
        self.label1.setText('First Slide')
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label1.setStyleSheet('QLabel{background-color: rgb(245, 177, 66); color: rgb(21, 21, 21); font: 25pt;}')
        self.slider.addWidget(self.label1)

        self.label2 = QLabel()
        self.label2.setText('Second Slide')
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label2.setStyleSheet('QLabel{background-color: rgb(21, 21, 21); color: rgb(245, 177, 66); font: 25pt;}')
        self.slider.addWidget(self.label2)

        self.label3 = QLabel()
        self.label3.setText('Third Slide')
        self.label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label3.setStyleSheet('QLabel{background-color: rgb(93, 132, 48); color: rgb(245, 177, 66); font: 25pt;}')
        self.slider.addWidget(self.label3)

        self.buttonPrevious = QPushButton()
        self.buttonPrevious.setText('Previous Slide')
        self.buttonPrevious.clicked.connect(self.slider.slidePrevious)

        self.buttonNext = QPushButton()
        self.buttonNext.setText('Next Slide')
        self.buttonNext.clicked.connect(self.slider.slideNext)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.buttonPrevious)
        self.buttonLayout.addWidget(self.buttonNext)

        self.vBoxLayout.addWidget(self.slider)
        self.vBoxLayout.addLayout(self.buttonLayout)

        self.centralWidget = QWidget(self)
        self.centralWidget.setLayout(self.vBoxLayout)
        self.setCentralWidget(self.centralWidget)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = Window()
    sys.exit(app.exec())