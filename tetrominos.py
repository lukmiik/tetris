import copy
import time
from typing import TYPE_CHECKING

import pygame

from settings import Settings

if TYPE_CHECKING:
    from game import Game


class Tetromino:
    '''Tetromino class for the game'''

    LAST_COL_IDX: int = Settings.GRID_N_OF_COL - 1
    pos: list[list]
    TAG: str
    NEXT_TETROMINO_GRID_POS: list[list]
    SPAWN_POS: list[list]

    def __init__(
        self,
        game: 'Game',
    ) -> None:
        '''Initialize Tetromino object with the Game object and child class attributes'''
        self.game = game
        self.settings = self.game.settings
        self.grid = self.game.grid
        self.next_tetromino_grid = game.next_tetromino_grid
        self.spawn()
        self.main_pos = self.pos[1]
        self.current_rotation = 0

    def spawn(self) -> None:
        '''Set the spawn position'''
        self.pos = copy.deepcopy(self.SPAWN_POS)

    def check_down(self) -> bool:
        '''
        Checks if the tetromino is at the bottom of the grid

        Returns:
            (bool): True if the tetromino is at the bottom of the grid, False otherwise
        '''
        for cell in self.pos:
            if cell[0] == self.settings.GRID_N_OF_ROWS - 1:
                return True
        return False

    def check_touch(self) -> bool:
        '''
        Check if the bottom of the tetromino is touching another tetromino

        Returns:
            (bool): True if the bottom of the tetromino is touching another tetromino, False otherwise
        '''
        for cell in self.pos:
            if (
                self.grid[cell[0] + 1][cell[1]] != 0
                and [(cell[0] + 1), cell[1]] not in self.pos
            ):
                return True
        return False

    def update_on_grid(self) -> None:
        '''Updates the grid with the new position of the tetromino'''
        self.main_pos = self.pos[1]
        for cell in self.pos:
            self.grid[cell[0]][cell[1]] = self.TAG

    def put_on_next_tetromino_window(self) -> None:
        '''Puts the next tetromino on the next tetromino window'''
        self.clear_next_tetromino_window()
        for cell in self.NEXT_TETROMINO_GRID_POS:
            self.next_tetromino_grid[cell[0]][cell[1]] = self.TAG

    def clear_next_tetromino_window(self) -> None:
        '''Clears the next tetromino window'''
        for row in range(self.settings.NEXT_TETROMINO_N_OF_ROWS):
            for col in range(self.settings.NEXT_TETROMINO_N_OF_COL):
                self.next_tetromino_grid[row][col] = self.settings.EMPTY_CELL_TAG

    def clear(self) -> None:
        '''Clears the grid from the tetromino'''
        for cell in self.pos:
            self.grid[cell[0]][cell[1]] = 0

    def check_move_left(self) -> bool:
        '''
        Check if the tetromino can move left by checking if it is at the left edge of the grid or if it is touching another tetromino on the left

        Returns:
            (bool): True if the tetromino can move left, False otherwise
        '''
        for cell in self.pos:
            if cell[1] == 0 or (
                [(cell[0]), (cell[1] - 1)] not in self.pos
                and self.grid[cell[0]][cell[1] - 1] != 0
            ):
                return True
        return False

    def check_move_right(self) -> bool:
        '''
        Check if the tetromino can move right by checking if it is at the right edge of the grid or if it is touching another tetromino on the right

        Returns:
            (bool): True if the tetromino can move right, False otherwise
        '''
        for cell in self.pos:
            if cell[1] == self.LAST_COL_IDX or (
                [(cell[0]), (cell[1] + 1)] not in self.pos
                and self.grid[cell[0]][cell[1] + 1] != 0
            ):
                return True
        return False

    def rotate_left(self) -> None:
        '''Rotates the tetromino left'''
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
        '''Rotates the tetromino right'''
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
        '''Rotates the tetromino to position 0'''
        raise NotImplementedError("Subclasses must implement pos0 method")

    def pos1(self) -> None:
        '''Rotates the tetromino to position 1'''
        raise NotImplementedError("Subclasses must implement pos1 method")

    def pos2(self) -> None:
        '''Rotates the tetromino to position 2'''
        raise NotImplementedError("Subclasses must implement pos2 method")

    def pos3(self) -> None:
        '''Rotates the tetromino to position 3'''
        raise NotImplementedError("Subclasses must implement pos3 method")

    def check_cell_available_for_rotation(self, cell: list[int]) -> bool:
        '''
        Check if the cell is available for rotation

        Args:
            cell (list[int]): Cell to check

        REturns:
            (bool): True if the cell is available for rotation, False otherwise
        '''
        if (
            self.grid[cell[0]][cell[1]] != self.settings.EMPTY_CELL_TAG
            and cell not in self.pos
        ):
            return False
        return True

    def move_right(self) -> None:
        '''Moves the tetromino right'''
        if self.check_move_right():
            return
        self.clear()
        for i in self.pos:
            i[1] += 1

    def move_left(self) -> None:
        '''Moves the tetromino left'''
        if self.check_move_left():
            return
        self.clear()
        for cell in self.pos:
            cell[1] -= 1

    def move_down(self) -> bool | None:
        '''Moves the tetromino down'''
        if self.check_down() or self.check_touch():
            return False
        self.clear()
        for cell in self.pos:
            cell[0] += 1

    def hard_drop(self) -> None:
        '''Hard drops the tetromino'''
        while self.move_down() is not False:
            self.update_on_grid()
            self.game.draw_grid()
            self.game.draw_game_window()
            pygame.display.update()
            time.sleep(self.settings.HARD_DROP_LOOP_SLEEP_TIME)


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
        '''
        Calls the parent class constructor

        Args:
            game (Game): Game object
        '''
        super().__init__(game)

    def rotate_right(self) -> None:
        '''Rotates the tetromino right'''
        self.clear()
        if (
            self.current_rotation == 0
            and 0 < self.main_pos[0] < self.settings.GRID_N_OF_ROWS - 2
        ):
            self.pos1()
            self.current_rotation = 1
        elif self.current_rotation == 1 and 1 < self.main_pos[1] < self.LAST_COL_IDX:
            self.pos2()
            self.current_rotation = 2
        elif (
            self.current_rotation == 2
            and 1 < self.main_pos[0] < self.settings.GRID_N_OF_ROWS - 1
        ):
            self.pos3()
            self.current_rotation = 3
        elif (
            self.current_rotation == 3 and 0 < self.main_pos[1] < self.LAST_COL_IDX - 1
        ):
            self.pos0()
            self.current_rotation = 0

    def rotate_left(self) -> None:
        '''Rotates the tetromino left'''
        self.clear()
        if (
            self.current_rotation == 0
            and 1 < self.main_pos[0] < self.settings.GRID_N_OF_ROWS - 1
        ):
            self.pos3()
            self.current_rotation = 3
        elif self.current_rotation == 1 and 1 < self.main_pos[1] < self.LAST_COL_IDX:
            self.pos2()
            self.current_rotation = 0
        elif (
            self.current_rotation == 2
            and 0 < self.main_pos[0] < self.settings.GRID_N_OF_ROWS - 2
        ):
            self.pos1()
            self.current_rotation = 1
        elif (
            self.current_rotation == 3 and 0 < self.main_pos[1] < self.LAST_COL_IDX - 1
        ):
            self.pos0()
            self.current_rotation = 2

    def pos0(self) -> None:
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0], self.main_pos[1] + 1]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0], self.main_pos[1] + 2]
        if not self.check_cell_available_for_rotation(new3):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos1(self) -> None:
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0] + 2, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new3):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos2(self) -> None:
        new0 = [self.main_pos[0], self.main_pos[1] + 1]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0], self.main_pos[1] - 1]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0], self.main_pos[1] - 2]
        if not self.check_cell_available_for_rotation(new3):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos3(self) -> None:
        new0 = [self.main_pos[0] + 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0] - 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0] - 2, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new3):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3


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
        '''
        Calls the parent class constructor

        Args:
            game (Game): Game object
        '''
        super().__init__(game)

    def rotate_right(self) -> None:
        '''Do nothing because the tetromino is a square'''
        pass

    def rotate_left(self) -> None:
        '''Do nothing because the tetromino is a square'''
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
        '''
        Calls the parent class constructor

        Args:
            game (Game): Game object
        '''
        super().__init__(game)

    def pos0(self) -> None:
        '''Set the tetromino to position 0'''
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0], self.main_pos[1] + 1]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0], self.main_pos[1] - 1]
        if not self.check_cell_available_for_rotation(new3):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos1(self) -> None:
        '''Set the tetromino to position 1'''
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0], self.main_pos[1] + 1]
        if not self.check_cell_available_for_rotation(new3):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos2(self) -> None:
        '''Set the tetromino to position 2'''
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0], self.main_pos[1] + 1]
        if not self.check_cell_available_for_rotation(new3):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos3(self) -> None:
        '''Set the tetromino to position 3'''
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0], self.main_pos[1] - 1]
        if not self.check_cell_available_for_rotation(new3):
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
        '''
        Calls the parent class constructor

        Args:
            game (Game): Game object
        '''
        super().__init__(game)

    def pos0(self) -> None:
        '''Set the tetromino to position 0'''
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0] - 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0] - 1, self.main_pos[1] + 1]
        if not self.check_cell_available_for_rotation(new3):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos1(self) -> None:
        '''Set the tetromino to position 1'''
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0], self.main_pos[1] + 1]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1] + 1]
        if not self.check_cell_available_for_rotation(new3):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos2(self) -> None:
        '''Set the tetromino to position 2'''
        new0 = [self.main_pos[0] + 1, self.main_pos[1] - 1]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0], self.main_pos[1] + 1]
        if not self.check_cell_available_for_rotation(new3):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos3(self) -> None:
        '''Set the tetromino to position 3'''
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0] - 1, self.main_pos[1] - 1]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new3):
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
        '''
        Calls the parent class constructor

        Args:
            game (Game): Game object
        '''
        super().__init__(game)

    def pos0(self) -> None:
        '''Set the tetromino to position 0'''
        new0 = [self.main_pos[0] - 1, self.main_pos[1] - 1]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0] - 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0], self.main_pos[1] + 1]
        if not self.check_cell_available_for_rotation(new3):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos1(self) -> None:
        '''Set the tetromino to position 1'''
        new0 = [self.main_pos[0] + 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0], self.main_pos[1] + 1]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0] - 1, self.main_pos[1] + 1]
        if not self.check_cell_available_for_rotation(new3):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos2(self) -> None:
        '''Set the tetromino to position 2'''
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1] + 1]
        if not self.check_cell_available_for_rotation(new3):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos3(self) -> None:
        '''Set the tetromino to position 3'''
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0] - 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1] - 1]
        if not self.check_cell_available_for_rotation(new3):
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
        '''
        Calls the parent class constructor

        Args:
            game (Game): Game object
        '''
        super().__init__(game)

    def pos0(self) -> None:
        '''Set the tetromino to position 0'''
        new0 = [self.main_pos[0] - 1, self.main_pos[1] - 1]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0], self.main_pos[1] - 1]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0], self.main_pos[1] + 1]
        if not self.check_cell_available_for_rotation(new3):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos1(self) -> None:
        '''Set the tetromino to position 1'''
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0] - 1, self.main_pos[1] + 1]
        if not self.check_cell_available_for_rotation(new3):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos2(self) -> None:
        '''Set the tetromino to position 2'''
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0], self.main_pos[1] + 1]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1] + 1]
        if not self.check_cell_available_for_rotation(new3):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos3(self) -> None:
        '''Set the tetromino to position 3'''
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1] - 1]
        if not self.check_cell_available_for_rotation(new3):
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
        '''
        Calls the parent class constructor

        Args:
            game (Game): Game object
        '''
        super().__init__(game)

    def pos0(self) -> None:
        '''Set the tetromino to position 0'''
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0], self.main_pos[1] + 1]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0] - 1, self.main_pos[1] + 1]
        if not self.check_cell_available_for_rotation(new3):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos1(self) -> None:
        '''Set the tetromino to position 1'''
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0] + 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1] + 1]
        if not self.check_cell_available_for_rotation(new3):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos2(self) -> None:
        '''Set the tetromino to position 2'''
        new0 = [self.main_pos[0], self.main_pos[1] - 1]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0], self.main_pos[1] + 1]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1] - 1]
        if not self.check_cell_available_for_rotation(new3):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3

    def pos3(self) -> None:
        '''Set the tetromino to position 3'''
        new0 = [self.main_pos[0] - 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new0):
            return
        new2 = [self.main_pos[0] - 1, self.main_pos[1] - 1]
        if not self.check_cell_available_for_rotation(new2):
            return
        new3 = [self.main_pos[0] + 1, self.main_pos[1]]
        if not self.check_cell_available_for_rotation(new3):
            return
        self.pos[0] = new0
        self.pos[2] = new2
        self.pos[3] = new3
