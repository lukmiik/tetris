import random
from copy import deepcopy
from unittest import TestCase

from game import Game
from settings import Settings
from tetrominos import Itetromino, Tetromino


class TestGame(TestCase):
    CHECK_TETROMINO_GRID = [
        [
            Itetromino.TAG if row == 1 else Settings.EMPTY_CELL_TAG
            for col in range(Settings.GRID_N_OF_COL)
        ]
        for row in range(Settings.GRID_N_OF_ROWS)
    ]
    CHECK_LINE_FALSE_GRID = [
        [
            Itetromino.TAG if row == 1 else Settings.EMPTY_CELL_TAG
            for col in range(Settings.GRID_N_OF_COL)
        ]
        for row in range(Settings.GRID_N_OF_ROWS)
    ]
    CHECK_LINE_TRUE_GRID = [
        [
            Itetromino.TAG
            if row == Settings.GRID_N_OF_COL - 1
            else Settings.EMPTY_CELL_TAG
            for col in range(Settings.GRID_N_OF_COL)
        ]
        for row in range(Settings.GRID_N_OF_ROWS)
    ]
    DELETE_LINE_BEFORE_GRID = [
        [0, 0, 0, 0, 0, 'L', 0, 0, 0, 0],
        [0, 0, 0, 'L', 'L', 'L', 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 'O', 'O', 0, 0, 0, 0],
        ['I', 'I', 'I', 'I', 'O', 'O', 0, 0, 0, 0],
        [0, 'T', 0, 0, 0, 'Z', 0, 'J', 'J', 0],
        [0, 'T', 'T', 0, 'Z', 'Z', 0, 'J', 'O', 'O'],
        [0, 'T', 0, 0, 'Z', 0, 0, 'J', 'O', 'O'],
        ['Z', 'Z', 0, 'O', 'O', 0, 0, 0, 0, 'L'],
        [0, 'Z', 'Z', 'O', 'O', 'L', 0, 'L', 'L', 'L'],
        [0, 'Z', 'Z', 'L', 'L', 'L', 0, 'Z', 'Z', 0],
        ['O', 'O', 'Z', 'Z', 'I', 'I', 'I', 'I', 'Z', 'Z'],
        ['O', 'O', 0, 'O', 'O', 0, 0, 0, 0, 0],
        [0, 0, 0, 'O', 'O', 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 'S', 'S', 0, 0, 0, 0],
        [0, 0, 0, 'S', 'S', 0, 0, 'O', 'O', 0],
        [0, 0, 'L', 'O', 'O', 0, 0, 'O', 'O', 'L'],
        ['L', 'L', 'L', 'O', 'O', 0, 0, 'L', 'L', 'L'],
    ]
    DELETE_LINE_AFTER_GRID = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 'L', 0, 0, 0, 0],
        [0, 0, 0, 'L', 'L', 'L', 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 'O', 'O', 0, 0, 0, 0],
        ['I', 'I', 'I', 'I', 'O', 'O', 0, 0, 0, 0],
        [0, 'T', 0, 0, 0, 'Z', 0, 'J', 'J', 0],
        [0, 'T', 'T', 0, 'Z', 'Z', 0, 'J', 'O', 'O'],
        [0, 'T', 0, 0, 'Z', 0, 0, 'J', 'O', 'O'],
        ['Z', 'Z', 0, 'O', 'O', 0, 0, 0, 0, 'L'],
        [0, 'Z', 'Z', 'O', 'O', 'L', 0, 'L', 'L', 'L'],
        [0, 'Z', 'Z', 'L', 'L', 'L', 0, 'Z', 'Z', 0],
        ['O', 'O', 0, 'O', 'O', 0, 0, 0, 0, 0],
        [0, 0, 0, 'O', 'O', 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 'S', 'S', 0, 0, 0, 0],
        [0, 0, 0, 'S', 'S', 0, 0, 'O', 'O', 0],
        [0, 0, 'L', 'O', 'O', 0, 0, 'O', 'O', 'L'],
        ['L', 'L', 'L', 'O', 'O', 0, 0, 'L', 'L', 'L'],
    ]
    CLEAR_GRID = [
        [Settings.EMPTY_CELL_TAG for col in range(Settings.GRID_N_OF_COL)]
        for row in range(Settings.GRID_N_OF_ROWS)
    ]
    CLEAR_NEXT_TETROMINO_GRID = [
        [Settings.EMPTY_CELL_TAG for col in range(Settings.NEXT_TETROMINO_N_OF_COL)]
        for row in range(Settings.NEXT_TETROMINO_N_OF_ROWS)
    ]

    @classmethod
    def setUpClass(cls) -> None:
        cls.settings = Settings()
        cls.game = Game(cls.settings)

    def test_check_line(self) -> None:
        self.assertFalse(self.game.check_line())
        self.game.grid = self.CHECK_LINE_FALSE_GRID  # type: ignore
        self.assertFalse(self.game.check_line())
        self.game.grid = self.CHECK_LINE_TRUE_GRID  # type: ignore
        self.assertTrue(self.game.check_line())
        self.assertFalse(self.game.check_line())

    def test_delete_line(self) -> None:
        self.game.grid = self.DELETE_LINE_BEFORE_GRID  # type: ignore
        self.game.delete_line(15)
        self.assertEqual(self.game.grid, self.DELETE_LINE_AFTER_GRID)

    def test_check_tetromino_above_top(self) -> None:
        self.assertFalse(self.game.check_tetromino_above_top())
        self.game.grid = self.CHECK_TETROMINO_GRID  # type: ignore
        self.assertTrue(self.game.check_tetromino_above_top())

    def test_random_tetromino(self) -> None:
        tetromino = self.game.random_tetromino()
        self.assertIsInstance(tetromino, Tetromino)

    def test_reset_properties(self) -> None:
        self.game.grid = [
            [random.randint(1, 10) for col in range(Settings.GRID_N_OF_COL)]
            for row in range(Settings.GRID_N_OF_ROWS)
        ]
        self.game.next_tetromino_grid = [
            [random.randint(1, 10) for col in range(Settings.NEXT_TETROMINO_N_OF_COL)]
            for row in range(Settings.NEXT_TETROMINO_N_OF_ROWS)
        ]
        self.game.reset_properties()
        self.assertEqual(self.game.grid, self.CLEAR_GRID)
        self.assertEqual(self.game.next_tetromino_grid, self.CLEAR_NEXT_TETROMINO_GRID)
