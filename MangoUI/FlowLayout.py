from PyQt6.QtWidgets import QLayout, QSizePolicy
from PyQt6.QtCore import Qt, QRect, QSize, QPoint, QMargins


class FlowLayout(QLayout):
    """
    Flow layout widget, as outlined in the official Qt documentation and
    implemented by Tong Xiao.

    https://doc.qt.io/qt-5/qtwidgets-layouts-flowlayout-example.html
    https://gist.github.com/Cysu/7461066

    Parameters
    ----------
    parent : PyQt6.QtCore.QObject, optional
        Parent object that contains this widget. Passing this ensures that
        destroying the parent also destroys this widget.

    margin : int
        Left, right, top, and bottom margins for layout.

    spacing : int
        Spacing between child widgets.
    """

    def __init__(self, parent=None, margin=0, spacing=-1):
        if parent:
            super().__init__(parent)
            self.setContentsMargins(
                QMargins(
                    margin,
                    margin,
                    margin,
                    margin,
                )
            )
        else:
            super().__init__()

        self.setSpacing(spacing)
        self.itemList = []

    def __del__(self):
        """
        Delete layout.
        """

        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item):
        """
        Add widget to layout.

        Parameters
        ----------
        item : PyQt6.QtCore.QObject
            Item to add.
        """

        self.itemList.append(item)

    def count(self):
        """
        Get number of items.

        Returns
        -------
        int
            Number of items.
        """

        return len(self.itemList)

    def itemAt(self, idx):
        """
        Get item by index.

        Parameters
        ----------
        idx : int
            Item index.

        Returns
        -------
        PyQt6.QtCore.QObject
            Found item.
        """

        try:
            return self.itemList[idx]
        except IndexError:
            return None

    def takeAt(self, idx):
        """
        Pop item by index.

        Parameters
        ----------
        idx : int
            Item index.

        Returns
        -------
        PyQt6.QtCore.QObject
            Popped item.
        """

        try:
            return self.itemList.pop(idx)
        except IndexError:
            return None

    def expandingDirections(self):
        """
        Returns whether this layout can make use of more space than
        ``sizeHint`` indicates.

        Returns
        -------
        PyQt6.QtCore.Qt.Orientation
            Indicates whether this layout can make use of more space.
        """

        return Qt.Orientation(0)

    def hasHeightForWidth(self):
        """
        Returns True if this layout's preferred height depends on its width;
        otherwise returns False.

        Returns
        -------
        bool
            Indicates if height depends on width.
        """

        return True

    def heightForWidth(self, width):
        """
        Returns the preferred height for this layout item, given the width,
        which is not used in this default implementation.

        Parameters
        ----------
        width : int
            Given width.

        Returns
        -------
        int
            Preferred height.
        """

        height = self.doLayout(QRect(0, 0, width, 0), True)

        return height

    def setGeometry(self, rect):
        """
        Set geometry of the widget relative to its parent and excluding the
        window frame.

        Parameters
        ----------
        rect : PyQt6.QtCore.QRect
            Left, top, width, and height values.
        """

        super().setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        """
        Get the recommended size for the widget.

        Returns
        -------
        PyQt6.QtCore.QSize
            Recommended size.
        """

        return self.minimumSize()

    def minimumSize(self):
        """
        Get the widget's minimum size.

        Returns
        -------
        PyQt6.QtCore.QSize
            Minimum size.
        """

        size = QSize()

        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())

        size += QSize(
            2 * self.contentsMargins().top(),
            2 * self.contentsMargins().top(),
        )

        return size

    def doLayout(self, rect, testOnly):
        """
        Layout all items.

        Parameters
        ----------
        rect : PyQt6.QtCore.QRect
            Left, top, width, and height values.

        testOnly : bool
            Indicates if layout should be created.

        Returns
        -------
        int
            Height of layout.
        """

        x = rect.x()
        y = rect.y()
        lineHeight = 0

        for item in self.itemList:
            style = item.widget().style()
            layoutSpacingX = self.spacing() + style.layoutSpacing(
                QSizePolicy.ControlType.PushButton,
                QSizePolicy.ControlType.PushButton,
                Qt.Orientation.Horizontal,
            )

            layoutSpacingY = self.spacing() + style.layoutSpacing(
                QSizePolicy.ControlType.PushButton,
                QSizePolicy.ControlType.PushButton,
                Qt.Orientation.Vertical,
            )

            nextX = x + item.sizeHint().width() + layoutSpacingX
            if nextX - layoutSpacingX > rect.right() and lineHeight > 0:
                x = rect.x()
                y = y + lineHeight + layoutSpacingY
                nextX = x + item.sizeHint().width() + layoutSpacingX
                lineHeight = 0

            if not testOnly:
                item.setGeometry(
                    QRect(
                        QPoint(x, y),
                        item.sizeHint(),
                    )
                )

            x = nextX
            lineHeight = max(lineHeight, item.sizeHint().height())

        return y + lineHeight - rect.y()
