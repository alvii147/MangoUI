from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPen, QBrush, QPixmap
from MangoUI.utils.ColorOps import to_RGBAtuple

class Canvas(QLabel):
    '''Canvas an inherited class of QLabel with a null QPixmap. Using QPainter, Canvas allows the user to draw on the window.'''
    def __init__(
        self,
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
    ):
        '''Create new Canvas object.

        Parameters:
            parent (QWidget obj/QLayout obj): parent element
            width (int): width of canvas
            height (int): height of canvas
            penColor (QColor obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str): pen color
            canvasColor (QColor obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str): background color of canvas
            strokeStyle (QPenStyle obj): line style of pen stroke
            strokeWidth (int): width of pen stroke
            borderStyle (str): border style
            borderColor (QColor obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str): border color of canvas
            borderWidth (int): border width

        Returns:
            Canvas obj
        '''

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
        self.styleSheet = f'''
            QLabel {{
                border-style: {str(self.borderStyle)};
                border-color: rgba{to_RGBAtuple(self.borderColor)};
                border-width: {str(self.borderWidth)}px;
            }}
        '''
        self.setStyleSheet(self.styleSheet)

    def resize(self, width, height):
        ret = super().resize(width, height)
        self.setupPixmap()
        return ret

    def setPenColor(self, color):
        '''Set pen color.

        Parameters:
            color (QColor obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str): pen color

        Returns:
            None
        '''

        self.color = to_RGBAtuple(color)

    def setBorder(self, borderStyle = None, borderColor = None, borderWidth = None):
        '''Set canvas border properties.

        Parameters:
            borderStyle (str): border style
            borderColor (QColor obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str): border color of canvas
            borderWidth (int): border width

        Returns:
            None
        '''

        if borderStyle != None:
            self.borderStyle = borderStyle

        if borderColor != None:
            self.borderColor = borderColor

        if borderWidth != None:
            self.borderWidth = borderWidth

        self.renderStyleSheet()

    def saveCanvas(self, dest):
        '''Save canvas content to image file.

        Parameters:
            dest (str):  image file destination path

        Returns:
            None
        '''

        pixmap = self.pixmap()
        pixmap.save(dest)

    def clearCanvas(self):
        '''Clear canvas content.

        Returns:
            None
        '''

        pixmap = self.pixmap()
        pixmap.fill(QColor(*self.backgroundColor))
        self.setPixmap(pixmap)