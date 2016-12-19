import sys

from Image_Button import PicButton

try:
    from PyQt5 import QtGui, QtWidgets, QtCore
except Exception as e:
    print('PyQt5 not found: "{}"'.format(e),
          file=sys.stderr)
    sys.exit(1)

CELLSIZE = 72


class MainMenu(QtWidgets.QWidget):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.initUI()

    def initUI(self):
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background,
                         QtGui.QBrush(QtGui.QImage("Images\\menu.png")))
        self.setPalette(palette)
        self.init_button_one()
        self.init_button_two()
        self.setGeometry(0, 0, CELLSIZE * 11, CELLSIZE * 8)
        self.load_images(["menu.png", "ButtonL.png"])
        self.setFixedSize(CELLSIZE * 8, CELLSIZE * 8)
        self.show()

    def init_button_one(self):
        pic = QtGui.QPixmap("./Images/ButtonD.png")
        self.one_player_game_button = PicButton(pic, "Play Alone", self)
        self.one_player_game_button.clicked.connect(self.run_one_player_mode)
        self.one_player_game_button.resize(CELLSIZE * 6, CELLSIZE * 2)
        self.one_player_game_button.move(CELLSIZE, CELLSIZE * 2)

    def init_button_two(self):
        pic = QtGui.QPixmap("./Images/ButtonL.png")
        self.two_players_game_button = PicButton(
            pic, "Play With Friend", self)
        self.two_players_game_button.clicked.connect(self.run_one_player_mode)
        self.two_players_game_button.resize(CELLSIZE * 6, CELLSIZE * 2)
        self.two_players_game_button.move(CELLSIZE, CELLSIZE * 4)

    def run_one_player_mode(self):
        print("fdssf")

    def load_images(self, images_names):
        self.images = {name: QtGui.QImage("Images\\" + name) for name in
                       images_names}

        # def paintEvent(self, event):
        # painter = QtGui.QPainter()
        # painter.begin(self)
        # painter.end()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    menu = MainMenu()

    sys.exit(app.exec_())
