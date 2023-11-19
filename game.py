import pygame, sys, time, random
from settings import Settings
from tetrominos import Tetromino, Itetromino, Ttetromino, Otetromino, Stetromino, Ztetromino, Jtetromino, Ltetromino


class Game:
    def __init__(self):
        self.settings = Settings()
        self.screen = self.settings.screen
        self.screen.fill(self.settings.bg_color)
        self.game_window = pygame.Surface((self.settings.game_window_width, self.settings.game_window_height))
        self.game_window_rect = self.game_window.get_rect()
        self.next_tetromino_window = pygame.Surface(
            (self.settings.score_next_window_width, self.settings.score_next_window_height)
        )
        self.next_tetromino_window_rect = self.next_tetromino_window.get_rect()
        self.grid = [
            [self.settings.empty_cell_tag for col in range(self.settings.grid_n_of_col)]
            for row in range(self.settings.grid_n_of_rows)
        ]
        self.next_tetromino_grid = [
            [self.settings.empty_cell_tag for col in range(self.settings.next_tetromino_n_of_col)]
            for row in range(self.settings.next_tetromino_n_of_rows)
        ]

    def draw_grid(self):
        self.game_window.fill(self.settings.second_bg_color)
        for row, list in enumerate(self.grid[2:], 0):
            for col, value in enumerate(list):
                if value == self.settings.empty_cell_tag:
                    pygame.draw.rect(
                        self.game_window,
                        self.settings.cell_border_color,
                        (
                            col * self.settings.grid_cell_width,
                            row * self.settings.grid_cell_height,
                            self.settings.grid_cell_width,
                            self.settings.grid_cell_height,
                        ),
                        1,
                    )
                else:
                    x = getattr(self.settings, str(value))
                    pygame.draw.rect(
                        self.game_window,
                        x,
                        (
                            col * self.settings.grid_cell_width,
                            row * self.settings.grid_cell_height,
                            self.settings.grid_cell_width,
                            self.settings.grid_cell_height,
                        ),
                    )

    def draw_next_tetromino(self):
        self.next_tetromino_window.fill(self.settings.second_bg_color)
        for row, list in enumerate(self.next_tetromino_grid):
            for col, value in enumerate(list):
                if value == self.settings.empty_cell_tag:
                    pygame.draw.rect(
                        self.next_tetromino_window,
                        self.settings.second_bg_color,
                        (
                            col * self.settings.next_tetromino_cell_width,
                            row * self.settings.next_tetromino_cell_height,
                            self.settings.next_tetromino_cell_width,
                            self.settings.next_tetromino_cell_height,
                        ),
                    )
                else:
                    x = getattr(self.settings, str(value))
                    pygame.draw.rect(
                        self.next_tetromino_window,
                        x,
                        (
                            col * self.settings.next_tetromino_cell_width,
                            row * self.settings.next_tetromino_cell_height,
                            self.settings.next_tetromino_cell_width,
                            self.settings.next_tetromino_cell_height,
                        ),
                    )

    def draw_game_window(self):
        pygame.draw.rect(self.game_window, self.settings.border_color, self.game_window_rect, 5)
        self.screen.blit(
            self.game_window,
            (
                self.settings.screen_width / 2 - self.settings.game_window_width / 2,
                self.settings.screen_height - self.settings.game_window_height,
            ),
        )

    def draw_next_tetromino_window(self):
        pygame.draw.rect(self.next_tetromino_window, self.settings.border_color, self.next_tetromino_window_rect, 2)
        self.screen.blit(
            self.next_tetromino_window,
            (
                self.settings.next_window_x,
                self.settings.next_window_y,
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
        for x in range(self.settings.grid_n_of_col):
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

    def main(self):
        clock = pygame.time.Clock()
        self.current_tetromino = self.random_tetromino()
        self.current_tetromino.update_on_grid()
        self.next_tetromino = self.random_tetromino()
        self.next_tetromino.put_on_next_tetromino_window()
        self.draw_next_tetromino()
        # move current down every second
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        pygame.time.set_timer(pygame.USEREVENT + 1, 50)
        pygame.time.set_timer(pygame.USEREVENT + 2, 150)
        self.down = False
        while True:
            clock.tick(self.settings.fps)
            self.check_events()
            self.settings.draw_tetris_title()
            self.draw_grid()
            self.draw_game_window()
            self.draw_next_tetromino_window()
            # self.print_grid()
            if self.current_tetromino.check_down() or self.current_tetromino.check_touch():
                self.current_tetromino.update_on_grid()
                self.check_line()
                # game lost
                if self.check_tetromino_above_top():
                    print("game lost")
                    self.screen.fill(self.settings.bg_color)
                    self.settings.draw_tetris_title()
                    self.draw_grid()
                    self.draw_game_window()
                    self.draw_next_tetromino_window()
                    pygame.display.update()
                    break
                self.current_tetromino = self.next_tetromino
                self.next_tetromino = self.random_tetromino()
                self.next_tetromino.put_on_next_tetromino_window()
                self.draw_next_tetromino()
            self.current_tetromino.update_on_grid()
            pygame.display.update()
