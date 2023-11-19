import pygame
import sys
import time
import random

from tetrominos import (
    Tetromino,
    Itetromino,
    Ttetromino,
    Otetromino,
    Stetromino,
    Ztetromino,
    Jtetromino,
    Ltetromino,
)
from settings import Settings


class Game:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.screen = self.settings.screen
        self.game_window = pygame.Surface(
            (self.settings.GAME_WINDOW_WIDTH, self.settings.GAME_WINDOW_HEIGHT)
        )
        self.game_window_rect = self.game_window.get_rect()
        self.next_tetromino_window = pygame.Surface(
            (
                self.settings.SCORE_NEXT_WINDOW_WIDTH,
                self.settings.SCORE_NEXT_WINDOW_HEIGHT,
            )
        )
        self.next_tetromino_window_rect = self.next_tetromino_window.get_rect()
        self.score_window = pygame.Surface(
            (
                self.settings.SCORE_NEXT_WINDOW_WIDTH,
                self.settings.SCORE_NEXT_WINDOW_HEIGHT,
            )
        )
        self.score_window_rect = self.score_window.get_rect()
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

    def draw_grid(self) -> None:
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
                    x = getattr(self.settings, str(value))
                    pygame.draw.rect(
                        self.game_window,
                        x,
                        (
                            col * self.settings.GRID_CELL_WIDTH,
                            row * self.settings.GRID_CELL_HEIGHT,
                            self.settings.GRID_CELL_WIDTH,
                            self.settings.GRID_CELL_HEIGHT,
                        ),
                    )

    def draw_next_tetromino(self) -> None:
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
        self.draw_score_window()
        score_text = self.settings.font_score_text.render(
            str(self.score), True, self.settings.FONT_COLOR
        )
        self.screen.blit(
            score_text,
            (
                (
                    self.settings.SCORE_WINDOW_X
                    + self.settings.SCORE_NEXT_WINDOW_WIDTH / 2
                    - score_text.get_width() / 2
                ),
                (
                    self.settings.SCORE_WINDOW_Y
                    + self.settings.SCORE_NEXT_WINDOW_HEIGHT / 2
                    - score_text.get_height() / 2
                ),
            ),
        )

    def draw_score_title(self) -> None:
        self.screen.blit(
            self.settings.score_title_rendered,
            (self.settings.score_title_coordinates),
        )

    def draw_next_tetromino_title(self) -> None:
        self.screen.blit(
            self.settings.next_tetromino_title_rendered,
            (self.settings.next_tetromino_title_coordinates),
        )

    def draw_game_window(self) -> None:
        pygame.draw.rect(
            self.game_window, self.settings.BORDER_COLOR, self.game_window_rect, 5
        )
        self.screen.blit(
            self.game_window,
            (
                self.settings.SCREEN_WIDTH / 2 - self.settings.GAME_WINDOW_WIDTH / 2,
                self.settings.SCREEN_HEIGHT - self.settings.GAME_WINDOW_HEIGHT,
            ),
        )

    def draw_next_tetromino_window(self) -> None:
        pygame.draw.rect(
            self.next_tetromino_window,
            self.settings.BORDER_COLOR,
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

    def draw_score_window(self) -> None:
        pygame.draw.rect(
            self.score_window,
            self.settings.BORDER_COLOR,
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

    def check_line(self) -> None:
        for row, line in enumerate(self.grid[2:], 2):
            if 0 not in line:
                self.delete_line(row)

    def delete_line(self, row) -> None:
        for r in range(row, 1, -1):
            self.grid[r] = self.grid[r - 1].copy()

    def check_tetromino_above_top(self) -> bool:
        for x in range(self.settings.GRID_N_OF_COL):
            if self.grid[1][x] != 0:
                return True
        return False

    def check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT and not self.down:
                self.current_tetromino.move_down()
            if event.type == pygame.USEREVENT + 1:
                self.check_pressed()
            if event.type == pygame.USEREVENT + 2:
                self.check_rotate()

    def check_pressed(self) -> None:
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
            self.current_tetromino.move_down()
            self.down = True
        else:
            self.down = False
        if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            self.current_tetromino.move_right()
        if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
            self.current_tetromino.move_left()

    def check_rotate(self) -> None:
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
            self.current_tetromino.rotate_right()
        if keys_pressed[pygame.K_z]:
            self.current_tetromino.rotate_left()

    def random_tetromino(self) -> Tetromino:
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
        for row in self.grid:
            print(row)

    def reset_properties(self) -> None:
        for row in range(self.settings.GRID_N_OF_ROWS):
            for col in range(self.settings.GRID_N_OF_COL):
                self.grid[row][col] = self.settings.EMPTY_CELL_TAG
        for row in range(self.settings.NEXT_TETROMINO_N_OF_ROWS):
            for col in range(self.settings.NEXT_TETROMINO_N_OF_COL):
                self.next_tetromino_grid[row][col] = self.settings.EMPTY_CELL_TAG
        self.score = 0

    def main(self) -> None:
        clock = pygame.time.Clock()
        self.current_tetromino = self.random_tetromino()
        self.current_tetromino.update_on_grid()
        self.next_tetromino = self.random_tetromino()
        self.next_tetromino.put_on_next_tetromino_window()
        self.draw_next_tetromino()
        self.draw_score()
        self.draw_score_title()
        self.draw_next_tetromino_title()
        pygame.time.set_timer(pygame.USEREVENT, self.settings.MOVE_DOWN_TIME)
        pygame.time.set_timer(
            pygame.USEREVENT + 1, self.settings.CHECK_KEYS_PRESSED_MOVEMENT_TIME
        )
        pygame.time.set_timer(
            pygame.USEREVENT + 2, self.settings.CHECK_KEYS_PRESSED_ROTATION_TIME
        )
        self.down = False
        while True:
            clock.tick(self.settings.FPS)
            self.check_events()
            self.draw_grid()
            self.draw_game_window()
            if (
                self.current_tetromino.check_down()
                or self.current_tetromino.check_touch()
            ):
                self.current_tetromino.update_on_grid()
                if self.check_line():
                    self.draw_score()
                # game lost
                if self.check_tetromino_above_top():
                    print("game lost")
                    self.draw_grid()
                    self.draw_game_window()
                    self.draw_next_tetromino_window()
                    self.draw_score_window()
                    pygame.display.update()
                    self.reset_properties()
                    break
                self.current_tetromino = self.next_tetromino
                self.current_tetromino.update_on_grid()
                self.next_tetromino = self.random_tetromino()
                self.next_tetromino.put_on_next_tetromino_window()
                self.draw_next_tetromino()
            else:
                self.current_tetromino.update_on_grid()
            pygame.display.update()
