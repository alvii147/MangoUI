from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import Qt, QVariantAnimation, QAbstractAnimation
from PyQt5.QtGui import QCursor, QColor, QPainterPath, QPainter, QPen, QBrush, QPixmap
from utils.ColorOps import to_RGBAtuple

class SharpButton(QPushButton):
    def __init__(
            self,
            parent = None,
            primaryColor = (0, 179, 60, 255),
            secondaryColor = (204, 255, 221, 255),
            parentBackgroundColor = (240, 240, 240, 255),
            fontFamily = "Verdana",
            fontSize = 8,
            fontWeight = "normal",
            borderStyle = "solid",
            borderWidth = 1,
            borderRadius = 2
        ):

        if parent:
            super().__init__(parent)
        else:
            super().__init__()

        self.setCursor(QCursor(Qt.PointingHandCursor))

        self.primaryColor = to_RGBAtuple(primaryColor)
        self.secondaryColor = to_RGBAtuple(secondaryColor)
        self.parentBackgroundColor = to_RGBAtuple(parentBackgroundColor)

        self.setupColors()

        self.fontFamily = fontFamily
        self.fontSize = fontSize
        self.fontWeight = fontWeight

        self.borderStyle = borderStyle
        self.borderWidth = borderWidth
        self.borderRadius = borderRadius

        self.renderStyleSheet()

    def renderStyleSheet(self):
        self.styleSheet = f"""
            QPushButton {{
                color: rgba{to_RGBAtuple(self.color)};
                background-color: rgba{to_RGBAtuple(self.backgroundColor)};

                border-style: {str(self.borderStyle)};
                border-color: rgba{to_RGBAtuple(self.borderColor)};
                border-width: {str(self.borderWidth)}px;
                border-radius: {str(self.borderRadius)}px;

                font-family: {str(self.fontFamily)};
                font-size: {str(self.fontSize)}pt;
                font-weight: {self.fontWeight};
                padding: 5px;
            }}

            QPushButton::pressed {{
                border-color: rgba{to_RGBAtuple(self.parentBackgroundColor)};
            }}
        """
        self.setStyleSheet(self.styleSheet)

    def onHover(self, color):
        if self.animation.direction() == QAbstractAnimation.Forward:
            self.color = self.primaryColor
        else:
            self.color = self.secondaryColor
        self.backgroundColor = to_RGBAtuple(color)
        self.renderStyleSheet()

    def enterEvent(self, event):
        self.animation.setDirection(QAbstractAnimation.Backward)
        self.animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.animation.setDirection(QAbstractAnimation.Forward)
        self.animation.start()
        super().leaveEvent(event)

    def setupColors(self):
        self.color = self.primaryColor
        self.backgroundColor = self.secondaryColor
        self.animation = QVariantAnimation(
            startValue = QColor(*self.primaryColor),
            endValue = QColor(*self.secondaryColor),
            valueChanged = self.onHover, duration = 400
        )
        self.borderColor = self.primaryColor

    def setPrimaryColor(self, color):
        self.primaryColor = to_RGBAtuple(color)
        self.setupColors()
        self.renderStyleSheet()

        return True

    def setSecondaryColor(self, color):
        self.secondaryColor = to_RGBAtuple(color)
        self.setupColors()
        self.renderStyleSheet()

        return True

    def setParentBackgroundColor(self, color):
        self.parentBackgroundColor = to_RGBAtuple(color)
        self.renderStyleSheet()

        return True

    def setFont(self, fontFamily = None, fontSize = None, fontWeight = None):
        if fontFamily != None:
            self.fontFamily = fontFamily

        if fontSize != None:
            self.fontSize = fontSize

        if fontWeight != None:
            self.fontWeight = fontWeight

        self.renderStyleSheet()

        return True

    def setBorder(self, borderStyle = None, borderWidth = None, borderRadius = None):
        if borderStyle != None:
            self.borderStyle = borderStyle

        if borderWidth != None:
            self.borderWidth = borderWidth

        if borderRadius != None:
            self.borderRadius = borderRadius

        self.renderStyleSheet()

        return True

class SharpCanvas(QLabel):
    def __init__(
            self,
            parent = None,
            width = 200,
            height = 200,
            penColor = (25, 25, 25, 255),
            canvasColor = (255, 247, 242, 255),
            strokeStyle = Qt.SolidLine,
            strokeWidth = 3,
            borderStyle = "solid",
            borderColor = (0, 0, 0, 255),
            borderWidth = 1
        ):

        if parent:
            super().__init__(parent)
        else:
            super().__init__()

        self.width = width
        self.height = height

        self.color = penColor
        self.backgroundColor = canvasColor
    
        self.strokeStyle = strokeStyle
        self.strokeWidth = strokeWidth

        self.borderStyle = borderStyle
        self.borderColor = borderColor
        self.borderWidth = borderWidth

        self.xCache = None
        self.yCache = None
        self.setFixedSize(self.width, self.height)
        self.setupPixmap()
        self.renderStyleSheet()

    def mouseMoveEvent(self, event):
        if self.xCache == None:
            self.xCache = event.x()
            self.yCache = event.y()
        else:
            painter = QPainter(self.pixmap())
            pen = painter.pen()
            pen.setWidth(self.strokeWidth)
            pen.setColor(QColor(*self.color))
            pen.setStyle(self.strokeStyle)
            painter.setPen(pen)
            painter.drawLine(self.xCache, self.yCache, event.x(), event.y())
            painter.end()
            self.update()
            self.xCache = event.x()
            self.yCache = event.y()

    def mouseReleaseEvent(self, event):
        self.xCache = None
        self.yCache = None

    def setupPixmap(self):
        pixmap = QPixmap(self.width, self.height)
        pixmap.fill(QColor(*self.backgroundColor))
        self.setPixmap(pixmap)

    def renderStyleSheet(self):
        self.styleSheet = f"""
            QLabel {{
                border-style: {str(self.borderStyle)};
                border-color: rgba{to_RGBAtuple(self.borderColor)};
                border-width: {str(self.borderWidth)}px;
            }}
        """
        self.setStyleSheet(self.styleSheet)

    def resize(self, width, height):
        ret = super().resize(width, height)
        self.setupPixmap()
        return ret

    def setPenColor(self, color):
        if isinstance(color, tuple):
            self.color = color
        elif isinstance(color, QColor):
            self.color = to_RGBAtuple(color)
        else:
            return False

    def clearCanvas(self):
        pixmap = self.pixmap()
        pixmap.fill(QColor(*self.backgroundColor))
        self.setPixmap(pixmap)
        return True

    def saveCanvas(self, dest):
        pixmap = self.pixmap()
        pixmap.save(dest)
        return True