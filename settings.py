import pygame

class Settings:
    def __init__(self):
        #necessary inits
        pygame.init()
        pygame.display.init()
        pygame.font.init()
        #screen
        self.screen_width = 800
        self.screen_height = 800
        self.bg = (0,0,100)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))     
        #font
        self.font = pygame.font.SysFont('Tahoma',80)
        self.font_color = (255, 255, 255)
        #game window
        self.game_w_width = 400
        self.game_w_heihgt = 600
        #next and score windows
        self.info_w_width = 100
        self.info_w_height = 200
        

    def draw_tetris_title(self):
        text = self.font.render("TETRIS", True, self.font_color)
        self.screen.blit(text, (self.screen_width/2 - text.get_width()/2, 100))

