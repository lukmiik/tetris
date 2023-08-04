import pygame, sys, time, random
from settings import Settings
from tetrominos import Tetromino, Itetromino, Ttetromino, Otetromino, Stetromino, Ztetromino, Jtetromino, Ltetromino


class Game:
    def __init__(self):
        self.settings = Settings()
        self.screen = self.settings.screen
        self.win = pygame.Surface((self.settings.game_w_width, self.settings.game_w_height))
        self.win_rect = self.win.get_rect()
        self.grid = [[0 for i in range(self.settings.n_of_col)] for j in range(self.settings.n_of_rows)]

    def move_current(self):
        self.current.clear()
        for i in self.current.pos:
            i[0] += 1

    def draw_grid(self):
        self.win.fill((0, 0, 0))
        for row, list in enumerate(self.grid[2:], 0):
            for col, value in enumerate(list):
                if value == 0:
                    pygame.draw.rect(
                        self.win,
                        self.settings.cell_border_color,
                        (
                            col * self.settings.cell_width,
                            row * self.settings.cell_height,
                            self.settings.cell_width,
                            self.settings.cell_height,
                        ),
                        1,
                    )
                else:
                    x = getattr(self.settings, str(value))
                    pygame.draw.rect(
                        self.win,
                        x,
                        (
                            col * self.settings.cell_width,
                            row * self.settings.cell_height,
                            self.settings.cell_width,
                            self.settings.cell_height,
                        ),
                    )
                # elif value == 'I':
                #     pygame.draw.rect(self.win, self.settings.I_color, (col*self.settings.cell_width, row*self.settings.cell_height, self.settings.cell_width, self.settings.cell_height))
                # elif value == 'T':
                #     pygame.draw.rect(self.win, self.settings.T_color, (col*self.settings.cell_width, row*self.settings.cell_height, self.settings.cell_width, self.settings.cell_height))

    def draw_border(self):
        pygame.draw.rect(self.win, self.settings.border_color, self.win_rect, 5)

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

    def check_end(self):
        for x in range(self.settings.n_of_col):
            if self.grid[1][x] != 0:
                return True

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT + 1:
                self.check_pressed()
            if event.type == pygame.USEREVENT + 2:
                self.check_rotate()
            if event.type == pygame.USEREVENT and not self.down:
                self.move_current()

    def check_pressed(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
            self.current.move_down()
            self.down = True
        else:
            self.down = False
        if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            self.current.move_right()
        if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
            self.current.move_left()

    def check_rotate(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
            self.current.rotate_right()
        if keys_pressed[pygame.K_z]:
            self.current.rotate_left()

    def random_tetromino(self):
        tetrominos = [Itetromino, Ttetromino, Otetromino, Stetromino, Ztetromino, Jtetromino, Ltetromino]
        random_tetromino = random.choice(tetrominos)
        self.current = random_tetromino(self)

    def main(self):
        # for i in self.grid:
        #     print(i)
        clock = pygame.time.Clock()
        self.random_tetromino()
        # move current down every second
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        pygame.time.set_timer(pygame.USEREVENT + 1, 50)
        pygame.time.set_timer(pygame.USEREVENT + 2, 150)
        self.down = False
        while True:
            clock.tick(self.settings.fps)
            self.check_events()
            # if flag:
            #     time.sleep(5)
            #     break
            self.screen.fill(self.settings.bg)
            self.settings.draw_tetris_title()
            self.draw_grid()
            self.draw_border()
            self.screen.blit(
                self.win,
                (
                    self.settings.screen_width / 2 - self.settings.game_w_width / 2,
                    self.settings.screen_height - self.settings.game_w_height,
                ),
            )

            if self.current.check_down() or self.current.check_touch():
                self.current.put_on_grid()
                self.check_line()
                # game lost
                if self.check_end():
                    print("end")
                    self.screen.fill(self.settings.bg)
                    self.settings.draw_tetris_title()
                    self.draw_grid()
                    self.draw_border()
                    self.screen.blit(
                        self.win,
                        (
                            self.settings.screen_width / 2 - self.settings.game_w_width / 2,
                            self.settings.screen_height - self.settings.game_w_height,
                        ),
                    )
                    pygame.display.update()
                    time.sleep(3)
                    break
                self.random_tetromino()
            self.current.put_on_grid()
            pygame.display.update()
