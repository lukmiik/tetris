from unittest import TestCase

from tetris.game import Game
from tetris.settings import Settings
from tetris.tetrominos import Itetromino, Tetromino


class TestTetromino(TestCase):
    """
    Test case class for testing the Tetromino class.
    """

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
        '''
        Set up the test class by initializing the settings, game, and tetromino objects.

        Args:
            cls: The class object.

        Returns:
            None
        '''
        cls.settings = Settings()
        cls.game = Game(cls.settings)
        cls.tetromino = Itetromino(cls.game)

    def test_check_down(self) -> None:
        '''Test the check down method of the Tetromino class.'''
        self.assertFalse(self.tetromino.check_down())
        self.tetromino.pos = self.CHECK_DOWN_POS
        self.assertTrue(self.tetromino.check_down())

    def test_check_touch(self) -> None:
        '''Test the check touch method of the Tetromino class.'''
        self.assertFalse(self.tetromino.check_touch())
        self.tetromino.grid[2] = ["tag2" for _ in range(Settings.GRID_N_OF_COL)]  # type: ignore
        self.assertTrue(self.tetromino.check_touch())

    def test_check_move_left(self) -> None:
        '''Test the check move left method of the Tetromino class.'''
        self.assertFalse(self.tetromino.check_move_left())
        self.tetromino.pos = self.LEFT_EDGE_POS
        self.assertTrue(self.tetromino.check_move_left())
        self.tetromino.pos = [[1, col + 1] for col in range(4)]
        self.tetromino.grid[1][0] = "tag2"  # type: ignore
        self.assertTrue(self.tetromino.check_move_left())

    def test_check_move_right(self) -> None:
        '''Test the check move right method of the Tetromino class.'''
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
