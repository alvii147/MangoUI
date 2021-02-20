from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt, QVariantAnimation, QAbstractAnimation
from PyQt5.QtGui import QCursor, QColor
from .utils.ColorOps import to_RGBAtuple

class Button(QPushButton):
    def __init__(
            self,
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