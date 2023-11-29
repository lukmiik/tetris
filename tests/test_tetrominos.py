from unittest import TestCase

from game import Game
from settings import Settings
from tetrominos import Tetromino


class TestTetromino(TestCase):
    CHECK_DOWN_POS = [
        [Settings.GRID_N_OF_ROWS - 1, Tetromino.LAST_COL_IDX // 2 - 1],
        [Settings.GRID_N_OF_ROWS - 1, Tetromino.LAST_COL_IDX // 2],
        [Settings.GRID_N_OF_ROWS - 1, Tetromino.LAST_COL_IDX // 2 + 1],
        [Settings.GRID_N_OF_ROWS - 1, Tetromino.LAST_COL_IDX // 2 + 2],
    ]
    LEFT_EDGE_POS = [[1, col] for col in range(4)]
    RIGHT_EDGE_POS = [
        [1, col]
        for col in range(Tetromino.LAST_COL_IDX, Tetromino.LAST_COL_IDX - 4, -1)
    ]

    @classmethod
    def setUpClass(cls) -> None:
        cls.settings = Settings()
        cls.game = Game(cls.settings)
        cls.pos = [
            [1, Tetromino.LAST_COL_IDX // 2 - 1],
            [1, Tetromino.LAST_COL_IDX // 2],
            [1, Tetromino.LAST_COL_IDX // 2 + 1],
            [1, Tetromino.LAST_COL_IDX // 2 + 2],
        ]
        cls.tag = "tag"
        cls.next_tetromino_grid_pos = [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
        ]
        cls.tetromino = Tetromino(
            cls.game, cls.pos, cls.tag, cls.next_tetromino_grid_pos
        )

    def test_check_down(self) -> None:
        self.assertFalse(self.tetromino.check_down())
        self.tetromino.pos = self.CHECK_DOWN_POS
        self.assertTrue(self.tetromino.check_down())

    def test_check_touch(self) -> None:
        self.assertFalse(self.tetromino.check_touch())
        self.tetromino.grid[2] = ["tag2" for _ in range(Settings.GRID_N_OF_COL)]  # type: ignore
        self.assertTrue(self.tetromino.check_touch())

    def test_check_move_left(self) -> None:
        self.assertFalse(self.tetromino.check_move_left())
        self.tetromino.pos = self.LEFT_EDGE_POS
        self.assertTrue(self.tetromino.check_move_left())
        self.tetromino.pos = [[1, col + 1] for col in range(4)]
        self.tetromino.grid[1][0] = "tag2"  # type: ignore
        self.assertTrue(self.tetromino.check_move_left())

    def test_check_move_right(self) -> None:
        self.assertFalse(self.tetromino.check_move_right())
        self.tetromino.pos = self.RIGHT_EDGE_POS
        self.assertTrue(self.tetromino.check_move_right())
        self.tetromino.pos = [
            [1, col]
            for col in range(
                self.tetromino.LAST_COL_IDX - 1, self.tetromino.LAST_COL_IDX - 5, -1
            )
        ]
        self.tetromino.grid[1][self.tetromino.LAST_COL_IDX] = "tag2"  # type: ignore
        self.assertTrue(self.tetromino.check_move_right())
