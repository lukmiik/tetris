import sys
from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from settings import Settings


class Menu:
    '''Menu class for the game'''

    GAME_CHOICE: str = 'game'
    LEADERBOARD_CHOICE: str = 'leaderboard'
    CONTROLS_CHOICE: str = 'controls'
    RULES_CHOICE: str = 'rules'
    QUIT_CHOICE: str = 'quit'
    choice: str = ''

    def __init__(self, settings: 'Settings') -> None:
        '''
        Initializes the menu object and creates the buttons

        Args:
            settings (Settings): Settings object
        '''
        self.settings = settings
        self.screen = self.settings.screen
        self.create_buttons()

    def create_buttons(self) -> None:
        '''Creates menu buttons and its rects'''
        self.start_text = self.settings.font_tetris_title.render(
            "Start game", True, self.settings.FONT_COLOR
        )
        self.leaderboard_text = self.settings.font_tetris_title.render(
            "Leaderboard", True, self.settings.FONT_COLOR
        )
        self.controls_text = self.settings.font_tetris_title.render(
            "Controls", True, self.settings.FONT_COLOR
        )
        self.rules_text = self.settings.font_tetris_title.render(
            "Rules", True, self.settings.FONT_COLOR
        )
        self.quit_text = self.settings.font_tetris_title.render(
            "Quit", True, self.settings.FONT_COLOR
        )
        btn_height = 100
        gap = 20
        btn_start_y = 200
        self.start_btn = pygame.Rect(
            self.settings.SCREEN_WIDTH / 2 - self.start_text.get_width() / 2 - 10,
            btn_start_y,
            self.start_text.get_width() + 20,
            btn_height,
        )
        self.leaderboard_btn = pygame.Rect(
            self.settings.SCREEN_WIDTH / 2 - self.leaderboard_text.get_width() / 2 - 10,
            btn_start_y + btn_height + gap,
            self.leaderboard_text.get_width() + 20,
            btn_height,
        )
        self.controls_btn = pygame.Rect(
            self.settings.SCREEN_WIDTH / 2 - self.controls_text.get_width() / 2 - 10,
            btn_start_y + 2 * btn_height + 2 * gap,
            self.controls_text.get_width() + 20,
            btn_height,
        )
        self.rules_btn = pygame.Rect(
            self.settings.SCREEN_WIDTH / 2 - self.rules_text.get_width() / 2 - 1,
            btn_start_y + 3 * btn_height + 3 * gap,
            self.rules_text.get_width() + 20,
            btn_height,
        )
        self.quit_btn = pygame.Rect(
            self.settings.SCREEN_WIDTH / 2 - self.quit_text.get_width() / 2 - 10,
            btn_start_y + 4 * btn_height + 4 * gap,
            self.quit_text.get_width() + 20,
            btn_height,
        )

    def draw_buttons(self) -> None:
        '''Draws the buttons on the screen'''
        pygame.draw.rect(self.screen, self.settings.BG_COLOR, self.start_btn)
        self.screen.blit(
            self.start_text,
            (
                self.start_btn.centerx - self.start_text.get_width() / 2,
                self.start_btn.centery - self.start_text.get_height() / 2,
            ),
        )
        pygame.draw.rect(self.screen, self.settings.BG_COLOR, self.leaderboard_btn)
        self.screen.blit(
            self.leaderboard_text,
            (
                self.leaderboard_btn.centerx - self.leaderboard_text.get_width() / 2,
                self.leaderboard_btn.centery - self.leaderboard_text.get_height() / 2,
            ),
        )
        pygame.draw.rect(self.screen, self.settings.BG_COLOR, self.controls_btn)
        self.screen.blit(
            self.controls_text,
            (
                self.controls_btn.centerx - self.controls_text.get_width() / 2,
                self.controls_btn.centery - self.controls_text.get_height() / 2,
            ),
        )
        pygame.draw.rect(self.screen, self.settings.BG_COLOR, self.rules_btn)
        self.screen.blit(
            self.rules_text,
            (
                self.rules_btn.centerx - self.rules_text.get_width() / 2,
                self.rules_btn.centery - self.rules_text.get_height() / 2,
            ),
        )
        pygame.draw.rect(self.screen, self.settings.BG_COLOR, self.quit_btn)
        self.screen.blit(
            self.quit_text,
            (
                self.quit_btn.centerx - self.quit_text.get_width() / 2,
                self.quit_btn.centery - self.quit_text.get_height() / 2,
            ),
        )

    def controls(self) -> None:
        '''Displays controls screen'''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if pygame.K_ESCAPE:
                        return
            self.screen.fill('red')
            pygame.display.update()

    def rules(self) -> None:
        '''Displays rules screen'''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if pygame.K_ESCAPE:
                        return
            self.screen.fill('green')
            pygame.display.update()

    def check_events(self) -> bool | None:
        '''
        Checks for pygame events QUIT and MOUSEBUTTONDOWN and reacts to them

        Returns:
            (bool | None): True if game, leaderboard, controls or rules button is pressed, None otherwise
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_btn.collidepoint(event.pos):
                    self.choice = self.GAME_CHOICE
                    return True
                elif self.leaderboard_btn.collidepoint(event.pos):
                    self.choice = self.LEADERBOARD_CHOICE
                    return True
                elif self.controls_btn.collidepoint(event.pos):
                    self.controls()
                    self.choice = self.CONTROLS_CHOICE
                    return True
                elif self.rules_btn.collidepoint(event.pos):
                    self.rules()
                    self.choice = self.RULES_CHOICE
                    return True
                elif self.quit_btn.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

    def check_hover(self) -> None:
        '''Checks if mouse is hovering over the buttons and changes the cursor accordingly'''
        if (
            self.start_btn.collidepoint(pygame.mouse.get_pos())
            or self.leaderboard_btn.collidepoint(pygame.mouse.get_pos())
            or self.controls_btn.collidepoint(pygame.mouse.get_pos())
            or self.rules_btn.collidepoint(pygame.mouse.get_pos())
            or self.quit_btn.collidepoint(pygame.mouse.get_pos())
        ):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def main(self) -> str:
        '''
        Main menu loop, waits for the user to press a button and returns the choice

        Returns:
            (str): Choice of the user
        '''
        self.screen.fill(self.settings.BG_COLOR)
        self.settings.draw_tetris_title()
        while True:
            if self.check_events():
                return self.choice
            self.check_hover()
            self.draw_buttons()
            pygame.display.update()
