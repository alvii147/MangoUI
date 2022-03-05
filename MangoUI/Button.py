from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import (
    Qt,
    QVariantAnimation,
    QAbstractAnimation,
)
from PyQt6.QtGui import QCursor, QColor
import PyQt6
from MangoUI.utils.ColorOps import to_RGBAtuple


class Button(QPushButton):
    """
    Multi-colored, animated button.

    Parameters
    ----------
    parent : QObject, optional
        Parent object that contains this widget. Passing this ensures that
        destroying the parent also destroys this widget.

    primaryColor : int, tuple, str or PyQt6.QtGui.QColor
        Primary button color, as a 32-bit integer representing RGBA, tuple of
        floats representing RGBA values, HTML RGBA string, HTML hexadecimal
        string, or QColor object.

        This is the default text color of the button and the background color
        of the button on hover.

    secondaryColor : int, tuple, str or PyQt6.QtGui.QColor
        Secondary button color, as a 32-bit integer representing RGBA, tuple of
        floats representing RGBA values, HTML RGBA string, HTML hexadecimal
        string, or QColor object.

        This is the default background color of the button and the text color
        of the button on hover.

    parentBackgroundColor : int, tuple, str or PyQt6.QtGui.QColor
        Background color of parent widget, as a 32-bit integer representing
        RGBA, tuple of floats representing RGBA values, HTML RGBA string,
        HTML hexadecimal string, or QColor object.

        The button border is set to this color on press and is used to provide
        an illusion of compression on press.

    animationType : PyQt6.QtCore.QEasingCurve.Type
        Button animation type.

    animationDuration : int
        Button animation duration in milliseconds.

    fontFamily : str
        Font family of button text.

    fontSize : int
        Font size of button text in point value.

    fontWeight : str
        Font weight of button text.

    borderStyle : str
        Border style of button.

    borderWidth : int
        Border width of button in pixels.

    borderRadius : int
        Border radius of button in pixels.
    """

    def __init__(
        self,
        parent=None,
        primaryColor=(21, 21, 21, 255),
        secondaryColor=(245, 177, 66, 255),
        parentBackgroundColor=(240, 240, 240, 255),
        animationType=PyQt6.QtCore.QEasingCurve.Type.OutCubic,
        animationDuration=400,
        fontFamily='Verdana',
        fontSize=8,
        fontWeight='normal',
        borderStyle='solid',
        borderWidth=1,
        borderRadius=2,
    ):
        if parent:
            super().__init__(parent)
        else:
            super().__init__()

        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.primaryColor = to_RGBAtuple(primaryColor)
        self.secondaryColor = to_RGBAtuple(secondaryColor)
        self.parentBackgroundColor = to_RGBAtuple(parentBackgroundColor)
        self.animationType = animationType
        self.animationDuration = animationDuration

        self.fontFamily = fontFamily
        self.fontSize = fontSize
        self.fontWeight = fontWeight

        self.borderStyle = borderStyle
        self.borderWidth = borderWidth
        self.borderRadius = borderRadius

        self.setupAnimationColors()
        self.renderStyleSheet()

    def renderStyleSheet(self):
        """
        Set QSS style sheet for widget using defined attributes.
        """

        self.buttonStyleSheet = f"""
            QPushButton {{
                color: rgba{to_RGBAtuple(self.textColor)};
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
        self.setStyleSheet(self.buttonStyleSheet)

    def animateText(self, currentTextColor):
        """
        Update text color during animation.

        Parameters
        ----------
        currentTextColor : PyQt6.QtGui.QColor
            Current button text color.
        """

        self.textColor = to_RGBAtuple(currentTextColor)
        self.renderStyleSheet()

    def animateBackground(self, currentBackgroundColor):
        """
        Update background color during animation.

        Parameters
        ----------
        currentTextColor : PyQt6.QtGui.QColor
            Current button background color.
        """

        self.backgroundColor = to_RGBAtuple(currentBackgroundColor)
        self.renderStyleSheet()

    def setupAnimationColors(self):
        """
        Set up button colors and animations.
        """

        self.textColor = self.primaryColor
        self.backgroundColor = self.secondaryColor
        self.borderColor = self.primaryColor

        self.textAnimation = QVariantAnimation(
            startValue=QColor(*self.textColor),
            endValue=QColor(*self.backgroundColor),
            valueChanged=self.animateText,
            duration=self.animationDuration,
            easingCurve=self.animationType,
        )

        self.backgroundAnimation = QVariantAnimation(
            startValue=QColor(*self.backgroundColor),
            endValue=QColor(*self.textColor),
            valueChanged=self.animateBackground,
            duration=self.animationDuration,
            easingCurve=self.animationType,
        )

    def enterEvent(self, event):
        """
        Override enter event signal method for widget to set animation
        direction and start animation.

        Parameters
        ----------
        event : PyQt6.QtGui.QEnterEvent
            Event passed to base method.
        """

        self.textAnimation.setDirection(QAbstractAnimation.Direction.Forward)
        self.backgroundAnimation.setDirection(
            QAbstractAnimation.Direction.Forward
        )

        self.textAnimation.start()
        self.backgroundAnimation.start()

        super().enterEvent(event)

    def leaveEvent(self, event):
        """
        Override leave event signal method for widget to set animation
        direction and start animation.

        Parameters
        ----------
        event : PyQt6.QtCore.QEvent
            Event passed to base method.
        """

        self.textAnimation.setDirection(QAbstractAnimation.Direction.Backward)
        self.backgroundAnimation.setDirection(
            QAbstractAnimation.Direction.Backward
        )

        self.textAnimation.start()
        self.backgroundAnimation.start()

        super().leaveEvent(event)

    def setColors(
        self,
        primaryColor=None,
        secondaryColor=None,
        parentBackgroundColor=None,
    ):
        """
        Set button colors.

        Parameters
        ----------
        primary : int, tuple, str or PyQt6.QtGui.QColor
            Primary button color, as a 32-bit integer representing RGBA, tuple
            of floats representing RGBA values, HTML RGBA string, HTML
            hexadecimal string, or QColor object.

            This is the default text color of the button and the background
            color of the button on hover.

        secondaryColor : int, tuple, str or PyQt6.QtGui.QColor
            Secondary button color, as a 32-bit integer representing RGBA,
            tuple o floats representing RGBA values, HTML RGBA string, HTML
            hexadecimal string, or QColor object.

            This is the default background color of the button and the text
            color of the button on hover.

        parentBackgroundColor : int, tuple, str or PyQt6.QtGui.QColor
            Background color of parent widget, as a 32-bit integer representing
            RGBA, tuple of floats representing RGBA values, HTML RGBA string,
            HTML hexadecimal string, or QColor object.

            The button border is set to this color on press and is used to
            provide an illusion of compression on press.
        """

        if primaryColor is not None:
            self.primaryColor = to_RGBAtuple(primaryColor)

        if secondaryColor is not None:
            self.secondaryColor = to_RGBAtuple(secondaryColor)

        if parentBackgroundColor is not None:
            self.parentBackgroundColor = to_RGBAtuple(parentBackgroundColor)

        self.setupAnimationColors()
        self.renderStyleSheet()

    def setFont(self, fontFamily=None, fontSize=None, fontWeight=None):
        """
        Set button text font properties.

        Parameters
        ----------
        fontFamily : str
            Font family of button text.

        fontSize : int
            Font size of button text in point value.

        fontWeight : str
            Font weight of button text.
        """

        if fontFamily is not None:
            self.fontFamily = fontFamily

        if fontSize is not None:
            self.fontSize = fontSize

        if fontWeight is not None:
            self.fontWeight = fontWeight

        self.renderStyleSheet()

    def setBorder(self, borderStyle=None, borderWidth=None, borderRadius=None):
        """
        Set button border properties.

        Parameters
        ----------
        borderStyle : str
            Border style of button.

        borderWidth : int
            Border width of button in pixels.

        borderRadius : int
            Border radius of button in pixels.
        """

        if borderStyle is not None:
            self.borderStyle = borderStyle

        if borderWidth is not None:
            self.borderWidth = borderWidth

        if borderRadius is not None:
            self.borderRadius = borderRadius

        self.renderStyleSheet()
