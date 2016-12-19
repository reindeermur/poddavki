class Checker():
    def __init__(self, is_black, x, y):
        self.is_black = is_black
        self.coordinates = (x, y)

    @property
    def x(self):
        return self.coordinates[0]

    @property
    def y(self):
        return self.coordinates[1]

    def opposite_color(self, other_cell):
        return self.is_black != other_cell.is_black

    def move(self, new_coords):
        return Checker(self.is_black, *new_coords)

    def __str__(self):
        return "x={}, y={}, color={}".format(
            self.x, self.y, "black" if self.is_black else 'white')
