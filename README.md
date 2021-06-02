![QSharpTools Logo](img/MangoUILogoLight.png)

# Overview

**Mango.UI** is a library for **PyQt5** that includes sharper-looking custom-styled widgets for better desktop UI development.

<table>
<tr>
	<td>
		<p align="center"><strong>Button</strong></p>
	</td>
	<td>
		<p align="center"><strong>Canvas</strong></p>
	</td>
</tr>
<tr>
    <td>
    	<p align="center"><img src="img/ButtonExample.gif" alt="Button Example" width="200"/></p>
    </td>
    <td>
    	<p align="center"><img src="img/CanvasExample.gif" alt="Canvas Example" width="200"/></p>
    </td>
</tr>
<tr>
	<td>
		<p align="center"><strong>Slider</strong></p>
	</td>
	<td>
		<p align="center"><strong>TagBox</strong></p>
	</td>
</tr>
<tr>
	<td>
		<p align="center"><img src="img/SliderExample.gif" alt="Slider Example" width="300"/></p>
	</td>
	<td>
        <p align="center"><img src="img/TagBoxExample.gif" alt="TagBox Example" width="400"/></p>
	</td>
</tr>
</table>



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
        self.xPos = 600
        self.yPos = 400
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
<img src="img/ButtonExample.gif" alt="Button Example" width="200"/>

## Constructors & Methods

- [Button()](#button-1)
- [setColors()](#setcolor)
- [setFont()](#setfont)
- [setBorder()](#setborder)

## Button()

```python
Button(
    parent = None,
    primaryColor = (21, 21, 21, 255),
    secondaryColor = (245, 177, 66, 255),
    parentBackgroundColor = (240, 240, 240, 255),
    fontFamily = 'Verdana',
    fontSize = 8,
    fontWeight = 'normal',
    borderStyle = 'solid',
    borderWidth = 1,
    borderRadius = 2,
)
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

## setColors()

**Return type:** bool

**Parameters:**

- *primaryColor = None:* [QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) object, RGBA tuple, RGBA unsigned 32-bit integer, or RGBA string
- *secondaryColor = None:* [QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) object, RGBA tuple, RGBA unsigned 32-bit integer, or RGBA string
- *parentBackgroundColor = None:* [QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) object, RGBA tuple, RGBA unsigned 32-bit integer, or RGBA string

**Description:** set button colors.

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
Canvas(
    parent = None,
    width = 200,
    height = 200,
    penColor = (25, 25, 25, 255),
    canvasColor = (255, 247, 242, 255),
    strokeStyle = Qt.SolidLine,
    strokeWidth = 3,
    borderStyle = 'solid',
    borderColor = (0, 0, 0, 255),
    borderWidth = 1,
)
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

# Slider

**Slider** an inherited class of **QStackedWidget** that supports slide navigation between stacked widgets.

## Example Use

```python
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt, QEasingCurve

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
            direction = Qt.Horizontal,
            duration = 750,
            animationType = QEasingCurve.OutQuad,
            wrap = False,
        )

        self.label1 = QLabel()
        self.label1.setText('First Slide')
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setStyleSheet('QLabel{background-color: rgb(245, 177, 66); color: rgb(21, 21, 21); font: 25pt;}')
        self.slider.addWidget(self.label1)

        self.label2 = QLabel()
        self.label2.setText('Second Slide')
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setStyleSheet('QLabel{background-color: rgb(21, 21, 21); color: rgb(245, 177, 66); font: 25pt;}')
        self.slider.addWidget(self.label2)

        self.label3 = QLabel()
        self.label3.setText('Third Slide')
        self.label3.setAlignment(Qt.AlignCenter)
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
    sys.exit(app.exec_())
```

<img src="img/SliderExample.gif" alt="Slider Example" width="400"/>

## Constructors & Methods

- [Slider()](#slider-1)
- [setDirection()](#setdirection)
- [setDuration()](#setduration)
- [setAnimationType()](#setAnimationType)
- [setWrap()](#setwrap)

## Slider()

```python
Slider(
    parent = None,
    direction = Qt.Horizontal,
    duration = 500,
    animationType = QEasingCurve.OutCubic,
    wrap = False,
)
```

**Parameters:**

- *direction:*
  - [Qt.Orientation](https://doc.qt.io/qtforpython/PySide6/QtCore/Qt.html#PySide6.QtCore.PySide6.QtCore.Qt.Orientation) enum object
  - indicates direction of animation
- *duration:*
  - animation duration in milliseconds (ms)
- *animationType:*
  - [QEasingCurve.Type](https://doc.qt.io/qtforpython/PySide6/QtCore/QEasingCurve.html#PySide6.QtCore.PySide6.QtCore.QEasingCurve.Type) enum object
  - animation type
- *wrap:*
  - boolean
  - wrap around slides

## setDirection()

**Return type:** bool

**Parameters:**

- *direction:* [Qt.Orientation](https://doc.qt.io/qtforpython/PySide6/QtCore/Qt.html#PySide6.QtCore.PySide6.QtCore.Qt.Orientation) enum object

**Description:** set direction of animation.

## setDuration()

**Return type:** bool

**Parameters:**

- *duration:* integer representing animation duration

**Description:** set animation duration.

## setAnimationType()

**Return type:** bool

**Parameters:**

- *animationType:* [QEasingCurve.Type](https://doc.qt.io/qtforpython/PySide6/QtCore/QEasingCurve.html#PySide6.QtCore.PySide6.QtCore.QEasingCurve.Type) enum object

**Description:** set animation type.

## setWrap()

**Return type:** bool

- *wrap:* boolean representing whether or not to wrap around slides

**Description:** set up slides to wrap around..

