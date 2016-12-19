from Checker import Checker


class Board:
    def __init__(self):
        self.checkers = {}  # массив, в который потом запихнём шашешчки
        self.setup_checkers()
        self.selected_cells = []
        self.is_black_turn = False
        self.kill_cells = {}
        self.undo = []
        self.redo = []

    @staticmethod
    def is_in_board(x, y):
        return 0 <= x < 8 and 0 <= y < 8

    @staticmethod
    def is_black(x, y):
        return (x + y) % 2 != 0

    @staticmethod
    def get_point_inside(start, finish):
        return ((finish[0] - start[0]) / 2 + start[0],
                (finish[1] - start[1]) / 2 + start[1])

    @property
    def possible_move_cells(self):
        return self.kill_cells.keys()

    @property
    def all_checkers(self):
        return {c for c in self.checkers.values()}

    @property
    def checkers_coords(self):
        return {el for el in self.checkers.keys()}

    def swap_turn(self):
        self.is_black_turn = not self.is_black_turn

    def setup_checkers(self):
        self.checkers = {(x, y): Checker(y < 3, x, y)
                         for x in range(8) for y in {0, 1, 2, 5, 6, 7}
                         if (x + y) % 2 != 0}

    def is_empty_cell(self, x, y):
        return (x, y) in self.checkers_coords

    def handle_mouse_click(self, mouse_pos, cell_size):
        cell_coords = (mouse_pos.x() // cell_size, mouse_pos.y() // cell_size)
        if not self.is_in_board(*cell_coords):
            return

        if not self.selected_cells:
            self.try_select_first_cell(cell_coords)
        elif len(self.selected_cells) == 1:
            self.try_select_second_cell(cell_coords)

        if len(self.selected_cells) == 2:
            self.move(self.selected_cells.pop(0), self.selected_cells.pop(0))

    def try_select_first_cell(self, cell_coords):
        if cell_coords in self.checkers_coords:
            if self.is_black_turn == self.checkers[cell_coords].is_black:
                self.selected_cells.append(cell_coords)
                self.kill_cells = self.get_move_cells(cell_coords)

    def try_select_second_cell(self, cell_coords):
        if cell_coords in self.possible_move_cells:
            self.selected_cells.append(cell_coords)
        else:
            self.selected_cells = []
            self.kill_cells = {}

    def move(self, start, finish):
        old = self.checkers.pop(start)
        new = old.move(finish)
        self.checkers[finish] = new
        if self.kill_cells[finish]:
            for cell in self.kill_cells[finish]:
                self.checkers.pop(cell)
        self.swap_turn()
        self.kill_cells = {}
        self.undo.append(frozenset(self.checkers.items()))
        self.redo = []

    def make_undo(self):
        if self.undo:
            poped = self.undo.pop()
            self.redo.append(poped)
            poped_ = {coord: checker for coord, checker in poped}
            self.checkers = poped_
            print(1)

    def make_redo(self):
        if self.redo:
            poped = self.redo.pop()
            self.undo.append(poped)
            self.checkers = {coord: checker for coord, checker in poped}

    def get_move_cells(self, cell_coords):
        checker = self.checkers[cell_coords]
        move_cells = self.get_hit_path(cell_coords)

        if not move_cells:
            move_cells = {cell: [] for cell in
                          self.step_coords(cell_coords, checker.is_black)
                          if cell not in self.checkers_coords}
        return move_cells

    def get_hit_path(self, cell_coords):
        queue = [cell_coords]
        checker = self.checkers[cell_coords]
        p = {}
        l = {cell_coords: 0}
        cells_to_kill = {cell_coords: []}
        while queue:
            curr = queue.pop(-1)
            for c in self.coords_around(curr):
                hit_cell = self.get_hit_cell(curr, c)
                if self.is_valid(c, checker, hit_cell, p):
                    queue.append(hit_cell)
                    p[hit_cell] = curr
                    l[hit_cell] = l[curr] + 1
                    cells_to_kill[hit_cell] = cells_to_kill[curr] + [c]
        max_l = max(l.values())
        if max_l:
            return {cell: cells_to_kill[cell] for cell, _ in
                    filter(lambda x: x[1] == max_l, l.items())}

    def is_valid(self, c, checker, hit_cell, p):
        return (c in self.checkers_coords
                and checker.opposite_color(self.checkers[c])
                and hit_cell not in self.checkers_coords
                and hit_cell not in set(p.values())
                and self.is_in_board(*hit_cell))

    @staticmethod
    def coords_around(cell):
        return [(cell[0] + d[0], cell[1] + d[1]) for d in
                [(-1, 1), (1, 1), (1, -1), (-1, -1)]]

    @staticmethod
    def step_coords(cell, is_black):
        return [(cell[0] + d[0], cell[1] + d[1]) for d in (
            [(-1, 1), (1, 1)] if is_black else [(1, -1), (-1, -1)])]

    @staticmethod
    def get_hit_cell(cell, other_cell):
        d = (other_cell[0] - cell[0], other_cell[1] - cell[1])
        return other_cell[0] + d[0], other_cell[1] + d[1]
