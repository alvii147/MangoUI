from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt, QVariantAnimation, QAbstractAnimation
from PyQt6.QtGui import QCursor, QColor
from MangoUI.utils.ColorOps import to_RGBAtuple

class Button(QPushButton):
    '''Button an inherited class of QPushButton, styled using QSS and QVariantAnimation.'''
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
        '''Create new Button object.

        Parameters:
            parent (QWidget obj/QLayout obj): parent element
            primaryColor (QColor obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str): normal text color and background color on hover
            secondaryColor (QColor obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str): normal background color and the text color on hover
            parentBackgroundColor (QColor obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str): parent element's background color used for minimize effect on click 
            fontFamily (str): name of font family
            fontSize (int): font size
            fontWeight (str): font weight
            borderStyle (str): border style
            borderWidth (int): border width
            borderRadius (int): border radius

        Returns:
            Button obj
        '''

        if parent:
            super().__init__(parent)
        else:
            super().__init__()

        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

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
        self.styleSheet = f'''
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
        '''
        self.setStyleSheet(self.styleSheet)

    def onHover(self, color):
        if self.animation.direction() == QAbstractAnimation.Direction.Forward:
            self.color = self.primaryColor
        else:
            self.color = self.secondaryColor
        self.backgroundColor = to_RGBAtuple(color)
        self.renderStyleSheet()

    def enterEvent(self, event):
        self.animation.setDirection(QAbstractAnimation.Direction.Backward)
        self.animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.animation.setDirection(QAbstractAnimation.Direction.Forward)
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

    def setColors(self, primaryColor = None, secondaryColor = None, parentBackgroundColor = None):
        '''Set button colors.

        Parameters:
            primaryColor (QColor obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str): normal text color and background color on hover
            secondaryColor (QColor obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str): normal background color and the text color on hover
            parentBackgroundColor (QColor obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str): parent element's background color used for minimize effect on click 

        Returns:
            None
        '''

        if primaryColor != None:
            self.primaryColor = to_RGBAtuple(primaryColor)

        if secondaryColor != None:
            self.secondaryColor = to_RGBAtuple(secondaryColor)

        if parentBackgroundColor != None:
            self.parentBackgroundColor = to_RGBAtuple(parentBackgroundColor)

        self.setupColors()
        self.renderStyleSheet()

    def setFont(self, fontFamily = None, fontSize = None, fontWeight = None):
        '''Set button text font properties.

        Parameters:
            fontFamily (str): name of font family
            fontSize (int): font size
            fontWeight (str): font weight

        Returns:
            None
        '''

        if fontFamily != None:
            self.fontFamily = fontFamily

        if fontSize != None:
            self.fontSize = fontSize

        if fontWeight != None:
            self.fontWeight = fontWeight

        self.renderStyleSheet()

    def setBorder(self, borderStyle = None, borderWidth = None, borderRadius = None):
        '''Set button border properties.

        Parameters:
            borderStyle (str): border style
            borderWidth (int): border width
            borderRadius (int): border radius

        Returns:
            None
        '''

        if borderStyle != None:
            self.borderStyle = borderStyle

        if borderWidth != None:
            self.borderWidth = borderWidth

        if borderRadius != None:
            self.borderRadius = borderRadius

        self.renderStyleSheet()