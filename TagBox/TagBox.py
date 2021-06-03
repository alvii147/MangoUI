from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QCursor
from MangoUI import FlowLayout
from MangoUI.utils.ColorOps import to_RGBAtuple

class TagBox(QWidget):
    '''TagBox is an inherited class of QWidget that handles tag lists.'''
    def __init__(
        self,
        parent = None,
        textColor = (21, 21, 21, 255),
        backgroundColor = (245, 177, 66, 255),
        backgroundColorOnHover = (249, 205, 134, 255),
        fontFamily = 'Verdana',
        fontSize = 10,
        fontWeight = 'normal',
        borderStyle = 'solid',
        borderColor = (21, 21, 21, 255),
        borderWidth = 1,
        borderRadius = 2,
    ):

        '''Create new TagBox object.

        Parameters:
            parent (QWidget obj/QLayout obj): parent element
            textColor (QColor obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str): tag text color
            backgroundColor (QColor obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str): tag background color
            backgroundColorOnHover (QColor obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str): tag background color on mouse hover
            fontFamily (str): name of font family
            fontSize (int): font size
            fontWeight (str): font weight
            borderStyle (str): tag border style
            borderColor (QColor obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str): tag border color
            borderWidth (int): tag border width
            borderRadius (int): tag border radius

        Returns:
            TagBox obj
        '''

        if parent:
            super().__init__(parent)
        else:
            super().__init__()

        self.textColor = to_RGBAtuple(textColor)
        self.backgroundColor = to_RGBAtuple(backgroundColor)
        self.backgroundColorOnHover = to_RGBAtuple(backgroundColorOnHover)

        self.fontFamily = fontFamily
        self.fontSize = fontSize
        self.fontWeight = fontWeight

        self.borderStyle = borderStyle
        self.borderColor = to_RGBAtuple(borderColor)
        self.borderWidth = borderWidth
        self.borderRadius = borderRadius

        self.tagList = []

        self.flowLayout = FlowLayout()
        self.setLayout(self.flowLayout)

        self.initTagBox()

    def renderStyleSheet(self, tagWidget):
        self.tagStyleSheet = f'''
            QWidget {{
                color: rgba{str(self.textColor)};
                background-color: rgba{str(self.backgroundColor)};

                font-family: {str(self.fontFamily)};
                font-size: {str(self.fontSize)}pt;
                font-weight: {self.fontWeight};

                border-style: {str(self.borderStyle)};
                border-color: rgba{str(self.borderColor)};
                border-width: {str(self.borderWidth)}px;
                border-radius: {str(self.borderRadius)}px;

                padding: 0px;
            }}
            QWidget:hover {{
                background-color: rgba{str(self.backgroundColorOnHover)}
            }}
        '''

        tagWidget.setStyleSheet(self.tagStyleSheet)

    def initTagBox(self):
        if self.flowLayout.count() != 0:
            self.clearTags()

        for tagName in self.tagList:
            self.displayTag(tagName)

    def displayTag(self, tagName):
        tagWidget = QWidget()
        tagWidget.setAttribute(Qt.WA_StyledBackground, True)
        tagWidget.enterEvent = lambda e : self.setCursor(QCursor(Qt.PointingHandCursor))
        tagWidget.leaveEvent = lambda e : self.setCursor(QCursor(Qt.ArrowCursor))
        tagWidget.mouseReleaseEvent = lambda e : self.removeTag(self.flowLayout.indexOf(tagWidget))
        self.renderStyleSheet(tagWidget)

        hBoxTag = QHBoxLayout()

        tagLabel = QLabel()
        tagLabel.setText(tagName)
        tagLabel.setStyleSheet(f'''
            QLabel {{
                background-color: transparent;
                border: none;
            }}
        ''')
        hBoxTag.addWidget(tagLabel)

        crossIcon = QPixmap('MangoUI/TagBox/img/crossresized.png')
        crossIconLabel = QLabel()
        crossIconLabel.setPixmap(crossIcon)
        crossIconLabel.setStyleSheet(f'''
            QLabel {{
                background-color: transparent;
                border: none;
            }}
        ''')
        hBoxTag.addWidget(crossIconLabel)

        hBoxTag.setContentsMargins(10, 6, 6, 6)
        tagWidget.setLayout(hBoxTag)
        self.flowLayout.addWidget(tagWidget)

    def addTag(self, tagName):
        '''Add new tag if it doesn't exist.

        Parameters:
            tagName (str): tag name

        Returns:
            bool
        '''

        if tagName not in self.tagList:
            self.tagList.append(tagName)
            self.displayTag(tagName)
            return True
        return False

    def removeTag(self, index):
        '''Remove tag by index.

        Parameters:
            index (int): index position of tag to remove

        Returns:
            None
        '''

        self.tagList.pop(index)
        self.initTagBox()

    def clearTags(self):
        '''Clear all tags.

        Returns:
            None
        '''

        while self.flowLayout.count():
            child = self.flowLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def getTags(self):
        '''Get list of tags.

        Returns:
            list
        '''

        return self.tagList