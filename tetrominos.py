import copy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game

from settings import Settings


class Tetromino:
    LAST_COL_IDX: int = Settings.GRID_N_OF_COL - 1

    def __init__(
        self,
        game: 'Game',
        pos: list[list],
        tag: str,
        next_tetromino_grid_pos: list[list],
    ) -> None:
        self.settings = game.settings
        self.grid = game.grid
        self.next_tetromino_grid = game.next_tetromino_grid
        self.pos = pos
        self.tag = tag
        self.next_tetromino_grid_pos = next_tetromino_grid_pos
        self.current_rotation = 0

    def check_down(self) -> bool:
        for cell in self.pos:
            if cell[0] == self.settings.GRID_N_OF_ROWS - 1:
                return True
        return False

    def check_touch(self) -> bool:
        for cell in self.pos:
            if (
                self.grid[cell[0] + 1][cell[1]] != 0
                and [(cell[0] + 1), cell[1]] not in self.pos
            ):
                return True
        return False

    def update_on_grid(self) -> None:
        self.main_pos = self.pos[1]
        for cell in self.pos:
            self.grid[cell[0]][cell[1]] = self.tag

    def put_on_next_tetromino_window(self) -> None:
        self.clear_next_tetromino_window()
        for cell in self.next_tetromino_grid_pos:
            self.next_tetromino_grid[cell[0]][cell[1]] = self.tag

    def clear_next_tetromino_window(self) -> None:
        for row in range(self.settings.NEXT_TETROMINO_N_OF_ROWS):
            for col in range(self.settings.NEXT_TETROMINO_N_OF_COL):
                self.next_tetromino_grid[row][col] = self.settings.EMPTY_CELL_TAG

    def clear(self) -> None:
        for cell in self.pos:
            self.grid[cell[0]][cell[1]] = 0

    def check_move_left(self) -> bool:
        for cell in self.pos:
            if cell[1] == 0 or (
                [(cell[0]), (cell[1] - 1)] not in self.pos
                and self.grid[cell[0]][cell[1] - 1] != 0
            ):
                return True
        return False

    def check_move_right(self) -> bool:
        for cell in self.pos:
            if cell[1] == self.LAST_COL_IDX or (
                [(cell[0]), (cell[1] + 1)] not in self.pos
                and self.grid[cell[0]][cell[1] + 1] != 0
            ):
                return True
        return False

    def rotate_left(self) -> None:
        self.clear()
        if (
            self.current_rotation == 0
            and self.main_pos[0] != self.settings.GRID_N_OF_ROWS - 1
        ):
            self.pos3()
            self.current_rotation = 3
        elif self.current_rotation == 1 and self.main_pos[1] != 0:
            self.pos0()
            self.current_rotation = 0
        elif self.current_rotation == 2:
            self.pos1()
            self.current_rotation = 1
        elif self.current_rotation == 3 and self.main_pos[1] != self.LAST_COL_IDX:
            self.pos2()
            self.current_rotation = 2

    def rotate_right(self) -> None:
        self.clear()
        if (
            self.current_rotation == 0
            and self.main_pos[0] != self.settings.GRID_N_OF_ROWS - 1
        ):
            self.pos1()
            self.current_rotation = 1
        elif self.current_rotation == 1 and self.main_pos[1] != 0:
            self.pos2()
            self.current_rotation = 2
        elif self.current_rotation == 2:
            self.pos3()
            self.current_rotation = 3
        elif self.current_rotation == 3 and self.main_pos[1] != self.LAST_COL_IDX:
            self.pos0()
            self.current_rotation = 0

    def pos0(self) -> None:
        raise NotImplementedError("Subclasses must implement pos0 method")

    def pos1(self) -> None:
        raise NotImplementedError("Subclasses must implement pos1 method")

    def pos2(self) -> None:
        raise NotImplementedError("Subclasses must implement pos2 method")

    def pos3(self) -> None:
        raise NotImplementedError("Subclasses must implement pos3 method")

    def move_right(self) -> None:
        if self.check_move_right():
            return
        self.clear()
        for i in self.pos:
            i[1] += 1

    def move_left(self) -> None:
        if self.check_move_left():
            return
        self.clear()
        for cell in self.pos:
            cell[1] -= 1

    def move_down(self) -> None:
        self.clear()
        for cell in self.pos:
            cell[0] += 1


class Itetromino(Tetromino):
    TAG: str = 'I'
    NEXT_TETROMINO_GRID_POS: list[list] = [
        [1, 0],
        [1, 1],
        [1, 2],
        [1, 3],
    ]
    SPAWN_POS: list[list] = [
        [1, Tetromino.LAST_COL_IDX // 2 - 1],
        [1, Tetromino.LAST_COL_IDX // 2],
        [1, Tetromino.LAST_COL_IDX // 2 + 1],
        [1, Tetromino.LAST_COL_IDX // 2 + 2],
    ]

    def __init__(self, game: 'Game') -> None:
        self.spawn()
        super().__init__(game, self.pos, self.TAG, self.NEXT_TETROMINO_GRID_POS)

    def spawn(self) -> None:
        self.pos = copy.deepcopy(self.SPAWN_POS)

    def rotate_right(self) -> None:
        self.clear()
        if (
            self.current_rotation == 0
            and self.pos[0][0] < self.settings.GRID_N_OF_ROWS - 2
        ):
            new0 = [self.pos[0][0] - 1, self.pos[0][1] + 2]
            if (
                self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
                and new0 not in self.pos
            ):
                return
            new1 = [self.pos[1][0] + 1, self.pos[1][1] + 1]
            if (
                self.grid[new1[0]][new1[1]] != self.settings.EMPTY_CELL_TAG
                and new1 not in self.pos
            ):
                return
            new3 = [self.pos[3][0] + 2, self.pos[3][1] - 1]
            if (
                self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
                and new3 not in self.pos
            ):
                return
            self.pos[0] = new0
            self.pos[1] = new1
            self.pos[3] = new3
            self.current_rotation = 1
        elif (
            self.current_rotation == 1
            and self.pos[0][1] < self.LAST_COL_IDX
            and self.pos[0][1] > 1
        ):
            new0 = [self.pos[0][0] + 2, self.pos[0][1] - 2]
            if (
                self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
                and new0 not in self.pos
            ):
                return
            new2 = [self.pos[2][0] + 1, self.pos[2][1] - 1]
            if (
                self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
                and new2 not in self.pos
            ):
                return
            new3 = [self.pos[3][0] - 1, self.pos[3][1] + 1]
            if (
                self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
                and new3 not in self.pos
            ):
                return
            self.pos[0] = new0
            self.pos[2] = new2
            self.pos[3] = new3
            self.current_rotation = 2
        elif (
            self.current_rotation == 2
            and self.pos[0][0] < self.settings.GRID_N_OF_ROWS - 1
        ):
            new0 = [self.pos[0][0] - 2, self.pos[0][1] + 1]
            if (
                self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
                and new0 not in self.pos
            ):
                return
            new1 = [self.pos[1][0] - 1, self.pos[1][1] - 1]
            if (
                self.grid[new1[0]][new1[1]] != self.settings.EMPTY_CELL_TAG
                and new1 not in self.pos
            ):
                return
            new3 = [self.pos[3][0] + 1, self.pos[3][1] - 2]
            if (
                self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
                and new3 not in self.pos
            ):
                return
            self.pos[0] = new0
            self.pos[1] = new1
            self.pos[3] = new3
            self.current_rotation = 3
        elif (
            self.current_rotation == 3
            and self.pos[0][1] < self.LAST_COL_IDX - 1
            and self.pos[0][1] > 0
        ):
            new0 = [self.pos[0][0] + 1, self.pos[0][1] - 1]
            if (
                self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
                and new0 not in self.pos
            ):
                return
            new2 = [self.pos[2][0] - 1, self.pos[2][1] + 1]
            if (
                self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
                and new2 not in self.pos
            ):
                return
            new3 = [self.pos[3][0] - 2, self.pos[3][1] + 2]
            if (
                self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
                and new3 not in self.pos
            ):
                return
            self.pos[0] = new0
            self.pos[2] = new2
            self.pos[3] = new3
            self.current_rotation = 0

    def rotate_left(self) -> None:
        self.clear()
        if (
            self.current_rotation == 0
            and self.pos[0][0] < self.settings.GRID_N_OF_ROWS - 2
        ):
            new0 = [self.pos[0][0] - 1, self.pos[0][1] + 1]
            if (
                self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
                and new0 not in self.pos
            ):
                return
            new2 = [self.pos[2][0] + 1, self.pos[2][1] - 1]
            if (
                self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
                and new2 not in self.pos
            ):
                return
            new3 = [self.pos[3][0] + 2, self.pos[3][1] - 2]
            if (
                self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
                and new3 not in self.pos
            ):
                return
            self.pos[0] = new0
            self.pos[2] = new2
            self.pos[3] = new3
            self.current_rotation = 3
        elif (
            self.current_rotation == 1
            and self.pos[0][1] < self.LAST_COL_IDX
            and self.pos[0][1] > 1
        ):
            new0 = [self.pos[0][0] + 1, self.pos[0][1] - 2]
            if (
                self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
                and new0 not in self.pos
            ):
                return
            new1 = [self.pos[1][0] - 1, self.pos[1][1] - 1]
            if (
                self.grid[new1[0]][new1[1]] != self.settings.EMPTY_CELL_TAG
                and new1 not in self.pos
            ):
                return
            new3 = [self.pos[3][0] - 2, self.pos[3][1] + 1]
            if (
                self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
                and new3 not in self.pos
            ):
                return
            self.pos[0] = new0
            self.pos[1] = new1
            self.pos[3] = new3
            self.current_rotation = 0
        elif (
            self.current_rotation == 2
            and self.pos[0][0] < self.settings.GRID_N_OF_ROWS - 1
        ):
            new0 = [self.pos[0][0] - 2, self.pos[0][1] + 2]
            if (
                self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
                and new0 not in self.pos
            ):
                return
            new2 = [self.pos[2][0] - 1, self.pos[2][1] + 1]
            if (
                self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
                and new2 not in self.pos
            ):
                return
            new3 = [self.pos[3][0] + 1, self.pos[3][1] - 1]
            if (
                self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
                and new3 not in self.pos
            ):
                return
            self.pos[0] = new0
            self.pos[2] = new2
            self.pos[3] = new3
            self.current_rotation = 1
        elif (
            self.current_rotation == 3
            and self.pos[0][1] < self.LAST_COL_IDX - 1
            and self.pos[0][1] > 0
        ):
            new0 = [self.pos[0][0] + 2, self.pos[0][1] - 1]
            if (
                self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
                and new0 not in self.pos
            ):
                return
            new1 = [self.pos[1][0] + 1, self.pos[1][1] + 1]
            if (
                self.grid[new1[0]][new1[1]] != self.settings.EMPTY_CELL_TAG
                and new1 not in self.pos
            ):
                return
            new3 = [self.pos[3][0] - 1, self.pos[3][1] + 2]
            if (
                self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
                and new3 not in self.pos
            ):
                return
            self.pos[0] = new0
            self.pos[1] = new1
            self.pos[3] = new3
            self.current_rotation = 2


class Otetromino(Tetromino):
    TAG: str = 'O'
    NEXT_TETROMINO_GRID_POS: list[list] = [
        [1, 1],
        [2, 1],
        [1, 2],
        [2, 2],
    ]
    SPAWN_POS: list[list] = [
        [1, Tetromino.LAST_COL_IDX // 2],
        [1, Tetromino.LAST_COL_IDX // 2 + 1],
        [0, Tetromino.LAST_COL_IDX // 2],
        [0, Tetromino.LAST_COL_IDX // 2 + 1],
    ]

    def __init__(self, game: 'Game') -> None:
        self.spawn()
        super().__init__(game, self.pos, self.TAG, self.NEXT_TETROMINO_GRID_POS)

    def spawn(self) -> None:
        self.pos = copy.deepcopy(self.SPAWN_POS)

    def rotate_right(self) -> None:
        pass

    def rotate_left(self) -> None:
        pass


class Ttetromino(Tetromino):
    TAG: str = 'T'
    NEXT_TETROMINO_GRID_POS: list[list] = [
        [2, 0],
        [2, 1],
        [2, 2],
        [1, 1],
    ]
    SPAWN_POS: list[list] = [
        [1, Tetromino.LAST_COL_IDX // 2 - 2],
        [1, Tetromino.LAST_COL_IDX // 2 - 1],
        [1, Tetromino.LAST_COL_IDX // 2],
        [0, Tetromino.LAST_COL_IDX // 2 - 1],
    ]

    def __init__(self, game: 'Game') -> None:
        self.spawn()
        self.main_pos = self.pos[1]
        super().__init__(game, self.pos, self.TAG, self.NEXT_TETROMINO_GRID_POS)

    def spawn(self) -> None:
        self.pos = copy.deepcopy(self.SPAWN_POS)

    def pos0(self) -> None:
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if (
            self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
            and new0 not in self.pos
        ):
            return
        new2 = [self.main_pos[0], self.main_pos[1] + 1]
        if (
            self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
            and new2 not in self.pos
        ):
            return
        new3 = [self.main_pos[0], self.main_pos[1] - 1]
        if (
            self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
            and new3 not in self.pos
        ):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos1(self) -> None:
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if (
            self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
            and new0 not in self.pos
        ):
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if (
            self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
            and new2 not in self.pos
        ):
            return
        new3 = [self.main_pos[0], self.main_pos[1] + 1]
        if (
            self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
            and new3 not in self.pos
        ):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos2(self) -> None:
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if (
            self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
            and new0 not in self.pos
        ):
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if (
            self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
            and new2 not in self.pos
        ):
            return
        new3 = [self.main_pos[0], self.main_pos[1] + 1]
        if (
            self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
            and new3 not in self.pos
        ):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos3(self) -> None:
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if (
            self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
            and new0 not in self.pos
        ):
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if (
            self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
            and new2 not in self.pos
        ):
            return
        new3 = [self.main_pos[0], self.main_pos[1] - 1]
        if (
            self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
            and new3 not in self.pos
        ):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3


class Stetromino(Tetromino):
    TAG: str = 'S'
    NEXT_TETROMINO_GRID_POS: list[list] = [
        [2, 0],
        [2, 1],
        [1, 1],
        [1, 2],
    ]
    SPAWN_POS: list[list] = [
        [1, Tetromino.LAST_COL_IDX // 2 - 1],
        [1, Tetromino.LAST_COL_IDX // 2],
        [0, Tetromino.LAST_COL_IDX // 2],
        [0, Tetromino.LAST_COL_IDX // 2 + 1],
    ]

    def __init__(self, game: 'Game') -> None:
        self.spawn()
        self.main_pos = self.pos[1]
        super().__init__(game, self.pos, self.TAG, self.NEXT_TETROMINO_GRID_POS)

    def spawn(self) -> None:
        self.pos = copy.deepcopy(self.SPAWN_POS)

    def pos0(self) -> None:
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if (
            self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
            and new0 not in self.pos
        ):
            return
        new2 = [self.main_pos[0] - 1, self.main_pos[1]]
        if (
            self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
            and new2 not in self.pos
        ):
            return
        new3 = [self.main_pos[0] - 1, self.main_pos[1] + 1]
        if (
            self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
            and new3 not in self.pos
        ):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos1(self) -> None:
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if (
            self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
            and new0 not in self.pos
        ):
            return
        new2 = [self.main_pos[0], self.main_pos[1] + 1]
        if (
            self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
            and new2 not in self.pos
        ):
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1] + 1]
        if (
            self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
            and new3 not in self.pos
        ):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos2(self) -> None:
        new0 = [self.main_pos[0] + 1, self.main_pos[1] - 1]
        if (
            self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
            and new0 not in self.pos
        ):
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if (
            self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
            and new2 not in self.pos
        ):
            return
        new3 = [self.main_pos[0], self.main_pos[1] + 1]
        if (
            self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
            and new3 not in self.pos
        ):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos3(self) -> None:
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if (
            self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
            and new0 not in self.pos
        ):
            return
        new2 = [self.main_pos[0] - 1, self.main_pos[1] - 1]
        if (
            self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
            and new2 not in self.pos
        ):
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1]]
        if (
            self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
            and new3 not in self.pos
        ):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3


class Ztetromino(Tetromino):
    TAG: str = 'Z'
    NEXT_TETROMINO_GRID_POS: list[list] = [
        [1, 0],
        [1, 1],
        [2, 1],
        [2, 2],
    ]
    SPAWN_POS: list[list] = [
        [0, Tetromino.LAST_COL_IDX // 2 - 1],
        [1, Tetromino.LAST_COL_IDX // 2],
        [0, Tetromino.LAST_COL_IDX // 2],
        [1, Tetromino.LAST_COL_IDX // 2 + 1],
    ]

    def __init__(self, game: 'Game') -> None:
        self.spawn()
        self.main_pos = self.pos[1]
        super().__init__(game, self.pos, self.TAG, self.NEXT_TETROMINO_GRID_POS)

    def spawn(self) -> None:
        self.pos = copy.deepcopy(self.SPAWN_POS)

    def pos0(self) -> None:
        new0 = [self.main_pos[0] - 1, self.main_pos[1] - 1]
        if (
            self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
            and new0 not in self.pos
        ):
            return
        new2 = [self.main_pos[0] - 1, self.main_pos[1]]
        if (
            self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
            and new2 not in self.pos
        ):
            return
        new3 = [self.main_pos[0], self.main_pos[1] + 1]
        if (
            self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
            and new3 not in self.pos
        ):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos1(self) -> None:
        new0 = [self.main_pos[0] + 1, self.main_pos[1]]
        if (
            self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
            and new0 not in self.pos
        ):
            return
        new2 = [self.main_pos[0], self.main_pos[1] + 1]
        if (
            self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
            and new2 not in self.pos
        ):
            return
        new3 = [self.main_pos[0] - 1, self.main_pos[1] + 1]
        if (
            self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
            and new3 not in self.pos
        ):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos2(self) -> None:
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if (
            self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
            and new0 not in self.pos
        ):
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if (
            self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
            and new2 not in self.pos
        ):
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1] + 1]
        if (
            self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
            and new3 not in self.pos
        ):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos3(self) -> None:
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if (
            self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
            and new0 not in self.pos
        ):
            return
        new2 = [self.main_pos[0] - 1, self.main_pos[1]]
        if (
            self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
            and new2 not in self.pos
        ):
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1] - 1]
        if (
            self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
            and new3 not in self.pos
        ):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3


class Jtetromino(Tetromino):
    TAG: str = 'J'
    NEXT_TETROMINO_GRID_POS: list[list] = [
        [1, 0],
        [2, 0],
        [2, 1],
        [2, 2],
    ]
    SPAWN_POS: list[list] = [
        [0, Tetromino.LAST_COL_IDX // 2 - 1],
        [1, Tetromino.LAST_COL_IDX // 2],
        [1, Tetromino.LAST_COL_IDX // 2 - 1],
        [1, Tetromino.LAST_COL_IDX // 2 + 1],
    ]

    def __init__(self, game: 'Game') -> None:
        self.spawn()
        self.main_pos = self.pos[1]
        super().__init__(game, self.pos, self.TAG, self.NEXT_TETROMINO_GRID_POS)

    def spawn(self) -> None:
        self.pos = copy.deepcopy(self.SPAWN_POS)

    def pos0(self) -> None:
        new0 = [self.main_pos[0] - 1, self.main_pos[1] - 1]
        if (
            self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
            and new0 not in self.pos
        ):
            return
        new2 = [self.main_pos[0], self.main_pos[1] - 1]
        if (
            self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
            and new2 not in self.pos
        ):
            return
        new3 = [self.main_pos[0], self.main_pos[1] + 1]
        if (
            self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
            and new3 not in self.pos
        ):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos1(self) -> None:
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if (
            self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
            and new0 not in self.pos
        ):
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if (
            self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
            and new2 not in self.pos
        ):
            return
        new3 = [self.main_pos[0] - 1, self.main_pos[1] + 1]
        if (
            self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
            and new3 not in self.pos
        ):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos2(self) -> None:
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if (
            self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
            and new0 not in self.pos
        ):
            return
        new2 = [self.main_pos[0], self.main_pos[1] + 1]
        if (
            self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
            and new2 not in self.pos
        ):
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1] + 1]
        if (
            self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
            and new3 not in self.pos
        ):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos3(self) -> None:
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if (
            self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
            and new0 not in self.pos
        ):
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if (
            self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
            and new2 not in self.pos
        ):
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1] - 1]
        if (
            self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
            and new3 not in self.pos
        ):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3


class Ltetromino(Tetromino):
    TAG: str = 'L'
    NEXT_TETROMINO_GRID_POS: list[list] = [
        [2, 0],
        [2, 1],
        [2, 2],
        [1, 2],
    ]
    SPAWN_POS: list[list] = [
        [1, Tetromino.LAST_COL_IDX // 2 - 1],
        [1, Tetromino.LAST_COL_IDX // 2],
        [1, Tetromino.LAST_COL_IDX // 2 + 1],
        [0, Tetromino.LAST_COL_IDX // 2 + 1],
    ]

    def __init__(self, game: 'Game') -> None:
        self.spawn()
        self.main_pos = self.pos[1]
        super().__init__(game, self.pos, self.TAG, self.NEXT_TETROMINO_GRID_POS)

    def spawn(self) -> None:
        self.pos = copy.deepcopy(self.SPAWN_POS)

    def pos0(self) -> None:
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if (
            self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
            and new0 not in self.pos
        ):
            return
        new2 = [self.main_pos[0], self.main_pos[1] + 1]
        if (
            self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
            and new2 not in self.pos
        ):
            return
        new3 = [self.main_pos[0] - 1, self.main_pos[1] + 1]
        if (
            self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
            and new3 not in self.pos
        ):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos1(self) -> None:
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if (
            self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
            and new0 not in self.pos
        ):
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if (
            self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
            and new2 not in self.pos
        ):
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1] + 1]
        if (
            self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
            and new3 not in self.pos
        ):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos2(self) -> None:
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if (
            self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
            and new0 not in self.pos
        ):
            return
        new2 = [self.main_pos[0], self.main_pos[1] + 1]
        if (
            self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
            and new2 not in self.pos
        ):
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1] - 1]
        if (
            self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
            and new3 not in self.pos
        ):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos3(self) -> None:
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if (
            self.grid[new0[0]][new0[1]] != self.settings.EMPTY_CELL_TAG
            and new0 not in self.pos
        ):
            return
        new2 = [self.main_pos[0] - 1, self.main_pos[1] - 1]
        if (
            self.grid[new2[0]][new2[1]] != self.settings.EMPTY_CELL_TAG
            and new2 not in self.pos
        ):
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1]]
        if (
            self.grid[new3[0]][new3[1]] != self.settings.EMPTY_CELL_TAG
            and new3 not in self.pos
        ):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3
