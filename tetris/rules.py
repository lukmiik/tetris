import sys
from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from .settings import Settings


class Rules:
    '''A class to show the rules of the game'''

    TEXT: list[str] = [
        "The goal of the game is to get the highest score",
        "possible. You earn points by moving down tetrominos",
        "1 point for soft drop and two points for hard drop.",
        "You can also earn points by clearing lines.",
        "1 line is 100 points, 2 lines is 300 points,",
        "3 lines is 500 points, and 4 lines is 800 points.",
        "Each 10 lines cleared, the level increases.",
        "The level increases the speed of the tetrominos.",
        "The game ends when the tetrominos reach",
        "the top of the screen.",
    ]

    def __init__(self, settings: 'Settings') -> None:
        '''Initializes the rules object'''
        self.settings = settings
        self.screen = self.settings.screen
        self.create_title()

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

    def create_draw_text(self) -> None:
        '''Creates and draws the text of the rules'''
        for idx, line in enumerate(self.TEXT):
            text_rendered = self.settings.font_rules.render(
                line, True, self.settings.FONT_COLOR
            )
            text_rendered_width = text_rendered.get_width()
            text_coordinates = (
                self.settings.SCREEN_WIDTH / 2 - text_rendered_width / 2,
                self.settings.RULES_TEXT_Y + idx * self.settings.RULES_LINE_HEIGHT,
            )
            self.screen.blit(text_rendered, text_coordinates)

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
        self.create_draw_text()
        self.settings.draw_go_back_btn()
        while True:
            if self.check_events():
                return
            self.settings.check_go_back_btn_hover()
            pygame.display.update()
