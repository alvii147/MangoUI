![QSharpTools Logo](img/MangoUILogoLight.png)

# Overview

**Mango.UI** is a library for **PyQt5** that includes sharper-looking custom-styled widgets for better desktop UI development.

# Button

**Button** an inherited class of **QPushButton,** styled using **QSS** and **QVariantAnimation.**

## Example Use

```python
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
```
<img src="img/ButtonExample.gif" alt="ButtonExample" width="200"/>

## Constructors & Methods

- [Button()](#button-1)
- [setPrimaryColor()](#setprimarycolor)
- [setSecondaryColor()](#setsecondarycolor)
- [setParentBackgroundColor()](#setparentbackgroundcolor)
- [setFont()](#setfont)
- [setBorder()](#setborder)

## Button()

```python
Button(parent = None,
       primaryColor = (21, 21, 21, 255),
       secondaryColor = (245, 177, 66, 255),
       parentBackgroundColor = (240, 240, 240, 255),
       fontFamily = 'Verdana',
       fontSize = 8,
       fontWeight = 'normal',
       borderStyle = 'solid',
       borderWidth = 1,
       borderRadius = 2,
```

**Parameters:**

- *primaryColor:*
  - [QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) object, RGBA tuple, RGBA unsigned 32-bit integer, or RGBA string
  - Normal text color and background color on hover
- *secondaryColor:*
  - [QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) object, RGBA tuple, RGBA unsigned 32-bit integer, or RGBA string
  - Normal background color and the text color on hover
- *parentBackgroundColor:*
  - [QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) object, RGBA tuple, RGBA unsigned 32-bit integer, or RGBA string
  - Needed to apply a size change effect when clicked
- *fontFamily:*
  - string representing name of font family
- *fontSize:*
  - integer representing font size
- *fontWeight:*
  - string representing font weight
- *borderStyle:*
  - string representing border style
- *borderWidth:*
  - integer representing border width
- *borderRadius*
  - integer representing border radius

## setPrimaryColor()

**Return type:** bool

**Parameters:**

- *color:* [QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) object, RGBA tuple, RGBA unsigned 32-bit integer, or RGBA string

**Description:** set primary color.

## setSecondaryColor()

**Return type:** bool

**Parameters:**

- *color:* [QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) object, RGBA tuple, RGBA unsigned 32-bit integer, or RGBA string

**Description:** set secondary color.

## setParentBackgroundColor()

**Return type:** bool

**Parameters:**

- *color:* [QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) object, RGBA tuple, RGBA unsigned 32-bit integer, or RGBA string

**Description:** set background color of parent widget.

## setFont()

**Return type:** bool

**Parameters:**

- *fontFamily = None:* string representing name of font family
- *fontSize = None:* integer representing font size
- *fontWeight = None:* string representing font weight

**Description:** set font properties.

## setBorder()

**Return type:** bool

**Parameters:**

- *borderStyle = None:* string representing border style
- *borderWidth = None:* integer representing border width
- *borderRadius = None:* integer representing border radius

**Description:** set border properties.

# Canvas

**Canvas** an inherited class of **QLabel** with a null **QPixmap.** Using **QPainter,** **Canvas** allows the user to draw on the window.

## Example Use

```python
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from MangoUI import Canvas

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
```

<img src="img/CanvasExample.gif" alt="Canvas Example" width="200"/>

## Constructors & Methods

- [Canvas()](#canvas-1)
- [setPenColor()](#setpencolor)
- [setBorder()](#setborder-1)
- [saveCanvas()](#savecanvas)
- [clearCanvas()](#clearcanvas)

## Canvas()

```python
Canvas(parent = None,
       width = 200,
       height = 200,
       penColor = (25, 25, 25, 255),
       canvasColor = (255, 247, 242, 255),
       strokeStyle = Qt.SolidLine,
       strokeWidth = 3,
       borderStyle = 'solid',
       borderColor = (0, 0, 0, 255),
       borderWidth = 1,
```

**Parameters:**

- *width:*
  - Width of canvas
- *height:*
  - Height of canvas
- *penColor:*
  - [QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) object, RGBA tuple, RGBA unsigned 32-bit integer, or RGBA string
  - Color of pen
- *canvasColor:*
  - [QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) object, RGBA tuple, RGBA unsigned 32-bit integer, or RGBA string
  - Background color of canvas
- *strokeStyle:*
  - [QPenStyle](https://doc.qt.io/qtforpython-5.12/PySide2/QtGui/QPen.html#pen-style) object
  - Line style of pen stroke
- *strokeWidth:*
  - integer representing pen stroke width
- *borderStyle:*
  - string representing border style
- *borderColor*
  - [QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) object, RGBA tuple, RGBA unsigned 32-bit integer, or RGBA string
  - Color of canvas border
- *borderWidth:*
  - integer representing border width

## setPenColor()

**Return type:** bool

**Parameters:**

- *color:* [QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) object, RGBA tuple, RGBA unsigned 32-bit integer, or RGBA string

**Description:** set pen color.

## setBorder()

**Return type:** bool

**Parameters:**

- *borderStyle = None:* string representing border style
- *borderColor = None:* [QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) object, RGBA tuple, RGBA unsigned 32-bit integer, or RGBA string, representing canvas border color
- *borderWidth = None:* integer representing border width

**Description:** set border properties.

## saveCanvas()

**Return type:** bool

**Parameters:**

- *dest:* string representing file destination

**Description:** save canvas to image file.

## clearCanvas()

**Return type:** bool

**Description:** clear canvas drawing.