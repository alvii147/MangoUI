from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtCore import Qt, QEasingCurve, QPoint, pyqtSlot, QParallelAnimationGroup, QPropertyAnimation, QAbstractAnimation

class Slider(QStackedWidget):
    '''Slider an inherited class of QStackedWidget that supports slide navigation between stacked widgets.'''
    def __init__(
        self,
        parent = None,
        direction = Qt.Horizontal,
        duration = 500,
        animationType = QEasingCurve.OutCubic,
        wrap = False,
    ):
        '''Create new Slider object.

        Parameters:
            parent (QWidget obj/QLayout obj): Parent element
            direction (Qt.Orientation obj): direction of animation
            duration (int): animation during in milliseconds
            animationType (QEasingCurve.Type obj): animation type
            wrap (bool): wrap around slides

        Returns:
            Slider obj
        '''

        if parent:
            super().__init__(parent)
        else:
            super().__init__()

        self.direction = direction
        self.duration = duration
        self.animationType = animationType
        self.wrap = wrap
        self.currentSlide = 0
        self.nextSlide = 0
        self.currentPosition = QPoint(0, 0)
        self.active = False

    def setDirection(self, direction):
        '''Set direction of animation.

        Parameters:
            direction (Qt.Orientation obj): direction of animation

        Returns:
            None
        '''

        self.direction = direction

    def setDuration(self, duration):
        '''Set animation duration.

        Parameters:
            duration (int): animation during in milliseconds

        Returns:
            None
        '''

        self.duration = duration

    def setAnimationType(self, animationType):
        '''Set animation type.

        Parameters:
            animationType (QEasingCurve.Type obj): animation type

        Returns:
            None
        '''

        self.animationType = animationType

    def setWrap(self, wrap):
        '''Set animation duration.

        Parameters:
            wrap (bool): wrap around slides

        Returns:
            None
        '''

        self.wrap = wrap

    @pyqtSlot()
    def slidePrevious(self):
        '''Move to previous slide.

        Returns:
            None
        '''

        i = self.currentIndex()
        if self.wrap or i > 0:
            self.slideIndex(i - 1)

    @pyqtSlot()
    def slideNext(self):
        '''Move to next slide.

        Returns:
            None
        '''

        i = self.currentIndex()
        if self.wrap or i < self.count() - 1:
            self.slideIndex(i + 1)

    def slideIndex(self, index):
        '''Move to slide by index.

        Parameters:
            index (int): index position of slide

        Returns:
            None
        '''

        if index > self.count() - 1:
            index = index % self.count()
        elif index < 0:
            index = (index + self.count()) % self.count()
        self.slideWidget(self.widget(index))

    def slideWidget(self, widget):
        if self.active:
            return

        self.active = True

        i = self.currentIndex()
        i_next = self.indexOf(widget)

        if i == i_next:
            self.active = False
            return

        offsetX = self.frameRect().width()
        offsetY = self.frameRect().height()
        self.widget(i_next).setGeometry(self.frameRect())

        if self.direction == Qt.Horizontal:
            if i < i_next:
                offsetX = -offsetX
                offsetY = 0
            else:
                offsetY = 0
        else:
            if i < i_next:
                offsetX = 0
                offsetY = -offsetY
            else:
                offsetX = 0

        positionCurrent = self.widget(i).pos()
        positionNext = self.widget(i_next).pos()
        self.currentPosition = positionCurrent

        offset = QPoint(offsetX, offsetY)
        self.widget(i_next).move(positionNext - offset)
        self.widget(i_next).show()
        self.widget(i_next).raise_()

        animationGroup = QParallelAnimationGroup(self, finished = self.animationDoneSlot)

        for index, start, end in zip((i, i_next), (positionCurrent, positionNext - offset), (positionCurrent + offset, positionNext)):
            animation = QPropertyAnimation(
                self.widget(index),
                b'pos',
                duration = self.duration,
                easingCurve = self.animationType,
                startValue = start,
                endValue = end,
            )
            animationGroup.addAnimation(animation)

        self.nextSlide = i_next
        self.currentSlide = i
        self.active = True
        animationGroup.start(QAbstractAnimation.DeleteWhenStopped)

    @pyqtSlot()
    def animationDoneSlot(self):
        self.setCurrentIndex(self.nextSlide)
        self.widget(self.currentSlide).hide()
        self.widget(self.currentSlide).move(self.currentPosition)
        self.active = False