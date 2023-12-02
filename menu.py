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
            self.settings.MENU_START_GAME_TEXT, True, self.settings.FONT_COLOR
        )
        self.leaderboard_text = self.settings.font_tetris_title.render(
            self.settings.MENU_LEADERBOARD_TEXT, True, self.settings.FONT_COLOR
        )
        self.controls_text = self.settings.font_tetris_title.render(
            self.settings.MENU_CONTROLS_TEXT, True, self.settings.FONT_COLOR
        )
        self.rules_text = self.settings.font_tetris_title.render(
            self.settings.MENU_RULES_TEXT, True, self.settings.FONT_COLOR
        )
        self.quit_text = self.settings.font_tetris_title.render(
            self.settings.MENU_QUIT_TEXT, True, self.settings.FONT_COLOR
        )
        self.start_btn = pygame.Rect(
            self.settings.SCREEN_WIDTH / 2 - self.start_text.get_width() / 2 - 10,
            self.settings.MENU_BTNS_FIRST_Y,
            self.start_text.get_width() + 20,
            self.settings.MENU_BTNS_HEIGHT,
        )
        self.leaderboard_btn = pygame.Rect(
            self.settings.SCREEN_WIDTH / 2 - self.leaderboard_text.get_width() / 2 - 10,
            self.settings.MENU_BTNS_FIRST_Y
            + self.settings.MENU_BTNS_HEIGHT
            + self.settings.MENU_BTN_GAP,
            self.leaderboard_text.get_width() + 20,
            self.settings.MENU_BTNS_HEIGHT,
        )
        self.controls_btn = pygame.Rect(
            self.settings.SCREEN_WIDTH / 2 - self.controls_text.get_width() / 2 - 10,
            self.settings.MENU_BTNS_FIRST_Y
            + 2 * self.settings.MENU_BTNS_HEIGHT
            + 2 * self.settings.MENU_BTN_GAP,
            self.controls_text.get_width() + 20,
            self.settings.MENU_BTNS_HEIGHT,
        )
        self.rules_btn = pygame.Rect(
            self.settings.SCREEN_WIDTH / 2 - self.rules_text.get_width() / 2 - 1,
            self.settings.MENU_BTNS_FIRST_Y
            + 3 * self.settings.MENU_BTNS_HEIGHT
            + 3 * self.settings.MENU_BTN_GAP,
            self.rules_text.get_width() + 20,
            self.settings.MENU_BTNS_HEIGHT,
        )
        self.quit_btn = pygame.Rect(
            self.settings.SCREEN_WIDTH / 2 - self.quit_text.get_width() / 2 - 10,
            self.settings.MENU_BTNS_FIRST_Y
            + 4 * self.settings.MENU_BTNS_HEIGHT
            + 4 * self.settings.MENU_BTN_GAP,
            self.quit_text.get_width() + 20,
            self.settings.MENU_BTNS_HEIGHT,
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
                    self.choice = self.CONTROLS_CHOICE
                    return True
                elif self.rules_btn.collidepoint(event.pos):
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
