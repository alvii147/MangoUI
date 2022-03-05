from PyQt6.QtWidgets import QStackedWidget
from PyQt6.QtCore import (
    Qt,
    QPoint,
    pyqtSlot,
    QParallelAnimationGroup,
    QPropertyAnimation,
    QAbstractAnimation,
)
import PyQt6


class Slider(QStackedWidget):
    """
    Widget that supports slide navigation between stacked widgets.

    Parameters
    ----------
    parent : QObject, optional
        Parent object that contains this widget. Passing this ensures that
        destroying the parent also destroys this widget.

    slideDirection : PyQt6.QtCore.Qt.Orientation
        Sliding animation direction.

    animationType : PyQt6.QtCore.QEasingCurve.Type
        Sliding animation type.

    animationDuration : int
        Sliding animation duration in milliseconds.

    wrapAround : bool
        Wrap around slides. If set to true, the first slide returns after the
        last slide.
    """

    def __init__(
        self,
        parent=None,
        slideDirection=PyQt6.QtCore.Qt.Orientation.Horizontal,
        animationType=PyQt6.QtCore.QEasingCurve.Type.OutCubic,
        animationDuration=500,
        wrapAround=False,
    ):
        if parent:
            super().__init__(parent)
        else:
            super().__init__()

        self.slideDirection = slideDirection
        self.animationType = animationType
        self.animationDuration = animationDuration
        self.wrapAround = wrapAround
        self.currentSlide = 0
        self.nextSlide = 0
        self.currentPosition = QPoint(0, 0)
        self.active = False

    def setSlideDirection(self, slideDirection):
        """
        Set sliding animation direction.

        Parameters
        ----------
        slideDirection : Qt.Orientation.Horizontal
            Sliding animation direction.
        """

        self.slideDirection = slideDirection

    def setAnimationType(self, animationType):
        """
        Set sliding animation type.

        Parameters
        ----------
        animationType : PyQt6.QtCore.Qt.QEasingCurve.Type
            Sliding animation type.
        """

        self.animationType = animationType

    def setAnimationDuration(self, animationDuration):
        """
        Set animation duration.

        Parameters
        ----------
        animationDuration : int
            Sliding animation duration in milliseconds.
        """

        self.animationDuration = animationDuration

    def setWrapAround(self, wrapAround):
        """
        Set wrap around slides.

        Parameters
        ----------
        wrapAround : bool
            Wrap around slides.
        """

        self.wrapAround = wrapAround

    @pyqtSlot()
    def slidePrevious(self):
        """
        Move to previous slide.
        """

        i = self.currentIndex()
        if self.wrapAround or i > 0:
            self.slideToIndex(i - 1)

    @pyqtSlot()
    def slideNext(self):
        """
        Move to next slide.
        """

        i = self.currentIndex()
        if self.wrapAround or i < self.count() - 1:
            self.slideToIndex(i + 1)

    def slideToIndex(self, idx):
        """
        Move to slide by index.

        Parameters
        ----------
        idx : int
            Slide index.
        """

        if idx > self.count() - 1:
            idx = idx % self.count()
        elif idx < 0:
            idx = (idx + self.count()) % self.count()

        self.slideToWidget(self.widget(idx))

    def slideToWidget(self, widget):
        """
        Slide to given widget.

        Parameters
        ----------
        widget : PyQt6.QtWidgets.QWidget
            Widget to slide to.
        """

        if self.active:
            return

        self.active = True

        i = self.currentIndex()
        iNext = self.indexOf(widget)

        if i == iNext:
            self.active = False
            return

        offsetX = self.frameRect().width()
        offsetY = self.frameRect().height()
        self.widget(iNext).setGeometry(self.frameRect())

        if self.slideDirection == Qt.Orientation.Horizontal:
            if i < iNext:
                offsetX = -offsetX
                offsetY = 0
            else:
                offsetY = 0
        else:
            if i < iNext:
                offsetX = 0
                offsetY = -offsetY
            else:
                offsetX = 0

        positionCurrent = self.widget(i).pos()
        positionNext = self.widget(iNext).pos()
        self.currentPosition = positionCurrent

        offset = QPoint(offsetX, offsetY)
        self.widget(iNext).move(positionNext - offset)
        self.widget(iNext).show()
        self.widget(iNext).raise_()

        animationGroup = QParallelAnimationGroup(
            self,
            finished=self.animationDoneSlot,
        )

        for idx, start, end in zip(
            (i, iNext),
            (positionCurrent, positionNext - offset),
            (positionCurrent + offset, positionNext),
        ):
            animation = QPropertyAnimation(
                self.widget(idx),
                b'pos',
                startValue=start,
                endValue=end,
                easingCurve=self.animationType,
                duration=self.animationDuration,
            )
            animationGroup.addAnimation(animation)

        self.nextSlide = iNext
        self.currentSlide = i
        self.active = True
        animationGroup.start(
            QAbstractAnimation.DeletionPolicy.DeleteWhenStopped
        )

    @pyqtSlot()
    def animationDoneSlot(self):
        self.setCurrentIndex(self.nextSlide)
        self.widget(self.currentSlide).hide()
        self.widget(self.currentSlide).move(self.currentPosition)
        self.active = False
