from PyQt5 import QtGui
from PyQt5 import QtWidgets

CELLSIZE = 72


class PicButton(QtWidgets.QPushButton):
    def __init__(self, image, text, parent=None):
        super().__init__(text, parent)
        self.image = image

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(event.rect(), self.image)
        painter.setFont(QtGui.QFont("Comic Sans MS", 32))
        painter.setPen(QtGui.QColor("black"))
        painter.drawText(CELLSIZE * 3 - CELLSIZE * 0.29 * len(self.text()) / 2,
                         CELLSIZE * 1.2, self.text())

    def sizeHint(self):
        return self.image.size()
