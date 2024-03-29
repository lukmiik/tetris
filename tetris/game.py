import random
import sys
import time
from typing import TYPE_CHECKING

import pygame
import pygame_gui

from .db.models.user import User, user_exists
from .tetrominos import (
    Itetromino,
    Jtetromino,
    Ltetromino,
    Otetromino,
    Stetromino,
    Tetromino,
    Ttetromino,
    Ztetromino,
)

if TYPE_CHECKING:
    from .settings import Settings


class Game:
    '''Class contains main game logic and methods to draw game elements'''

    game_window: pygame.Surface
    game_window_rect: pygame.Rect
    next_tetromino_window: pygame.Surface
    next_tetromino_window_rect: pygame.Rect
    score_window: pygame.Surface
    score_window_rect: pygame.Rect
    lvl_window: pygame.Surface
    lvl_window_rect: pygame.Rect
    grid: list[list[int]]
    next_tetromino_grid: list[list[int]]
    username: str
    score: int
    lvl: int
    lines_cleared: int
    move_down_key_pressed: bool = False
    space_down: bool = False

    def __init__(self, settings: 'Settings') -> None:
        """
        Create game windows and initialize the Game properties

        Args:
            settings (Settings): The settings object that contains game configurations
        """
        self.settings = settings
        self.screen = self.settings.screen
        self.create_game_windows()
        self.init_properties()

    def create_game_windows(self) -> None:
        '''Create game windows'''
        self.game_window = pygame.Surface(
            (self.settings.GAME_WINDOW_WIDTH, self.settings.GAME_WINDOW_HEIGHT)
        )
        self.game_window_rect = self.game_window.get_rect()
        self.score_window = pygame.Surface(
            (
                self.settings.INFO_WINDOW_WIDTH,
                self.settings.INFO_WINDOW_HEIGHT,
            )
        )
        self.score_window_rect = self.score_window.get_rect()
        self.lvl_window = pygame.Surface(
            (
                self.settings.INFO_WINDOW_WIDTH,
                self.settings.INFO_WINDOW_HEIGHT,
            )
        )
        self.lvl_window_rect = self.lvl_window.get_rect()
        self.next_tetromino_window = pygame.Surface(
            (
                self.settings.INFO_WINDOW_WIDTH,
                self.settings.INFO_WINDOW_HEIGHT,
            )
        )
        self.next_tetromino_window_rect = self.next_tetromino_window.get_rect()

    def init_properties(self) -> None:
        '''Initialize game properties'''
        self.grid = [
            [self.settings.EMPTY_CELL_TAG for col in range(self.settings.GRID_N_OF_COL)]
            for row in range(self.settings.GRID_N_OF_ROWS)
        ]
        self.next_tetromino_grid = [
            [
                self.settings.EMPTY_CELL_TAG
                for col in range(self.settings.NEXT_TETROMINO_N_OF_COL)
            ]
            for row in range(self.settings.NEXT_TETROMINO_N_OF_ROWS)
        ]
        self.score = 0
        self.lvl = 1
        self.lines_cleared = 0
        self.move_down_key_pressed = False
        self.space_down = False

    def get_username(self) -> None:
        self.manager = pygame_gui.UIManager(
            (self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT)
        )
        self.username_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(
                (
                    self.settings.GET_USERNAME_INPUT_BOX_X,
                    self.settings.GET_USERNAME_INPUT_BOX_Y,
                ),
                (
                    self.settings.GET_USERNAME_INPUT_BOX_WIDTH,
                    self.settings.GET_USERNAME_INPUT_BOX_HEIGHT,
                ),
            ),
            manager=self.manager,
            object_id='#u',
        )
        clock = pygame.time.Clock()
        self.screen.fill(self.settings.BG_COLOR)
        self.screen.blit(
            self.settings.get_username_text, self.settings.get_username_input_rect
        )
        while True:
            UI_REFRESH_RATE = clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if (
                    event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED
                    and event.ui_object_id == '#u'
                ):
                    if event.text:
                        self.username = event.text
                        return
                self.manager.process_events(event)
            self.manager.update(UI_REFRESH_RATE)
            self.manager.draw_ui(self.screen)
            pygame.display.update()

    def draw_grid(self) -> None:
        '''Draw grid with tetrominos on game window'''
        self.game_window.fill(self.settings.SECOND_BG_COLOR)
        for row, list in enumerate(self.grid[2:], 0):
            for col, value in enumerate(list):
                if value == self.settings.EMPTY_CELL_TAG:
                    pygame.draw.rect(
                        self.game_window,
                        self.settings.CELL_BORDER_COLOR,
                        (
                            col * self.settings.GRID_CELL_WIDTH,
                            row * self.settings.GRID_CELL_HEIGHT,
                            self.settings.GRID_CELL_WIDTH,
                            self.settings.GRID_CELL_HEIGHT,
                        ),
                        1,
                    )
                else:
                    tetromino_color = getattr(self.settings, str(value))
                    pygame.draw.rect(
                        self.game_window,
                        tetromino_color,
                        (
                            col * self.settings.GRID_CELL_WIDTH,
                            row * self.settings.GRID_CELL_HEIGHT,
                            self.settings.GRID_CELL_WIDTH,
                            self.settings.GRID_CELL_HEIGHT,
                        ),
                    )

    def draw_next_tetromino(self) -> None:
        '''Draw next tetromino on next tetromino window'''
        self.next_tetromino_window.fill(self.settings.SECOND_BG_COLOR)
        for row, list in enumerate(self.next_tetromino_grid):
            for col, value in enumerate(list):
                if value == self.settings.EMPTY_CELL_TAG:
                    pygame.draw.rect(
                        self.next_tetromino_window,
                        self.settings.SECOND_BG_COLOR,
                        (
                            col * self.settings.NEXT_TETROMINO_CELL_WIDTH,
                            row * self.settings.NEXT_TETROMINO_CELL_HEIGHT,
                            self.settings.NEXT_TETROMINO_CELL_WIDTH,
                            self.settings.NEXT_TETROMINO_CELL_HEIGHT,
                        ),
                    )
                else:
                    x = getattr(self.settings, str(value))
                    pygame.draw.rect(
                        self.next_tetromino_window,
                        x,
                        (
                            col * self.settings.NEXT_TETROMINO_CELL_WIDTH,
                            row * self.settings.NEXT_TETROMINO_CELL_HEIGHT,
                            self.settings.NEXT_TETROMINO_CELL_WIDTH,
                            self.settings.NEXT_TETROMINO_CELL_HEIGHT,
                        ),
                    )
        self.draw_next_tetromino_window()

    def draw_score(self) -> None:
        '''Draw score window and score on'''
        self.draw_score_window()
        score_text = self.settings.font_score_lvl_text.render(
            str(self.score), True, self.settings.FONT_COLOR
        )
        self.screen.blit(
            score_text,
            (
                (
                    self.settings.SCORE_WINDOW_X
                    + self.settings.INFO_WINDOW_WIDTH / 2
                    - score_text.get_width() / 2
                ),
                (
                    self.settings.SCORE_WINDOW_Y
                    + self.settings.INFO_WINDOW_HEIGHT / 2
                    - score_text.get_height() / 2
                ),
            ),
        )

    def draw_score_title(self) -> None:
        '''Draw score title on screen'''
        self.screen.blit(
            self.settings.score_title_rendered,
            (self.settings.score_title_coordinates),
        )

    def draw_lvl(self) -> None:
        '''Draw score window and score on'''
        self.draw_lvl_window()
        lvl_text = self.settings.font_score_lvl_text.render(
            str(self.lvl), True, self.settings.FONT_COLOR
        )
        self.screen.blit(
            lvl_text,
            (
                (
                    self.settings.LVL_WINDOW_X
                    + self.settings.INFO_WINDOW_WIDTH / 2
                    - lvl_text.get_width() / 2
                ),
                (
                    self.settings.LVL_WINDOW_Y
                    + self.settings.INFO_WINDOW_HEIGHT / 2
                    - lvl_text.get_height() / 2
                ),
            ),
        )

    def draw_lvl_title(self) -> None:
        '''Draw score title on screen'''
        self.screen.blit(
            self.settings.lvl_title_rendered,
            (self.settings.lvl_title_coordinates),
        )

    def draw_next_tetromino_title(self) -> None:
        '''Draw next tetromino title on screen'''
        self.screen.blit(
            self.settings.next_tetromino_title_rendered,
            (self.settings.next_tetromino_title_coordinates),
        )

    def draw_game_window(self) -> None:
        '''Draw game window on screen'''
        pygame.draw.rect(
            self.game_window, self.settings.GAME_BORDER_COLOR, self.game_window_rect, 5
        )
        self.screen.blit(
            self.game_window,
            (
                self.settings.SCREEN_WIDTH / 2 - self.settings.GAME_WINDOW_WIDTH / 2,
                self.settings.SCREEN_HEIGHT - self.settings.GAME_WINDOW_HEIGHT,
            ),
        )

    def draw_score_window(self) -> None:
        '''Draw score window on screen'''
        pygame.draw.rect(
            self.score_window,
            self.settings.GAME_BORDER_COLOR,
            self.score_window_rect,
            2,
        )
        self.screen.blit(
            self.score_window,
            (
                self.settings.SCORE_WINDOW_X,
                self.settings.SCORE_WINDOW_Y,
            ),
        )

    def draw_lvl_window(self) -> None:
        '''Draw score window on screen'''
        pygame.draw.rect(
            self.lvl_window,
            self.settings.GAME_BORDER_COLOR,
            self.lvl_window_rect,
            2,
        )
        self.screen.blit(
            self.lvl_window,
            (
                self.settings.LVL_WINDOW_X,
                self.settings.LVL_WINDOW_Y,
            ),
        )

    def draw_next_tetromino_window(self) -> None:
        '''Draw next tetromino window on screen'''
        pygame.draw.rect(
            self.next_tetromino_window,
            self.settings.GAME_BORDER_COLOR,
            self.next_tetromino_window_rect,
            2,
        )
        self.screen.blit(
            self.next_tetromino_window,
            (
                self.settings.NEXT_WINDOW_X,
                self.settings.NEXT_WINDOW_Y,
            ),
        )

    def check_line(self) -> bool:
        '''
        Check if there is a line of tetrominos and delete it

        Args:
            None

        Returns:
            (bool): True if there is a line of tetrominos, False otherwise
        '''
        lines_cleared_now = 0
        for row, line in enumerate(self.grid[2:], 2):
            if self.settings.EMPTY_CELL_TAG not in line:
                self.delete_line(row)
                lines_cleared_now += 1
        if lines_cleared_now:
            self.lines_cleared += lines_cleared_now
            self.add_score(lines_cleared_now)
            return True
        return False

    def delete_line(self, row) -> None:
        '''Delete line from grid and move all tetrominos above it down'''
        for r in range(row, 0, -1):
            self.grid[r] = self.grid[r - 1].copy()
        self.grid[0] = [
            self.settings.EMPTY_CELL_TAG for col in range(self.settings.GRID_N_OF_COL)
        ]

    def add_score(self, lines_cleared: int) -> None:
        '''Add score for cleared lines'''
        self.score += self.settings.POINTS_PER_LINES[lines_cleared]

    def check_lvl_up(self) -> None:
        if self.lines_cleared >= self.settings.N_OF_LINES_TO_LVL_UP * self.lvl:
            self.lvl_up()
            self.draw_lvl()

    def lvl_up(self) -> None:
        self.lvl += 1
        self.settings.move_down_time -= self.settings.MOVE_DOWN_ACCELERATION_PER_LVL
        pygame.time.set_timer(pygame.USEREVENT, self.settings.move_down_time)

    def check_tetromino_above_top(self) -> bool:
        '''Check if there is a tetromino above visible top of the grid'''
        for x in range(self.settings.GRID_N_OF_COL):
            if self.grid[1][x] != 0:
                return True
        return False

    def draw_end_of_game_btns(self) -> None:
        '''Draw buttons displayed at the end of the game, after loss'''
        pygame.draw.rect(
            self.screen,
            self.settings.END_OF_BTNS_COLOR,
            self.settings.end_of_game_menu_btn,
        )
        self.screen.blit(
            self.settings.end_of_game_menu_btn_text,
            (
                self.settings.end_of_game_menu_btn.centerx
                - self.settings.end_of_game_menu_btn_text.get_width() / 2,
                self.settings.end_of_game_menu_btn.centery
                - self.settings.end_of_game_menu_btn_text.get_height() / 2,
            ),
        )
        pygame.draw.rect(
            self.screen,
            self.settings.END_OF_BTNS_COLOR,
            self.settings.end_of_game_next_btn,
        )
        self.screen.blit(
            self.settings.end_of_game_next_btn_text,
            (
                self.settings.end_of_game_next_btn.centerx
                - self.settings.end_of_game_next_btn_text.get_width() / 2,
                self.settings.end_of_game_next_btn.centery
                - self.settings.end_of_game_next_btn_text.get_height() / 2,
            ),
        )

    def next_game(self) -> bool:
        '''Check if user clicked on next game button or menu button'''
        while True:
            self.check_hover()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.settings.end_of_game_menu_btn.collidepoint(event.pos):
                        return False
                    elif self.settings.end_of_game_next_btn.collidepoint(event.pos):
                        return True

    def check_hover(self) -> None:
        '''Checks if mouse is hovering over the buttons and changes the cursor accordingly'''
        if self.settings.end_of_game_menu_btn.collidepoint(
            pygame.mouse.get_pos()
        ) or self.settings.end_of_game_next_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def db_insert_user(self) -> None:
        '''Insert user into database'''
        if user_exists(self.username):
            user = User.get(User.username == self.username)
            if self.score > user.highest_score:
                user.highest_score = self.score
                user.lvl = self.lvl
            user.save()
        else:
            user = User(username=self.username, highest_score=self.score, lvl=self.lvl)
            user.save()

    def check_events(self) -> None:
        '''Check pygane events and react to them'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT and not self.move_down_key_pressed:
                self.current_tetromino.move_down()
            if event.type == pygame.USEREVENT + 1:
                self.check_pressed_down_movement()
            if event.type == pygame.USEREVENT + 2:
                self.check_pressed_side_movement()
            if event.type == pygame.USEREVENT + 3:
                self.check_pressed_rotate()

    def check_pressed_down_movement(self) -> None:
        '''Check if down movement keys are pressed and react to them'''
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
            self.current_tetromino.move_down()
            self.move_down_key_pressed = True
        else:
            self.move_down_key_pressed = False
        if keys_pressed[pygame.K_SPACE] and not self.space_down:
            self.current_tetromino.hard_drop()
            self.space_down = True
        if not keys_pressed[pygame.K_SPACE]:
            self.space_down = False

    def check_pressed_side_movement(self) -> None:
        '''Check if side movement keys are pressed and react to them'''
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            self.current_tetromino.move_right()
        if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
            self.current_tetromino.move_left()

    def check_pressed_rotate(self) -> None:
        '''Check if rotation keys are pressed and react to them'''
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
            self.current_tetromino.rotate_right()
        if keys_pressed[pygame.K_z]:
            self.current_tetromino.rotate_left()

    def random_tetromino(self) -> Tetromino:
        '''
        Return random tetromino

        Returns:
            (Tetromino): Random tetromino
        '''
        tetrominos = [
            Itetromino,
            Ttetromino,
            Otetromino,
            Stetromino,
            Ztetromino,
            Jtetromino,
            Ltetromino,
        ]
        random_tetromino = random.choice(tetrominos)
        return random_tetromino(self)

    def print_grid(self) -> None:
        '''Print grid in console'''
        for row in self.grid:
            print(row)

    def main(self) -> None:
        '''Main game loop'''
        self.get_username()
        self.screen.fill(self.settings.BG_COLOR)
        clock = pygame.time.Clock()
        self.current_tetromino = self.random_tetromino()
        self.current_tetromino.update_on_grid()
        self.next_tetromino = self.random_tetromino()
        self.next_tetromino.put_on_next_tetromino_window()
        self.settings.draw_tetris_title()
        self.draw_score_title()
        self.draw_score()
        self.draw_lvl_title()
        self.draw_lvl()
        self.draw_next_tetromino_title()
        self.draw_next_tetromino()
        pygame.time.set_timer(pygame.USEREVENT, self.settings.move_down_time)
        pygame.time.set_timer(
            pygame.USEREVENT + 1, self.settings.CHECK_KEYS_PRESSED_MOVEMENT_DOWN_TIME
        )
        pygame.time.set_timer(
            pygame.USEREVENT + 2, self.settings.CHECK_KEYS_PRESSED_MOVEMENT_SIDE_TIME
        )
        pygame.time.set_timer(
            pygame.USEREVENT + 3, self.settings.CHECK_KEYS_PRESSED_ROTATION_TIME
        )
        while True:
            clock.tick(self.settings.FPS)
            self.check_events()
            self.draw_grid()
            self.draw_game_window()
            self.draw_score()
            if (
                self.current_tetromino.check_down()
                or self.current_tetromino.check_touch()
            ):
                self.current_tetromino.update_on_grid()
                if self.check_line():
                    self.check_lvl_up()
                # game lost
                if self.check_tetromino_above_top():
                    self.draw_grid()
                    self.draw_game_window()
                    pygame.display.update()
                    self.db_insert_user()
                    self.init_properties()
                    time.sleep(3)
                    self.draw_end_of_game_btns()
                    pygame.display.update()
                    if self.next_game():
                        continue
                    else:
                        break
                self.current_tetromino = self.next_tetromino
                self.current_tetromino.update_on_grid()
                self.next_tetromino = self.random_tetromino()
                self.next_tetromino.put_on_next_tetromino_window()
                self.draw_next_tetromino()
            else:
                self.current_tetromino.update_on_grid()
            pygame.display.update()
