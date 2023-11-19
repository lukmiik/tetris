import pygame


class Settings:
    def __init__(self):
        # necessary inits
        pygame.init()
        pygame.display.init()
        pygame.font.init()
        # screen
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (0, 0, 100)
        self.second_bg_color = (0, 0, 0)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        # font
        self.font = pygame.font.SysFont('Tahoma', 80)
        self.font_color = (255, 255, 255)
        # game window
        self.fps = 60
        self.game_window_width = 400
        self.game_window_height = 600
        self.border_color = (255, 0, 0)
        self.cell_border_color = (119, 136, 153)
        self.grid_n_of_col = 10
        self.grid_n_of_rows = 22
        self.grid_cell_width = self.game_window_width // self.grid_n_of_col
        self.grid_cell_height = self.game_window_height // (self.grid_n_of_rows - 2)
        self.empty_cell_tag = 0
        # tetrominos
        self.I = (0, 255, 255)  # cyan
        self.O = (255, 255, 0)  # żółty
        self.T = (128, 0, 128)  # fioletowy
        self.S = (0, 255, 0)  # zielony
        self.Z = (255, 0, 0)  # czerwony
        self.J = (0, 0, 255)  # niebieski
        self.L = (255, 165, 0)  # pomarańczowy
        # next and score windows
        self.score_next_window_width = 220
        self.score_next_window_height = 150
        self.next_window_x = 725
        self.next_window_y = 200
        self.next_tetromino_n_of_col = 4
        self.next_tetromino_n_of_rows = 4
        self.next_tetromino_cell_width = self.score_next_window_width // self.next_tetromino_n_of_col
        self.next_tetromino_cell_height = self.score_next_window_height // self.next_tetromino_n_of_rows

    def draw_tetris_title(self):
        text = self.font.render("TETRIS", True, self.font_color)
        self.screen.blit(text, (self.screen_width / 2 - text.get_width() / 2, 50))
