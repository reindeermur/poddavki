import sys

from Board import Board
from Checker import Checker
from Image_Button import PicButton

try:
    from PyQt5 import QtGui, QtWidgets, QtCore
except Exception as e:
    print('PyQt5 not found: "{}"'.format(e),
          file=sys.stderr)
    sys.exit(1)

CELLSIZE = 72


class GUI(QtWidgets.QWidget):
    def __init__(self, board: Board):
        super(GUI, self).__init__()
        self.board = board
        self.init_button_undo()
        self.init_button_redo()
        self.initUI()
        self.show()

    def initUI(self):
        self.setGeometry(0, 0, CELLSIZE * 11, CELLSIZE * 8)
        self.load_images(
            ["white.png", "black.png", "checkerD.png", "checkerW.png",
             "QueenD.png", "QueenW.png", "scoreBoard.png", "Menu.png",
             "checkerD.png", "ButtonL.png"])
        self.setFixedSize(CELLSIZE * 8, CELLSIZE * 8.5)

    def load_images(self, images_names):
        self.images = {name: QtGui.QImage("Images\\" + name) for name in
                       images_names}

    def mousePressEvent(self, q_mouse_event):
        self.board.handle_mouse_click(q_mouse_event.pos(), CELLSIZE)
        self.repaint()

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        self._draw_board(painter)
        painter.end()

    def _draw_board(self, painter):
        for x in range(8):
            for y in range(8):
                self._draw_cell(painter, (x, y))

        for c in self.board.possible_move_cells:
            self._draw_highlight(painter, c)

        for checker in self.board.all_checkers:
            self._draw_checker(painter, checker)

        self.draw_panel(painter)

    @staticmethod
    def draw_panel(painter: QtGui.QPainter):
        rect = QtCore.QRect(0, CELLSIZE * 8, CELLSIZE * 8, CELLSIZE * 0.5, )
        painter.fillRect(rect, QtGui.QBrush(QtGui.QColor(47, 79, 79)))

    @staticmethod
    def _draw_highlight(painter: QtGui.QPainter, coordinates):
        pen = QtGui.QPen(QtGui.QColor(255, 255, 0))
        pen.setWidth(3)
        painter.setPen(pen)
        painter.drawRect(coordinates[0] * CELLSIZE,
                         coordinates[1] * CELLSIZE, CELLSIZE, CELLSIZE)
        painter.setPen(QtGui.QColor(0, 0, 0))

    def _draw_cell(self, painter: QtGui.QPainter, coords):
        painter.drawImage(coords[0] * CELLSIZE, coords[1] * CELLSIZE,
                          self.images[
                              "black.png" if self.board.is_black(
                                  *coords) else "white.png"])

    def _draw_checker(self, painter: QtGui.QPainter, checker: Checker):
        painter.drawImage(checker.x * CELLSIZE + 2, checker.y * CELLSIZE + 2,
                          self.images[
                              "checkerD.png" if checker.is_black
                              else "checkerW.png"])

    def init_button_undo(self):
        pic = QtGui.QPixmap(".\\Images\\ButtonD.png")
        self.undo = PicButton(pic, "undo", self)
        self.undo.clicked.connect(self.run_undo)
        self.undo.resize(CELLSIZE * 4, CELLSIZE * 0.5)
        self.undo.move(0, CELLSIZE * 8)

    def run_undo(self):
        self.board.make_undo()
        self.repaint()

    def init_button_redo(self):
        pic = QtGui.QPixmap(".\\Images\\ButtonD.png")
        self.undo = PicButton(pic, "redo", self)
        self.undo.clicked.connect(self.run_redo)
        self.undo.resize(CELLSIZE * 4, CELLSIZE * 0.5)
        self.undo.move(CELLSIZE * 4, CELLSIZE * 8)

    def run_redo(self):
        self.board.make_redo()
        self.repaint()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = GUI(Board())

    sys.exit(app.exec_())
