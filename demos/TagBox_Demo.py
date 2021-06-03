import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton

from MangoUI import TagBox

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.width = 450
        self.height = 250
        self.xPos = 600
        self.yPos = 400
        self.initUI()

    def initUI(self):
        self.setGeometry(self.xPos, self.yPos, self.width, self.height)
        self.vBoxLayout = QVBoxLayout()
        
        self.tagbox = TagBox()
        self.tagbox.addTag('Homelander')
        self.tagbox.addTag('Queen Maeve')
        self.tagbox.addTag('Black Noir')
        self.tagbox.addTag('Transluscent')
        self.tagbox.addTag('A-Train')
        self.tagbox.addTag('The Deep')
        self.vBoxLayout.addWidget(self.tagbox)

        self.tagEdit = QLineEdit()
        self.vBoxLayout.addWidget(self.tagEdit)

        self.addButton = QPushButton()
        self.addButton.setText('Add New Tag')
        self.addButton.clicked.connect(self.addNewTag)
        self.vBoxLayout.addWidget(self.addButton)

        self.centralWidget = QWidget(self)
        self.centralWidget.setLayout(self.vBoxLayout)
        self.setCentralWidget(self.centralWidget)
        self.show()

    def addNewTag(self):
        self.tagbox.addTag(self.tagEdit.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = Window()
    sys.exit(app.exec_())