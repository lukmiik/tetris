import sys
from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from settings import Settings


class Rules:
    '''A class to show the rules of the game'''

    TEXT: str = "The goal of the game is to get the highest score\n\
possible. You earn points by moving down tetrominos,\n\
1 point for soft drop and two points for hard drop.\n\
You can also earn points by clearing lines.\n\
1 line is 100 points, 2 lines is 300 points,\n\
3 lines is 500 points, and 4 lines is 800 points.\n\
Each 10 lines cleared, the level increases.\n\
The level increases the speed of the tetrominos.\n\
The game ends when the tetrominos reach\n\
the top of the screen."

    def __init__(self, settings: 'Settings') -> None:
        '''Initializes the rules object'''
        self.settings = settings
        self.screen = self.settings.screen
        self.create_title()
        self.create_text()

    def create_title(self) -> None:
        '''Creates the title of the controls'''
        self.title_rendered = self.settings.font_rules_title.render(
            self.settings.RULES_TITLE, True, self.settings.FONT_COLOR
        )
        self.title_rendered_width = self.title_rendered.get_width()
        self.title_coordinates = (
            self.settings.SCREEN_WIDTH / 2 - self.title_rendered_width / 2,
            self.settings.RULES_TITLE_Y,
        )

    def draw_title(self) -> None:
        '''Draws the controls title'''
        self.screen.blit(
            self.title_rendered,
            (self.title_coordinates),
        )

    def create_text(self) -> None:
        '''Creates the text of the rules'''
        self.text_rendered = self.settings.font_rules.render(
            self.TEXT, True, self.settings.FONT_COLOR
        )
        self.text_rendered_width = self.text_rendered.get_width()
        self.text_coordinates = (
            self.settings.SCREEN_WIDTH / 2 - self.text_rendered_width / 2,
            self.settings.RULES_TEXT_Y,
        )

    def draw_text(self) -> None:
        ''''''
        self.screen.blit(self.text_rendered, self.text_coordinates)

    def check_events(self) -> bool | None:
        '''
        Checks for events

        Returns:
            (bool | None): True if go back button is pressed, None otherwise
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and self.settings.go_back_btn_rect.collidepoint(event.pos)
            ):
                return True

    def main(self) -> None:
        '''Main method for the controls screen'''
        self.screen.fill(self.settings.BG_COLOR)
        self.settings.draw_tetris_title()
        self.draw_title()
        self.draw_text()
        self.settings.draw_go_back_btn()
        while True:
            if self.check_events():
                return
            self.settings.check_go_back_btn_hover()
            pygame.display.update()
