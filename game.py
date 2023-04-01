import pygame, sys, time, random
from settings import Settings
from tetrominos import Tetromino, Itetromino, Ttetromino

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
            i[0] +=1

    def draw_grid(self):
        self.win.fill((0,0,0))
        for row, list in enumerate(self.grid[2:], 0):
            for col, value in enumerate(list):
                if value == 0:
                    pygame.draw.rect(self.win, self.settings.cell_border_color, (col*self.settings.cell_width, row*self.settings.cell_height, self.settings.cell_width, self.settings.cell_height), 1)
                else:
                    pygame.draw.rect(self.win, self.current.color, (col*self.settings.cell_width, row*self.settings.cell_height, self.settings.cell_width, self.settings.cell_height))
                # elif value == 'I':
                #     pygame.draw.rect(self.win, self.settings.I_color, (col*self.settings.cell_width, row*self.settings.cell_height, self.settings.cell_width, self.settings.cell_height))
                # elif value == 'T':
                #     pygame.draw.rect(self.win, self.settings.T_color, (col*self.settings.cell_width, row*self.settings.cell_height, self.settings.cell_width, self.settings.cell_height))
    
    def draw_border(self):
        pygame.draw.rect(self.win, self.settings.border_color, self.win_rect, 5)
    
    def check_events(self):  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            #         # self.current.move_right()
            #         self.move_right = True
            #     if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            #         self.current.move_left()
            #     if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            #         self.current.move_down() 
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            #         # self.current.move_right()
            #         self.move_right = False
            #     if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            #         self.current.move_left()
            #     if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            #         self.current.move_down()    
            if event.type == pygame.USEREVENT + 1:
                self.check_pressed()
            if event.type == pygame.USEREVENT + 2:
                self.check_rotate()                    
            if event.type == pygame.USEREVENT and not self.down:
                self.move_current()

    def check_pressed(self):
        keys_pressed = pygame.key.get_pressed()
        if (keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]):
            self.current.move_down()
            self.down = True
        else:
            self.down = False 
        if (keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]):
            self.current.move_right()
        if (keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]):
            self.current.move_left()

    def check_rotate(self):
        keys_pressed = pygame.key.get_pressed()
        if (keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]):
            self.current.rotate_right()
        if (keys_pressed[pygame.K_z]):
            self.current.rotate_left()

    def main(self):
        clock = pygame.time.Clock()
        self.current = Itetromino(self)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        pygame.time.set_timer(pygame.USEREVENT+1, 200)
        pygame.time.set_timer(pygame.USEREVENT+2, 150)
        pygame.time.set_timer(pygame.USEREVENT+3, 500)
        while True:
            clock.tick(self.settings.fps)
            self.check_events()            
            self.screen.fill(self.settings.bg)
            self.settings.draw_tetris_title()
            self.screen.blit(self.win, (self.settings.screen_width/2 - self.settings.game_w_width/2,self.settings.screen_height-self.settings.game_w_height))
            self.draw_grid()
            self.draw_border()      
            if self.current.check_down() or self.current.check_touch():
                self.current.put_on_grid()
                self.current = Itetromino(self)
            self.current.put_on_grid()
            pygame.display.update()
            
