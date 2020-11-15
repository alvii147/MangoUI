import re
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget
from PyQt5.QtCore import Qt, QVariantAnimation, QAbstractAnimation
from PyQt5.QtGui import QCursor, QColor, QPainterPath, QPainter, QPen, QBrush

def rgbStringToInt(rgbString):
    search = re.search("^rgb\(\s*(\d*)\s*,\s*(\d*)\s*,\s*(\d*)\s*\)$", rgbString)
    return int(search.group(1)), int(search.group(2)), int(search.group(3))

def rgbIntToString(redInt, greenInt, blueInt):
    return "rgb(" + str(redInt) + ", " + str(greenInt) + ", " + str(blueInt) + ")"

def rgbTupleToString(rgbTuple):
    return "rgb(" + str(rgbTuple[0]) + ", " + str(rgbTuple[1]) + ", " + str(rgbTuple[2]) + ")"

class SharpButton(QPushButton):
    def __init__(self, parent = None, primaryColor = (0, 179, 60), secondaryColor = (204, 255, 221), pressed_border_color = (240, 240, 240), font_family = "Verdana", font_size = 13, font_weight = "normal", border_style = "solid", border_width = 2, border_radius = 0):
        if parent:
            super().__init__(parent)
        else:
            super().__init__()
        self.setCursor(QCursor(Qt.PointingHandCursor))

        self.primaryColor = primaryColor
        self.secondaryColor = secondaryColor
        p1, p2, p3 = self.primaryColor
        s1, s2, s3 = self.secondaryColor
        self.color = self.primaryColor
        self.background_color = self.secondaryColor
        self.animation = QVariantAnimation(startValue = QColor(p1, p2, p3), endValue = QColor(s1, s2, s3), valueChanged = self.onHover, duration = 400)

        self.font_family = font_family
        self.font_size = font_size
        self.font_weight = font_weight

        self.border_style = border_style
        self.border_color = self.primaryColor
        self.pressed_border_color = pressed_border_color
        self.border_width = border_width
        self.border_radius = border_radius

        self.renderStyleSheet()

    def renderStyleSheet(self):
        self.styleSheet = "QPushButton{"
        self.styleSheet += "color: " + rgbTupleToString(self.color) + ";"
        self.styleSheet += "background-color: " + rgbTupleToString(self.background_color) + ";"

        self.styleSheet += "border-style: " + self.border_style + ";"
        self.styleSheet += "border-color: " + rgbTupleToString(self.border_color) + ";"
        self.styleSheet += "border-width: " + str(self.border_width) + "px" + ";"
        self.styleSheet += "border-radius: " + str(self.border_radius) + "px" + ";"

        self.styleSheet += "font-family: " + self.font_family + ";"
        self.styleSheet += "font-size: " + str(self.font_size) + "px" + ";"
        self.styleSheet += "font-weight: " + self.font_weight + ";"
        self.styleSheet += "}"

        self.styleSheet += "QPushButton::pressed{"
        self.styleSheet += "border-color: " + rgbTupleToString(self.pressed_border_color) + ";"
        self.styleSheet += "}"

        self.setStyleSheet(self.styleSheet)
    
    def onHover(self, color):
        if self.animation.direction() == QAbstractAnimation.Forward:
            self.color = self.primaryColor
        else:
            self.color = self.secondaryColor
        self.background_color = (color.red(), color.green(), color.blue())
        self.renderStyleSheet()

    def enterEvent(self, event):
        self.animation.setDirection(QAbstractAnimation.Backward)
        self.animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.animation.setDirection(QAbstractAnimation.Forward)
        self.animation.start()
        super().leaveEvent(event)

class SharpCanvas(QWidget):
    def __init__(self, parent = None, width = 200, height = 200, posX = 0, posY = 0):
        if parent:
            super().__init__(parent)
        else:
            super().__init__()
        self._path = QPainterPath()
        self.width = width
        self.height = height
        self.posX = posX
        self.posY = posY

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setBrush(QBrush(QColor(255, 247, 242), Qt.SolidPattern))
        painter.setPen(QPen(Qt.NoPen))
        painter.drawRect(self.posX, self.posY, self.width, self.height)

        pen = QPen()
        pen.setWidth(7)
        pen.setColor(QColor(0, 0, 0))
        pen.setStyle(Qt.SolidLine)
        painter.setPen(pen)
        painter.drawPath(self._path)
    
    def mousePressEvent(self, event):
        self._path.moveTo(event.pos())
        self.update()
    
    def mouseMoveEvent(self, event):
        self._path.lineTo(event.pos())
        self.update()
    
    def newPath(self):
        self._path = QPainterPath()
        self.update()