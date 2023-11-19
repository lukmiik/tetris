import pygame

from settings import Settings


class Tetromino:
    tag: str = ''
    pos: list = []
    next_tetromino_grid_pos: list = []

    def __init__(self, game):
        self.settings = game.settings
        self.grid = game.grid
        self.next_tetromino_grid = game.next_tetromino_grid
        self.last_col_idx = self.settings.grid_n_of_col - 1
        self.current_rotation = 0

    def check_down(self):
        for i in self.pos:
            if i[0] == self.settings.grid_n_of_rows - 1:
                return True

    def check_touch(self):
        for i in self.pos:
            if self.grid[i[0] + 1][i[1]] != 0 and [(i[0] + 1), i[1]] not in self.pos:
                return True

    def update_on_grid(self):
        self.main_pos = self.pos[1]
        for i in self.pos:
            self.grid[i[0]][i[1]] = self.tag

    def put_on_next_tetromino_window(self):
        self.clear_next_tetromino_window()
        for cell in self.next_tetromino_grid_pos:
            self.next_tetromino_grid[cell[0]][cell[1]] = self.tag

    def clear_next_tetromino_window(self):
        for row in range(self.settings.next_tetromino_n_of_rows):
            for col in range(self.settings.next_tetromino_n_of_col):
                self.next_tetromino_grid[row][col] = self.settings.empty_cell_tag

    def clear(self):
        for cell in self.pos:
            self.grid[cell[0]][cell[1]] = 0

    def check_move_left(self):
        for cell in self.pos:
            if cell[1] == 0 or ([(cell[0]), (cell[1] - 1)] not in self.pos and self.grid[cell[0]][cell[1] - 1] != 0):
                return True

    def check_move_right(self):
        for cell in self.pos:
            if cell[1] == self.last_col_idx or (
                [(cell[0]), (cell[1] + 1)] not in self.pos and self.grid[cell[0]][cell[1] + 1] != 0
            ):
                return True

    def rotate_left(self):
        self.clear()
        if self.current_rotation == 0 and self.main_pos[0] != self.settings.grid_n_of_rows - 1:
            self.pos3()
            self.current_rotation = 3
        elif self.current_rotation == 1 and self.main_pos[1] != 0:
            self.pos0()
            self.current_rotation = 0
        elif self.current_rotation == 2:
            self.pos1()
            self.current_rotation = 1
        elif self.current_rotation == 3 and self.main_pos[1] != self.last_col_idx:
            self.pos2()
            self.current_rotation = 2

    def rotate_right(self):
        self.clear()
        if self.current_rotation == 0 and self.main_pos[0] != self.settings.grid_n_of_rows - 1:
            self.pos1()
            self.current_rotation = 1
        elif self.current_rotation == 1 and self.main_pos[1] != 0:
            self.pos2()
            self.current_rotation = 2
        elif self.current_rotation == 2:
            self.pos3()
            self.current_rotation = 3
        elif self.current_rotation == 3 and self.main_pos[1] != self.last_col_idx:
            self.pos0()
            self.current_rotation = 0

    def pos0(self):
        raise NotImplementedError("Subclasses must implement pos0 method")

    def pos1(self):
        raise NotImplementedError("Subclasses must implement pos1 method")

    def pos2(self):
        raise NotImplementedError("Subclasses must implement pos2 method")

    def pos3(self):
        raise NotImplementedError("Subclasses must implement pos3 method")

    def move_right(self):
        if self.check_move_right():
            return
        self.clear()
        for i in self.pos:
            i[1] += 1

    def move_left(self):
        if self.check_move_left():
            return
        self.clear()
        for cell in self.pos:
            cell[1] -= 1

    def move_down(self):
        self.clear()
        for cell in self.pos:
            cell[0] += 1


class Itetromino(Tetromino):
    tag = 'I'
    next_tetromino_grid_pos = [
        [1, 0],
        [1, 1],
        [1, 2],
        [1, 3],
    ]

    def __init__(self, game):
        super().__init__(game)
        self.spawn()

    def spawn(self):
        self.pos = [
            [1, self.last_col_idx // 2 - 1],
            [1, self.last_col_idx // 2],
            [1, self.last_col_idx // 2 + 1],
            [1, self.last_col_idx // 2 + 2],
        ]

    def rotate_right(self):
        self.clear()
        if self.current_rotation == 0 and self.pos[0][0] < self.settings.grid_n_of_rows - 2:
            new0 = [self.pos[0][0] - 1, self.pos[0][1] + 2]
            if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
                return
            new1 = [self.pos[1][0] + 1, self.pos[1][1] + 1]
            if self.grid[new1[0]][new1[1]] != self.settings.empty_cell_tag and new1 not in self.pos:
                return
            new3 = [self.pos[3][0] + 2, self.pos[3][1] - 1]
            if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
                return
            self.pos[0] = new0
            self.pos[1] = new1
            self.pos[3] = new3
            self.current_rotation = 1
        elif self.current_rotation == 1 and self.pos[0][1] < self.last_col_idx and self.pos[0][1] > 1:
            new0 = [self.pos[0][0] + 2, self.pos[0][1] - 2]
            if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
                return
            new2 = [self.pos[2][0] + 1, self.pos[2][1] - 1]
            if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
                return
            new3 = [self.pos[3][0] - 1, self.pos[3][1] + 1]
            if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
                return
            self.pos[0] = new0
            self.pos[2] = new2
            self.pos[3] = new3
            self.current_rotation = 2
        elif self.current_rotation == 2 and self.pos[0][0] < self.settings.grid_n_of_rows - 1:
            new0 = [self.pos[0][0] - 2, self.pos[0][1] + 1]
            if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
                return
            new1 = [self.pos[1][0] - 1, self.pos[1][1] - 1]
            if self.grid[new1[0]][new1[1]] != self.settings.empty_cell_tag and new1 not in self.pos:
                return
            new3 = [self.pos[3][0] + 1, self.pos[3][1] - 2]
            if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
                return
            self.pos[0] = new0
            self.pos[1] = new1
            self.pos[3] = new3
            self.current_rotation = 3
        elif self.current_rotation == 3 and self.pos[0][1] < self.last_col_idx - 1 and self.pos[0][1] > 0:
            new0 = [self.pos[0][0] + 1, self.pos[0][1] - 1]
            if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
                return
            new2 = [self.pos[2][0] - 1, self.pos[2][1] + 1]
            if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
                return
            new3 = [self.pos[3][0] - 2, self.pos[3][1] + 2]
            if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
                return
            self.pos[0] = new0
            self.pos[2] = new2
            self.pos[3] = new3
            self.current_rotation = 0

    def rotate_left(self):
        self.clear()
        if self.current_rotation == 0 and self.pos[0][0] < self.settings.grid_n_of_rows - 2:
            new0 = [self.pos[0][0] - 1, self.pos[0][1] + 1]
            if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
                return
            new2 = [self.pos[2][0] + 1, self.pos[2][1] - 1]
            if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
                return
            new3 = [self.pos[3][0] + 2, self.pos[3][1] - 2]
            if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_ta and new3 not in self.pos:
                return
            self.pos[0] = new0
            self.pos[2] = new2
            self.pos[3] = new3
            self.current_rotation = 3
        elif self.current_rotation == 1 and self.pos[0][1] < self.last_col_idx and self.pos[0][1] > 1:
            new0 = [self.pos[0][0] + 1, self.pos[0][1] - 2]
            if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
                return
            new1 = [self.pos[1][0] - 1, self.pos[1][1] - 1]
            if self.grid[new1[0]][new1[1]] != self.settings.empty_cell_tag and new1 not in self.pos:
                return
            new3 = [self.pos[3][0] - 2, self.pos[3][1] + 1]
            if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
                return
            self.pos[0] = new0
            self.pos[1] = new1
            self.pos[3] = new3
            self.current_rotation = 0
        elif self.current_rotation == 2 and self.pos[0][0] < self.settings.grid_n_of_rows - 1:
            new0 = [self.pos[0][0] - 2, self.pos[0][1] + 2]
            if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
                return
            new2 = [self.pos[2][0] - 1, self.pos[2][1] + 1]
            if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
                return
            new3 = [self.pos[3][0] + 1, self.pos[3][1] - 1]
            if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
                return
            self.pos[0] = new0
            self.pos[2] = new2
            self.pos[3] = new3
            self.current_rotation = 1
        elif self.current_rotation == 3 and self.pos[0][1] < self.last_col_idx - 1 and self.pos[0][1] > 0:
            new0 = [self.pos[0][0] + 2, self.pos[0][1] - 1]
            if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
                return
            new1 = [self.pos[1][0] + 1, self.pos[1][1] + 1]
            if self.grid[new1[0]][new1[1]] != self.settings.empty_cell_tag and new1 not in self.pos:
                return
            new3 = [self.pos[3][0] - 1, self.pos[3][1] + 2]
            if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
                return
            self.pos[0] = new0
            self.pos[1] = new1
            self.pos[3] = new3
            self.current_rotation = 2


class Otetromino(Tetromino):
    tag = 'O'
    next_tetromino_grid_pos = [
        [1, 1],
        [2, 1],
        [1, 2],
        [2, 2],
    ]

    def __init__(self, game):
        super().__init__(game)
        self.spawn()

    def spawn(self):
        self.pos = [
            [1, self.last_col_idx // 2],
            [1, self.last_col_idx // 2 + 1],
            [0, self.last_col_idx // 2],
            [0, self.last_col_idx // 2 + 1],
        ]

    def rotate_right(self):
        pass

    def rotate_left(self):
        pass


class Ttetromino(Tetromino):
    tag = 'T'
    next_tetromino_grid_pos = [
        [2, 0],
        [2, 1],
        [2, 2],
        [1, 1],
    ]

    def __init__(self, game):
        super().__init__(game)
        self.spawn()
        self.main_pos = self.pos[1]

    def spawn(self):
        self.pos = [
            [1, self.last_col_idx // 2 - 2],
            [1, self.last_col_idx // 2 - 1],
            [1, self.last_col_idx // 2],
            [0, self.last_col_idx // 2 - 1],
        ]

    def pos0(self):
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
            return
        new2 = [self.main_pos[0], self.main_pos[1] + 1]
        if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
            return
        new3 = [self.main_pos[0], self.main_pos[1] - 1]
        if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos1(self):
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
            return
        new3 = [self.main_pos[0], self.main_pos[1] + 1]
        if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos2(self):
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
            return
        new3 = [self.main_pos[0], self.main_pos[1] + 1]
        if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos3(self):
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
            return
        new3 = [self.main_pos[0], self.main_pos[1] - 1]
        if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3


class Stetromino(Tetromino):
    tag = 'S'
    next_tetromino_grid_pos = [
        [2, 0],
        [2, 1],
        [1, 1],
        [1, 2],
    ]

    def __init__(self, game):
        super().__init__(game)
        self.spawn()
        self.main_pos = self.pos[1]

    def spawn(self):
        self.pos = [
            [1, self.last_col_idx // 2 - 1],
            [1, self.last_col_idx // 2],
            [0, self.last_col_idx // 2],
            [0, self.last_col_idx // 2 + 1],
        ]

    def pos0(self):
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
            return
        new2 = [self.main_pos[0] - 1, self.main_pos[1]]
        if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
            return
        new3 = [self.main_pos[0] - 1, self.main_pos[1] + 1]
        if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos1(self):
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
            return
        new2 = [self.main_pos[0], self.main_pos[1] + 1]
        if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1] + 1]
        if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos2(self):
        new0 = [self.main_pos[0] + 1, self.main_pos[1] - 1]
        if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
            return
        new3 = [self.main_pos[0], self.main_pos[1] + 1]
        if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos3(self):
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
            return
        new2 = [self.main_pos[0] - 1, self.main_pos[1] - 1]
        if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1]]
        if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3


class Ztetromino(Tetromino):
    tag = 'Z'
    next_tetromino_grid_pos = [
        [1, 0],
        [1, 1],
        [2, 1],
        [2, 2],
    ]

    def __init__(self, game):
        super().__init__(game)
        self.spawn()
        self.main_pos = self.pos[1]

    def spawn(self):
        self.pos = [
            [0, self.last_col_idx // 2 - 1],
            [1, self.last_col_idx // 2],
            [0, self.last_col_idx // 2],
            [1, self.last_col_idx // 2 + 1],
        ]

    def pos0(self):
        new0 = [self.main_pos[0] - 1, self.main_pos[1] - 1]
        if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
            return
        new2 = [self.main_pos[0] - 1, self.main_pos[1]]
        if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
            return
        new3 = [self.main_pos[0], self.main_pos[1] + 1]
        if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos1(self):
        new0 = [self.main_pos[0] + 1, self.main_pos[1]]
        if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
            return
        new2 = [self.main_pos[0], self.main_pos[1] + 1]
        if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
            return
        new3 = [self.main_pos[0] - 1, self.main_pos[1] + 1]
        if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos2(self):
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1] + 1]
        if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos3(self):
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
            return
        new2 = [self.main_pos[0] - 1, self.main_pos[1]]
        if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1] - 1]
        if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3


class Jtetromino(Tetromino):
    tag = 'J'
    next_tetromino_grid_pos = [
        [1, 0],
        [2, 0],
        [2, 1],
        [2, 2],
    ]

    def __init__(self, game):
        super().__init__(game)
        self.spawn()
        self.main_pos = self.pos[1]

    def spawn(self):
        self.pos = [
            [0, self.last_col_idx // 2 - 1],
            [1, self.last_col_idx // 2],
            [1, self.last_col_idx // 2 - 1],
            [1, self.last_col_idx // 2 + 1],
        ]

    def pos0(self):
        new0 = [self.main_pos[0] - 1, self.main_pos[1] - 1]
        if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
            return
        new2 = [self.main_pos[0], self.main_pos[1] - 1]
        if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
            return
        new3 = [self.main_pos[0], self.main_pos[1] + 1]
        if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos1(self):
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
            return
        new3 = [self.main_pos[0] - 1, self.main_pos[1] + 1]
        if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos2(self):
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
            return
        new2 = [self.main_pos[0], self.main_pos[1] + 1]
        if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1] + 1]
        if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos3(self):
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1] - 1]
        if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

class Ltetromino(Tetromino):
    tag = 'L'
    next_tetromino_grid_pos = [
        [2, 0],
        [2, 1],
        [2, 2],
        [1, 2],
    ]

    def __init__(self, game):
        super().__init__(game)
        self.spawn()
        self.main_pos = self.pos[1]

    def spawn(self):
        self.pos = [
            [1, self.last_col_idx // 2 - 1],
            [1, self.last_col_idx // 2],
            [1, self.last_col_idx // 2 + 1],
            [0, self.last_col_idx // 2 + 1],
        ]

    def pos0(self):
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
            return
        new2 = [self.main_pos[0], self.main_pos[1] + 1]
        if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
            return
        new3 = [self.main_pos[0] - 1, self.main_pos[1] + 1]
        if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos1(self):
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1] + 1]
        if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos2(self):
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
            return
        new2 = [self.main_pos[0], self.main_pos[1] + 1]
        if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1] - 1]
        if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos3(self):
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if self.grid[new0[0]][new0[1]] != self.settings.empty_cell_tag and new0 not in self.pos:
            return
        new2 = [self.main_pos[0] - 1, self.main_pos[1] - 1]
        if self.grid[new2[0]][new2[1]] != self.settings.empty_cell_tag and new2 not in self.pos:
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1]]
        if self.grid[new3[0]][new3[1]] != self.settings.empty_cell_tag and new3 not in self.pos:
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3
