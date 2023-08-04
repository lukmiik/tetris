import pygame

class Settings:
    def __init__(self):
        #necessary inits
        pygame.init()
        pygame.display.init()
        pygame.font.init()
        #screen
        self.screen_width = 1000
        self.screen_height = 800
        self.bg = (0,0,100)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))     
        #font
        self.font = pygame.font.SysFont('Tahoma',80)
        self.font_color = (255, 255, 255)
        #game window
        self.fps = 60
        self.game_w_width = 400
        self.game_w_height = 600
        self.border_color = (255, 0,0)
        self.cell_border_color = (119,136,153)
        self.n_of_col = 10
        self.n_of_rows = 22
        self.cell_width = self.game_w_width//self.n_of_col
        self.cell_height = self.game_w_height//(self.n_of_rows-2)
        #tetrominos
        self.I = (0, 255, 255)#cyan
        self.O = (255, 255, 0)#żółty
        self.T = (128, 0, 128)#fioletowy
        self.S = (0, 255, 0)#zielony
        self.Z = (255, 0, 0)#czerowmy
        self.J = (0, 0, 255)#niebieski
        self.L = (255, 165, 0)#pomarańczowy
        #next and score windows
        self.info_w_width = 100
        self.info_w_height = 200
        
    def draw_tetris_title(self):
        text = self.font.render("TETRIS", True, self.font_color)
        self.screen.blit(text, (self.screen_width/2 - text.get_width()/2, 50))

