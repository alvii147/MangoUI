from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QColor, QPainter, QPixmap
import PyQt6
from MangoUI.utils.ColorOps import to_RGBAtuple


class Canvas(QLabel):
    """
    Canvas widget for drawing.

    Parameters
    ----------
    parent : QObject, optional
        Parent object that contains this widget. Passing this ensures that
        destroying the parent also destroys this widget.

    width : int
        Canvas height.

    height : int
        Canvas height.

    canvasColor : int, tuple, str or PyQt6.QtGui.QColor
        Canvas background color, as a 32-bit integer representing RGBA, tuple
        of floats representing RGBA values, HTML RGBA string, HTML hexadecimal
        string, or QColor object.

    penColor : int, tuple, str or PyQt6.QtGui.QColor
        Pen color, as a 32-bit integer representing RGBA, tuple of floats
        representing RGBA values, HTML RGBA string, HTML hexadecimal string, or
        QColor object.

    strokeStyle : PyQt6.QtCore.Qt.PenStyle
        Pen stroke style.

    strokeWidth : int
        Pen stroke width.

    borderStyle : str
        Border style of canvas.

    borderColor : int, tuple, str or PyQt6.QtGui.QColor
        Border color of canvas. as a 32-bit integer representing RGBA, tuple of
        floats representing RGBA values, HTML RGBA string, HTML hexadecimal
        string, or QColor object.

    borderWidth : int
        Border width of canvas in pixels.
    """

    def __init__(
        self,
        parent=None,
        width=200,
        height=200,
        canvasColor=(255, 247, 242, 255),
        penColor=(25, 25, 25, 255),
        strokeStyle=PyQt6.QtCore.Qt.PenStyle.SolidLine,
        strokeWidth=3,
        borderStyle='solid',
        borderColor=(0, 0, 0, 255),
        borderWidth=1,
    ):
        if parent:
            super().__init__(parent)
        else:
            super().__init__()

        self.width = width
        self.height = height

        self.backgroundColor = canvasColor

        self.penColor = penColor
        self.strokeStyle = strokeStyle
        self.strokeWidth = strokeWidth

        self.borderStyle = borderStyle
        self.borderColor = to_RGBAtuple(borderColor)
        self.borderWidth = borderWidth

        self.xCache = None
        self.yCache = None

        self.setFixedSize(self.width, self.height)
        self.setupPixmap()
        self.renderStyleSheet()

    def renderStyleSheet(self):
        """
        Set QSS style sheet for widget using defined attributes.
        """

        self.styleSheet = f"""
            QLabel {{
                border-style: {str(self.borderStyle)};
                border-color: rgba{to_RGBAtuple(self.borderColor)};
                border-width: {str(self.borderWidth)}px;
            }}
        """
        self.setStyleSheet(self.styleSheet)

    def mouseMoveEvent(self, event):
        """
        Override mouse move event signal to draw on canvas.

        Parameters
        ----------
        event : PyQt6.QtGui.QMouseEvent
            Event passed to base method.
        """

        if self.xCache is None:
            self.xCache = event.position().x()
            self.yCache = event.position().y()
        else:
            painter = QPainter(self.canvas)

            pen = painter.pen()
            pen.setWidth(self.strokeWidth)
            pen.setColor(QColor(*self.penColor))
            pen.setStyle(self.strokeStyle)
            painter.setPen(pen)

            painter.drawLine(
                self.xCache,
                self.yCache,
                event.position().x(),
                event.position().y(),
            )
            painter.end()

            self.setPixmap(self.canvas)
            self.xCache = event.position().x()
            self.yCache = event.position().y()

    def mouseReleaseEvent(self, event):
        """
        Override mouse release event signal to draw on canvas.

        Parameters
        ----------
        event : PyQt6.QtGui.QMouseEvent
            Event passed to base method.
        """

        self.xCache = None
        self.yCache = None

    def setupPixmap(self):
        """
        Create and set new pixmap.
        """

        self.canvas = QPixmap(self.width, self.height)
        self.canvas.fill(QColor(*self.backgroundColor))
        self.setPixmap(self.canvas)

    def resize(self, width, height):
        """
        Override resize method to set up new pixmap everytime the window is
        resized.

        Parameters
        ----------
        width : int
            Widget width.

        height : int
            Widget height.
        """

        super().resize(width, height)
        self.setupPixmap()

    def setPen(self, penColor=None, strokeStyle=None, strokeWidth=None):
        """
        Set pen properties.

        Parameters
        ----------
        penColor : int, tuple, str or PyQt6.QtGui.QColor
            Pen color, as a 32-bit integer representing RGBA, tuple of floats
            representing RGBA values, HTML RGBA string, HTML hexadecimal
            string, or QColor object.

        strokeStyle : PyQt6.QtCore.Qt.QPenStyle
            Pen stroke style.

        strokeWidth : int
            Pen stroke width.
        """

        if penColor is not None:
            self.penColor = to_RGBAtuple(penColor)

        if strokeStyle is not None:
            self.strokeStyle = strokeStyle

        if strokeWidth is not None:
            self.strokeWidth = strokeWidth

    def setBorder(self, borderStyle=None, borderColor=None, borderWidth=None):
        """
        Set canvas border properties.

        Parameters
        ----------
        borderStyle : str
            Border style of canvas.

        borderColor : int, tuple, str or PyQt6.QtGui.QColor
            Border color of canvas. as a 32-bit integer representing RGBA,
            tuple of floats representing RGBA values, HTML RGBA string, HTML
            hexadecimal string, or QColor object.

        borderWidth : int
            Border width of canvas in pixels.
        """

        if borderStyle is not None:
            self.borderStyle = borderStyle

        if borderColor is not None:
            self.borderColor = to_RGBAtuple(borderColor)

        if borderWidth is not None:
            self.borderWidth = borderWidth

        self.renderStyleSheet()

    def saveCanvas(self, dest):
        """
        Save canvas content to image file.

        Parameters
        ----------
        dest : str or PyQt6.QtCore.QIODevice
            Image file destination path.
        """

        pixmap = self.pixmap()
        pixmap.save(dest)

    def clearCanvas(self):
        """
        Clear canvas contents.
        """

        pixmap = self.pixmap()
        pixmap.fill(QColor(*self.backgroundColor))
        self.setPixmap(pixmap)
