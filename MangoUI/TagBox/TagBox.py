from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QCursor
from MangoUI import FlowLayout
from MangoUI.utils.ColorOps import to_RGBAtuple


class TagBox(QWidget):
    """
    Widget for handling tags.

    Parameters
    ----------
    parent : PyQt6.QtCore.QObject, optional
        Parent object that contains this widget. Passing this ensures that
        destroying the parent also destroys this widget.

    textColor : int, tuple, str or PyQt6.QtGui.QColor
        Tag text color, as a 32-bit integer representing RGBA, tuple of floats
        representing RGBA values, HTML RGBA string, HTML hexadecimal string, or
        QColor object.

    backgroundColor : int, tuple, str or PyQt6.QtGui.QColor
        Tag background color, as a 32-bit integer representing RGBA, tuple of
        floats representing RGBA values, HTML RGBA string, HTML hexadecimal
        string, or QColor object.

    backgroundColorOnHover : int, tuple, str or PyQt6.QtGui.QColor
        Tag background color on hover, as a 32-bit integer representing RGBA,
        tuple of floats representing RGBA values, HTML RGBA string, HTML
        hexadecimal string, or QColor object.

    fontFamily : str
        Font family of tag text.

    fontSize : int
        Font size of tag text in point value.

    fontWeight : str
        Font weight of tag text.

    borderStyle : str
        Border style of tag.

    borderColor : int, tuple, str or PyQt6.QtGui.QColor
        Border color of tag. as a 32-bit integer representing RGBA, tuple of
        floats representing RGBA values, HTML RGBA string, HTML hexadecimal
        string, or QColor object.

    borderWidth : int
        Border width of tag in pixels.

    borderRadius : int
        Border radius of tag in pixels.
    """

    def __init__(
        self,
        parent=None,
        textColor=(21, 21, 21, 255),
        backgroundColor=(245, 177, 66, 255),
        backgroundColorOnHover=(249, 205, 134, 255),
        fontFamily='Verdana',
        fontSize=10,
        fontWeight='normal',
        borderStyle='solid',
        borderColor=(21, 21, 21, 255),
        borderWidth=1,
        borderRadius=2,
    ):
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
        """
        Set QSS style sheet for tag using defined attributes.

        Parameters
        ----------
        tagWidget : QWidget
            Tag widget.
        """

        self.tagStyleSheet = f"""
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
        """

        tagWidget.setStyleSheet(self.tagStyleSheet)

    def initTagBox(self):
        """
        Clear and re-display all tags.
        """

        if self.flowLayout.count() != 0:
            self.clearTags()

        for tagName in self.tagList:
            self.displayTag(tagName)

    def displayTag(self, tagName):
        """
        Display tag on widget.

        Parameters
        ----------
        tagName : str
            Tag name.
        """

        tagWidget = QWidget()
        tagWidget.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        tagWidget.enterEvent = lambda e: self.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )
        tagWidget.leaveEvent = lambda e: self.setCursor(
            QCursor(Qt.CursorShape.ArrowCursor)
        )
        tagWidget.mouseReleaseEvent = lambda e: self.removeTag(
            self.flowLayout.indexOf(tagWidget),
            returnTag=False,
        )
        self.renderStyleSheet(tagWidget)

        hBoxTag = QHBoxLayout()

        tagLabel = QLabel()
        tagLabel.setText(tagName)
        tagLabel.setStyleSheet(
            """
            QLabel {{
                background-color: transparent;
                border: none;
            }}
            """
        )
        hBoxTag.addWidget(tagLabel)

        crossIcon = QPixmap('MangoUI/TagBox/img/crossresized.png')
        crossIconLabel = QLabel()
        crossIconLabel.setPixmap(crossIcon)
        crossIconLabel.setStyleSheet(
            """
            QLabel {{
                background-color: transparent;
                border: none;
            }}
            """
        )
        hBoxTag.addWidget(crossIconLabel)

        hBoxTag.setContentsMargins(10, 6, 6, 6)
        tagWidget.setLayout(hBoxTag)
        self.flowLayout.addWidget(tagWidget)

    def addTag(
        self, tagName, allowDuplicates=False, raiseErrorOnDuplicates=True
    ):
        """
        Add new tag if it doesn't exist.

        Parameters
        ----------
        tagName : str
            Tag name.

        allowDuplicates : bool
            Allow duplicate tags.

        raiseErrorOnDuplicates : bool
            Raise ValueError if duplicate tag added. This has no affect if
            ``allowDuplicates = True``.
        """

        if not allowDuplicates and tagName in self.tagList:
            if raiseErrorOnDuplicates:
                raise ValueError(
                    f'Tag {tagName} already exists. '
                    'To allow duplicate tags set allowDuplicates = True. '
                    'To silently ignore duplicate tags, '
                    'set allowDuplicates = False '
                    'and raiseErrorOnDuplicates = False.'
                )
            else:
                return

        self.tagList.append(tagName)
        self.displayTag(tagName)

    def removeTag(self, i, returnTag=True):
        """
        Remove tag by index.

        Parameters
        ----------
        i : int
            Index position of tag to remove.

        returnTag : bool
            Return tag name.

        Returns
        -------
        str or None
            Tag name. Setting ``returnTag = False``, returns None.
        """

        removedTag = self.tagList.pop(i)
        self.initTagBox()

        if returnTag:
            return removedTag
        else:
            return None

    def clearTags(self):
        """
        Clear all tags.
        """

        while self.flowLayout.count():
            child = self.flowLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def getTags(self):
        """
        Get tag names.

        Returns
        -------
        list
            list of tag names.
        """

        return self.tagList
