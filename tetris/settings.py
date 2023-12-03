import pkg_resources
import pygame


class Settings:
    '''Settings class for the game'''

    SCREEN_WIDTH: int = 1000
    SCREEN_HEIGHT: int = 800
    GAME_WINDOW_WIDTH: int = 400
    GAME_WINDOW_HEIGHT: int = 600

    BG_COLOR: tuple = (0, 0, 100)
    SECOND_BG_COLOR: tuple = (0, 0, 0)
    GAME_BORDER_COLOR: tuple = (255, 0, 0)
    CELL_BORDER_COLOR: tuple = (119, 136, 153)
    LEADERBOARD_BORDER_COLOR: tuple = (128, 128, 128)

    FPS: int = 60

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

    FONT_NAME: str = 'Tahoma'
    FONT_SIZE_TETRIS_TITLE: int = 80
    FONT_SIZE_INFO_TITLES: int = 30
    FONT_SIZE_SCORE_LVL: int = 30
    FONT_SIZE_END_OF_GAME_BTNS: int = 20
    FONT_SIZE_GET_USERNAME: int = 23
    FONT_SIZE_LEADERBOARD_TITLE: int = 40
    FONT_SIZE_LEADERBOARD_HEADER: int = 20
    FONT_SIZE_LEADERBOARD: int = 15
    FONT_SIZE_CONTROLS_TITLE: int = 40
    FONT_SIZE_CONTROLS: int = 30
    FONT_SIZE_RULES_TITLE: int = 40
    FONT_SIZE_RULES: int = 30
    FONT_COLOR: tuple = (255, 255, 255)

    TETRIS_TITLE: str = "TETRIS"
    SCORE_TITLE: str = "SCORE"
    LVL_TITLE: str = "LEVEL"
    NEXT_TETROMINO_TITLE: str = "NEXT"
    LEADERBOARD_TITLE: str = "LEADERBOARD"
    LEADERBOARD_HEADERS_TEXTS: list[str] = [
        "RANK",
        "USERNAME",
        "SCORE",
        "LVL",
        "GAMES PLAYED",
    ]
    CONTROLS_TITLE: str = "CONTROLS"
    RULES_TITLE: str = "RULES"

    TETRIS_TITLE_Y: int = SCREEN_HEIGHT // 16
    SCORE_NEXT_TITLE_Y: int = SCREEN_HEIGHT // 5
    LVL_TITLE_Y: float = SCREEN_HEIGHT / 1.95
    LEADERBOARD_TITLE_Y: int = SCREEN_HEIGHT // 5
    CONTROLS_TITLE_Y: int = SCREEN_HEIGHT // 5
    RULES_TITLE_Y: int = SCREEN_HEIGHT // 5
    RULES_TEXT_Y: float = SCREEN_HEIGHT / 3
    RULES_LINE_HEIGHT: int = SCREEN_HEIGHT // 20

    MENU_START_GAME_TEXT = "Start game"
    MENU_LEADERBOARD_TEXT = "Leaderboard"
    MENU_CONTROLS_TEXT = "Controls"
    MENU_RULES_TEXT = "Rules"
    MENU_QUIT_TEXT = "Quit"

    MENU_BTNS_FIRST_Y: int = SCREEN_HEIGHT // 4
    MENU_BTNS_HEIGHT: int = SCREEN_HEIGHT // 8
    MENU_BTN_GAP: int = SCREEN_HEIGHT // 40

    INFO_WINDOW_WIDTH: int = int(SCREEN_WIDTH / 4.55)
    INFO_WINDOW_HEIGHT: int = int(SCREEN_HEIGHT / 5.3)
    SCORE_WINDOW_X: int = SCREEN_WIDTH // 25
    SCORE_WINDOW_Y: int = SCREEN_HEIGHT // 4
    LVL_WINDOW_X: int = SCREEN_WIDTH // 25
    LVL_WINDOW_Y: float = SCREEN_HEIGHT / 1.8
    NEXT_WINDOW_X: float = SCREEN_WIDTH / 1.35
    NEXT_WINDOW_Y: int = SCREEN_HEIGHT // 4
    NEXT_TETROMINO_N_OF_COL: int = 4
    NEXT_TETROMINO_N_OF_ROWS: int = 4
    NEXT_TETROMINO_CELL_WIDTH: int = INFO_WINDOW_WIDTH // NEXT_TETROMINO_N_OF_COL
    NEXT_TETROMINO_CELL_HEIGHT: int = INFO_WINDOW_HEIGHT // NEXT_TETROMINO_N_OF_ROWS

    END_OF_GAME_BTNS_WIDTH: int = SCREEN_WIDTH // 8
    END_OF_GAME_BTNS_HEIGHT: int = SCREEN_HEIGHT // 18
    END_OF_GAME_BTNS_Y: int = SCREEN_HEIGHT // 2
    END_OF_GAME_MENU_BTN_X: int = SCREEN_WIDTH // 2 - END_OF_GAME_BTNS_WIDTH - 30
    END_OF_GAME_NEXT_BTN_X: int = SCREEN_WIDTH // 2 + 30
    END_OF_BTNS_COLOR: tuple = (218, 165, 32)
    END_OF_GAME_MENU_BTN_TEXT: str = "Menu"
    END_OF_GAME_NEXT_BTN_TEXT: str = "Next"

    GET_USERNAME_INPUT_BOX_WIDTH: int = SCREEN_WIDTH // 4
    GET_USERNAME_INPUT_BOX_HEIGHT: int = SCREEN_HEIGHT // 20
    GET_USERNAME_INPUT_BOX_X: float = SCREEN_WIDTH / 1.7
    GET_USERNAME_INPUT_BOX_Y: float = SCREEN_HEIGHT / 2 - 8
    GET_USERNAME_TEXT: str = "ENTER YOUR USERNAME (ENTER)"

    GO_BACK_ICON_FILENAME: str = pkg_resources.resource_filename(
        'tetris', 'assets/arrow_back.png'
    )
    GO_BACK_BTN_X: int = 30
    GO_BACK_BTN_Y: int = 40

    LEADERBOARD_WIDTH: float = SCREEN_WIDTH / 16 * 14
    LEADERBOARD_BORDER_X: float = SCREEN_WIDTH / 16
    LEADERBOARD_HEADER_Y: float = SCREEN_HEIGHT / 3.6
    LEADERBOARD_HEADER_HEIGHT: int = SCREEN_HEIGHT // 8
    LEADERBOARD_FIRST_ROW_Y: float = (
        LEADERBOARD_HEADER_Y + LEADERBOARD_HEADER_HEIGHT + 30
    )
    LEADERBOARD_ROW_HEIGHT: float = SCREEN_HEIGHT / 20
    LEADERBOARD_HEADER_BORDER_WIDTH: int = 3
    LEADERBOARD_BORDER_WIDTH: int = 1
    LEADERBOARD_HEADER_TEXT_Y: float = (
        LEADERBOARD_HEADER_Y + LEADERBOARD_HEADER_HEIGHT / 2
    )
    LEADERBOARD_TEXT_WIDTH: float = LEADERBOARD_WIDTH // 5
    LEADERBOARD_TEXT_X: list[float] = [
        (LEADERBOARD_BORDER_X + LEADERBOARD_TEXT_WIDTH / 2) / 1.4,
        (LEADERBOARD_BORDER_X + LEADERBOARD_TEXT_WIDTH / 2) / 1.4
        + LEADERBOARD_TEXT_WIDTH,
        LEADERBOARD_BORDER_X + LEADERBOARD_TEXT_WIDTH / 2 + LEADERBOARD_TEXT_WIDTH * 2,
        LEADERBOARD_BORDER_X + LEADERBOARD_TEXT_WIDTH / 2 + LEADERBOARD_TEXT_WIDTH * 3,
        LEADERBOARD_BORDER_X + LEADERBOARD_TEXT_WIDTH / 2 + LEADERBOARD_TEXT_WIDTH * 4,
    ]

    MOVE_DOWN_START_TIME: int = 1000
    MOVE_DOWN_ACCELERATION_PER_LVL: int = 19
    HARD_DROP_LOOP_SLEEP_TIME: float = 0.01
    CHECK_KEYS_PRESSED_MOVEMENT_DOWN_TIME: int = 50
    CHECK_KEYS_PRESSED_MOVEMENT_SIDE_TIME: int = 80
    CHECK_KEYS_PRESSED_ROTATION_TIME: int = 150

    N_OF_LINES_TO_LVL_UP: int = 10
    POINTS_FOR_SOFT_DROP: int = 1
    POINTS_FOR_HARD_DROP: int = 2
    POINTS_PER_LINES: dict = {1: 100, 2: 300, 3: 500, 4: 800}

    CONTROLS_TEXTS: list[str] = [
        "move down",
        "move left",
        "move right",
        "hard drop",
        "rotate left",
        "rotate right",
    ]
    CONTROLS_TEXTS_X: float = SCREEN_WIDTH / 3
    CONTROLS_TEXTS_Y: list[float] = [
        SCREEN_HEIGHT * 4 / 10,
        SCREEN_HEIGHT * 5 / 10,
        SCREEN_HEIGHT * 6 / 10,
        SCREEN_HEIGHT * 7 / 10,
        SCREEN_HEIGHT * 8 / 10,
        SCREEN_HEIGHT * 9 / 10,
    ]
    CONTROLS_ONE_KEY_X: float = SCREEN_WIDTH * 0.65
    CONTROLS_TWO_KEYS_X: list[float] = [SCREEN_WIDTH * 0.6, SCREEN_WIDTH * 0.7]
    MOVING_DOWN_KEY_1_FILENAME: str = pkg_resources.resource_filename(
        'tetris', 'assets/s_key.png'
    )
    MOVING_DOWN_KEY_2_FILENAME: str = pkg_resources.resource_filename(
        'tetris', 'assets/down_key.png'
    )
    MOVING_LEFT_KEY_1_FILENAME: str = pkg_resources.resource_filename(
        'tetris', 'assets/a_key.png'
    )
    MOVING_LEFT_KEY_2_FILENAME: str = pkg_resources.resource_filename(
        'tetris', 'assets/left_key.png'
    )
    MOVING_RIGHT_KEY_1_FILENAME: str = pkg_resources.resource_filename(
        'tetris', 'assets/d_key.png'
    )
    MOVING_RIGHT_KEY_2_FILENAME: str = pkg_resources.resource_filename(
        'tetris', 'assets/right_key.png'
    )
    HARD_DROP_KEY_FILENAME: str = pkg_resources.resource_filename(
        'tetris', 'assets/space_key.png'
    )
    ROTATE_LEFT_KEY_FILENAME: str = pkg_resources.resource_filename(
        'tetris', 'assets/z_key.png'
    )
    ROTATE_RIGHT_KEY_1_FILENAME: str = pkg_resources.resource_filename(
        'tetris', 'assets/w_key.png'
    )
    ROTATE_RIGHT_KEY_2_FILENAME: str = pkg_resources.resource_filename(
        'tetris', 'assets/up_key.png'
    )

    def __init__(self) -> None:
        '''Initialize pygame and create the screen and font'''
        pygame.init()
        pygame.display.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.font_tetris_title = pygame.font.SysFont(
            self.FONT_NAME, self.FONT_SIZE_TETRIS_TITLE
        )
        self.font_score_lvl_text = pygame.font.SysFont(
            self.FONT_NAME, self.FONT_SIZE_SCORE_LVL
        )
        self.font_info_titles = pygame.font.SysFont(
            self.FONT_NAME, self.FONT_SIZE_INFO_TITLES
        )
        self.font_end_of_game_btns = pygame.font.SysFont(
            self.FONT_NAME, self.FONT_SIZE_END_OF_GAME_BTNS
        )
        self.font_get_username = pygame.font.SysFont(
            self.FONT_NAME, self.FONT_SIZE_GET_USERNAME, bold=True
        )
        self.font_leaderboard_title = pygame.font.SysFont(
            self.FONT_NAME, self.FONT_SIZE_LEADERBOARD_TITLE
        )
        self.font_leaderboard_header = pygame.font.SysFont(
            self.FONT_NAME, self.FONT_SIZE_LEADERBOARD_HEADER
        )
        self.font_leaderboard = pygame.font.SysFont(
            self.FONT_NAME, self.FONT_SIZE_LEADERBOARD
        )
        self.font_controls_title = pygame.font.SysFont(
            self.FONT_NAME, self.FONT_SIZE_CONTROLS_TITLE
        )
        self.font_controls = pygame.font.SysFont(
            self.FONT_NAME, self.FONT_SIZE_CONTROLS
        )
        self.font_rules_title = pygame.font.SysFont(
            self.FONT_NAME, self.FONT_SIZE_RULES_TITLE
        )
        self.font_rules = pygame.font.SysFont(self.FONT_NAME, self.FONT_SIZE_RULES)
        self.create_titles_properties()
        self.create_get_username_text()
        self.create_end_of_game_btns()
        self.go_back_icon = pygame.image.load(self.GO_BACK_ICON_FILENAME)
        self.create_go_back_btn()
        self.move_down_time = self.MOVE_DOWN_START_TIME

    def create_titles_properties(self) -> None:
        '''Create properties for the titles'''
        self.tetris_title_rendered = self.font_tetris_title.render(
            self.TETRIS_TITLE, True, self.FONT_COLOR
        )
        self.tetris_title_rendered_width = self.tetris_title_rendered.get_width()
        self.tetris_title_coordinates = (
            self.SCREEN_WIDTH / 2 - self.tetris_title_rendered_width / 2,
            self.TETRIS_TITLE_Y,
        )
        self.score_title_rendered = self.font_info_titles.render(
            self.SCORE_TITLE, True, self.FONT_COLOR
        )
        self.score_title_rendered_width = self.score_title_rendered.get_width()
        self.score_title_coordinates = (
            self.SCORE_WINDOW_X
            + self.INFO_WINDOW_WIDTH / 2
            - self.score_title_rendered_width / 2,
            self.SCORE_NEXT_TITLE_Y,
        )
        self.lvl_title_rendered = self.font_info_titles.render(
            self.LVL_TITLE, True, self.FONT_COLOR
        )
        self.lvl_title_rendered_width = self.lvl_title_rendered.get_width()
        self.lvl_title_coordinates = (
            self.LVL_WINDOW_X
            + self.INFO_WINDOW_WIDTH / 2
            - self.lvl_title_rendered_width / 2,
            self.LVL_TITLE_Y,
        )
        self.next_tetromino_title_rendered = self.font_info_titles.render(
            self.NEXT_TETROMINO_TITLE, True, self.FONT_COLOR
        )
        self.next_tetromino_title_rendered_width = (
            self.next_tetromino_title_rendered.get_width()
        )
        self.next_tetromino_title_coordinates = (
            self.NEXT_WINDOW_X
            + self.INFO_WINDOW_WIDTH / 2
            - self.next_tetromino_title_rendered_width / 2,
            self.SCORE_NEXT_TITLE_Y,
        )

    def draw_tetris_title(self) -> None:
        '''Draws the tetris title'''
        self.screen.blit(
            self.tetris_title_rendered,
            (self.tetris_title_coordinates),
        )

    def create_get_username_text(self) -> None:
        '''Creates the input box for the username'''
        self.get_username_text = self.font_get_username.render(
            self.GET_USERNAME_TEXT, True, self.FONT_COLOR
        )
        self.get_username_input_rect = self.get_username_text.get_rect(
            topleft=(
                self.SCREEN_WIDTH / 6,
                self.SCREEN_HEIGHT / 2,
            )
        )

    def create_end_of_game_btns(self) -> None:
        '''Creates buttons displayed after the game is lost'''
        self.end_of_game_menu_btn = pygame.Rect(
            self.END_OF_GAME_MENU_BTN_X,
            self.END_OF_GAME_BTNS_Y,
            self.END_OF_GAME_BTNS_WIDTH,
            self.END_OF_GAME_BTNS_HEIGHT,
        )
        self.end_of_game_next_btn = pygame.Rect(
            self.END_OF_GAME_NEXT_BTN_X,
            self.END_OF_GAME_BTNS_Y,
            self.END_OF_GAME_BTNS_WIDTH,
            self.END_OF_GAME_BTNS_HEIGHT,
        )
        self.end_of_game_menu_btn_text = self.font_end_of_game_btns.render(
            self.END_OF_GAME_MENU_BTN_TEXT, True, self.FONT_COLOR
        )
        self.end_of_game_next_btn_text = self.font_end_of_game_btns.render(
            self.END_OF_GAME_NEXT_BTN_TEXT, True, self.FONT_COLOR
        )

    def create_go_back_btn(self) -> None:
        '''Creates the go back button'''
        self.go_back_btn_rect = pygame.Rect(
            self.GO_BACK_BTN_X,
            self.GO_BACK_BTN_Y,
            self.go_back_icon.get_width(),
            self.go_back_icon.get_height(),
        )

    def draw_go_back_btn(self) -> None:
        '''Draws the go back button'''
        self.screen.blit(
            self.go_back_icon,
            self.go_back_icon.get_rect(center=self.go_back_btn_rect.center),
        )

    def check_go_back_btn_hover(self) -> None:
        '''Checks if mouse is hovering over the go_back button and changes the cursor accordingly'''
        if self.go_back_btn_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
