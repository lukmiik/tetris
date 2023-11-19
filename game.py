import pygame
import sys
import time
import random

from settings import Settings
from tetrominos import Tetromino, Itetromino, Ttetromino, Otetromino, Stetromino, Ztetromino, Jtetromino, Ltetromino


class Game:
    def __init__(self, settings):
        self.settings = settings
        self.screen = self.settings.screen
        self.game_window = pygame.Surface((self.settings.GAME_WINDOW_WIDTH, self.settings.GAME_WINDOW_HEIGHT))
        self.game_window_rect = self.game_window.get_rect()
        self.next_tetromino_window = pygame.Surface(
            (self.settings.SCORE_NEXT_WINDOW_WIDTH, self.settings.SCORE_NEXT_WINDOW_HEIGHT)
        )
        self.next_tetromino_window_rect = self.next_tetromino_window.get_rect()
        self.grid = [
            [self.settings.EMPTY_CELL_TAG for col in range(self.settings.GRID_N_OF_COL)]
            for row in range(self.settings.GRID_N_OF_ROWS)
        ]
        self.next_tetromino_grid = [
            [self.settings.EMPTY_CELL_TAG for col in range(self.settings.NEXT_TETROMINO_N_OF_COL)]
            for row in range(self.settings.NEXT_TETROMINO_N_OF_ROWS)
        ]

    def draw_grid(self):
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

    def draw_next_tetromino(self):
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

    def draw_game_window(self):
        pygame.draw.rect(self.game_window, self.settings.BORDER_COLOR, self.game_window_rect, 5)
        self.screen.blit(
            self.game_window,
            (
                self.settings.SCREEN_WIDTH / 2 - self.settings.GAME_WINDOW_WIDTH / 2,
                self.settings.SCREEN_HEIGHT - self.settings.GAME_WINDOW_HEIGHT,
            ),
        )

    def draw_next_tetromino_window(self):
        pygame.draw.rect(self.next_tetromino_window, self.settings.BORDER_COLOR, self.next_tetromino_window_rect, 2)
        self.screen.blit(
            self.next_tetromino_window,
            (
                self.settings.NEXT_WINDOW_X,
                self.settings.NEXT_WINDOW_Y,
            ),
        )

    def check_line(self):
        for row, list in enumerate(self.grid[2:], 2):
            line = True
            for col, value in enumerate(list):
                if value == 0:
                    line = False
                    break
            if line:
                self.delete_line(row)

    def delete_line(self, row):
        for r in range(row, 1, -1):
            self.grid[r] = self.grid[r - 1].copy()

    def check_tetromino_above_top(self):
        for x in range(self.settings.GRID_N_OF_COL):
            if self.grid[1][x] != 0:
                return True

    def check_events(self):
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

    def check_pressed(self):
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

    def check_rotate(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
            self.current_tetromino.rotate_right()
        if keys_pressed[pygame.K_z]:
            self.current_tetromino.rotate_left()

    def random_tetromino(self):
        tetrominos = [Itetromino, Ttetromino, Otetromino, Stetromino, Ztetromino, Jtetromino, Ltetromino]
        random_tetromino = random.choice(tetrominos)
        return random_tetromino(self)

    def print_grid(self):
        for row in self.grid:
            print(row)

    def reset_grids(self) -> None:
        for row in range(self.settings.GRID_N_OF_ROWS):
            for col in range(self.settings.GRID_N_OF_COL):
                self.grid[row][col] = self.settings.EMPTY_CELL_TAG
        for row in range(self.settings.NEXT_TETROMINO_N_OF_ROWS):
            for col in range(self.settings.NEXT_TETROMINO_N_OF_COL):
                self.next_tetromino_grid[row][col] = self.settings.EMPTY_CELL_TAG

    def main(self):
        clock = pygame.time.Clock()
        self.current_tetromino = self.random_tetromino()
        self.current_tetromino.update_on_grid()
        self.next_tetromino = self.random_tetromino()
        self.next_tetromino.put_on_next_tetromino_window()
        self.draw_next_tetromino()
        pygame.time.set_timer(pygame.USEREVENT, self.settings.MOVE_DOWN_TIME)
        pygame.time.set_timer(pygame.USEREVENT + 1, self.settings.CHECK_KEYS_PRESSED_MOVEMENT_TIME)
        pygame.time.set_timer(pygame.USEREVENT + 2, self.settings.CHECK_KEYS_PRESSED_ROTATION_TIME)
        self.down = False
        while True:
            clock.tick(self.settings.FPS)
            self.check_events()
            self.draw_grid()
            self.draw_game_window()
            self.draw_next_tetromino_window()
            if self.current_tetromino.check_down() or self.current_tetromino.check_touch():
                self.current_tetromino.update_on_grid()
                self.check_line()
                # game lost
                if self.check_tetromino_above_top():
                    print("game lost")
                    self.draw_grid()
                    self.draw_game_window()
                    self.draw_next_tetromino_window()
                    pygame.display.update()
                    self.reset_grids()
                    break
                self.current_tetromino = self.next_tetromino
                self.current_tetromino.update_on_grid()
                self.next_tetromino = self.random_tetromino()
                self.next_tetromino.put_on_next_tetromino_window()
                self.draw_next_tetromino()
            else:
                self.current_tetromino.update_on_grid()
            pygame.display.update()
