import pygame


class Settings:
    SCREEN_WIDTH: int = 1000
    SCREEN_HEIGHT: int = 800
    BG_COLOR: tuple = (0, 0, 100)
    SECOND_BG_COLOR: tuple = (0, 0, 0)
    FONT_NAME: str = 'Tahoma'
    FONT_SIZE: int = 80
    FONT_SIZE_SCORE_NEXT_TITLES = 60
    FONT_COLOR: tuple = (255, 255, 255)
    TETRIS_TITLE: str = "TETRIS"
    SCORE_TITLE: str = "SCORE"
    NEXT_TETROMINO_TITLE: str = "NEXT"
    FPS: int = 60
    GAME_WINDOW_WIDTH: int = 400
    GAME_WINDOW_HEIGHT: int = 600
    BORDER_COLOR: tuple = (255, 0, 0)
    CELL_BORDER_COLOR: tuple = (119, 136, 153)
    GRID_N_OF_COL: int = 10
    GRID_N_OF_ROWS: int = 22
    GRID_CELL_WIDTH: int = GAME_WINDOW_WIDTH // GRID_N_OF_COL
    GRID_CELL_HEIGHT: int = GAME_WINDOW_HEIGHT // (GRID_N_OF_ROWS - 2)
    EMPTY_CELL_TAG: int = 0
    I: tuple = (0, 255, 255)  # cyan
    O: tuple = (255, 255, 0)  # żółty
    T: tuple = (128, 0, 128)  # fioletowy
    S: tuple = (0, 255, 0)  # zielony
    Z: tuple = (255, 0, 0)  # czerwony
    J: tuple = (0, 0, 255)  # niebieski
    L: tuple = (255, 165, 0)  # pomarańczowy
    SCORE_NEXT_WINDOW_WIDTH: int = 220
    SCORE_NEXT_WINDOW_HEIGHT: int = 150
    SCORE_WINDOW_X: int = 40
    SCORE_WINDOW_Y: int = 200
    NEXT_WINDOW_X: int = 740
    NEXT_WINDOW_Y: int = 200
    NEXT_TETROMINO_N_OF_COL: int = 4
    NEXT_TETROMINO_N_OF_ROWS: int = 4
    NEXT_TETROMINO_CELL_WIDTH: int = SCORE_NEXT_WINDOW_WIDTH // NEXT_TETROMINO_N_OF_COL
    NEXT_TETROMINO_CELL_HEIGHT: int = (
        SCORE_NEXT_WINDOW_HEIGHT // NEXT_TETROMINO_N_OF_ROWS
    )
    MOVE_DOWN_TIME: int = 1000
    CHECK_KEYS_PRESSED_MOVEMENT_TIME: int = 50
    CHECK_KEYS_PRESSED_ROTATION_TIME: int = 150

    def __init__(self) -> None:
        # necessary inits
        pygame.init()
        pygame.display.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.font = pygame.font.SysFont(self.FONT_NAME, self.FONT_SIZE)
        self.font_score_text = pygame.font.SysFont(self.FONT_NAME, 30)
        self.font_score_next_titles = pygame.font.SysFont(self.FONT_NAME, 30)
        self.create_titles_properties()

    def create_titles_properties(self) -> None:
        self.tetris_title_rendered = self.font.render(
            self.TETRIS_TITLE, True, self.FONT_COLOR
        )
        self.tetris_title_rendered_width = self.tetris_title_rendered.get_width()
        self.tetris_title_coordinates = (
            self.SCREEN_WIDTH / 2 - self.tetris_title_rendered_width / 2,
            50,
        )
        self.score_title_rendered = self.font_score_next_titles.render(
            self.SCORE_TITLE, True, self.FONT_COLOR
        )
        self.score_title_rendered_width = self.score_title_rendered.get_width()
        self.score_title_coordinates = (
            self.SCORE_WINDOW_X
            + self.SCORE_NEXT_WINDOW_WIDTH / 2
            - self.score_title_rendered_width / 2,
            150,
        )
        self.next_tetromino_title_rendered = self.font_score_next_titles.render(
            self.NEXT_TETROMINO_TITLE, True, self.FONT_COLOR
        )
        self.next_tetromino_title_rendered_width = (
            self.next_tetromino_title_rendered.get_width()
        )
        self.next_tetromino_title_coordinates = (
            self.NEXT_WINDOW_X
            + self.SCORE_NEXT_WINDOW_WIDTH / 2
            - self.next_tetromino_title_rendered_width / 2,
            150,
        )

    def draw_tetris_title(self) -> None:
        self.screen.blit(
            self.tetris_title_rendered,
            (self.tetris_title_coordinates),
        )
