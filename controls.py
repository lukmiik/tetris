import sys
from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from settings import Settings


class Controls:
    '''Class for the controls screen'''

    def __init__(self, settings: 'Settings') -> None:
        '''Initializes the controls object'''
        self.settings = settings
        self.screen = self.settings.screen
        self.moving_down_key_1 = pygame.image.load(
            self.settings.MOVING_DOWN_KEY_1_FILENAME
        )
        self.moving_down_key_2 = pygame.image.load(
            self.settings.MOVING_DOWN_KEY_2_FILENAME
        )
        self.moving_left_key_1 = pygame.image.load(
            self.settings.MOVING_LEFT_KEY_1_FILENAME
        )
        self.moving_left_key_2 = pygame.image.load(
            self.settings.MOVING_LEFT_KEY_2_FILENAME
        )
        self.moving_right_key_1 = pygame.image.load(
            self.settings.MOVING_RIGHT_KEY_1_FILENAME
        )
        self.moving_right_key_2 = pygame.image.load(
            self.settings.MOVING_RIGHT_KEY_2_FILENAME
        )
        self.hard_drop_key = pygame.image.load(self.settings.HARD_DROP_KEY_FILENAME)
        self.rotate_left_key = pygame.image.load(self.settings.ROTATE_LEFT_KEY_FILENAME)
        self.rotate_right_key_1 = pygame.image.load(
            self.settings.ROTATE_RIGHT_KEY_1_FILENAME
        )
        self.rotate_right_key_2 = pygame.image.load(
            self.settings.ROTATE_RIGHT_KEY_2_FILENAME
        )
        self.create_title()
        self.create_controls()

    def create_title(self) -> None:
        '''Creates the title of the controls'''
        self.title_rendered = self.settings.font_controls_title.render(
            self.settings.CONTROLS_TITLE, True, self.settings.FONT_COLOR
        )
        self.title_rendered_width = self.title_rendered.get_width()
        self.title_coordinates = (
            self.settings.SCREEN_WIDTH / 2 - self.title_rendered_width / 2,
            self.settings.CONTROLS_TITLE_Y,
        )

    def draw_title(self) -> None:
        '''Draws the controls title'''
        self.screen.blit(
            self.title_rendered,
            (self.title_coordinates),
        )

    def create_controls(self) -> None:
        '''Creates the controls'''
        self.move_down_text = self.settings.font_controls.render(
            self.settings.CONTROLS_TEXTS[0], True, self.settings.FONT_COLOR
        )
        self.move_down_key_1_rect = pygame.Rect(
            self.settings.CONTROLS_TWO_KEYS_X[0],
            self.settings.CONTROLS_TEXTS_Y[0] - self.move_down_text.get_height(),
            self.moving_down_key_1.get_width(),
            self.moving_down_key_1.get_height(),
        )
        self.move_down_key_2_rect = pygame.Rect(
            self.settings.CONTROLS_TWO_KEYS_X[1],
            self.settings.CONTROLS_TEXTS_Y[0] - self.move_down_text.get_height(),
            self.moving_down_key_1.get_width(),
            self.moving_down_key_1.get_height(),
        )
        self.move_left_text = self.settings.font_controls.render(
            self.settings.CONTROLS_TEXTS[1], True, self.settings.FONT_COLOR
        )
        self.moving_left_key_1_rect = pygame.Rect(
            self.settings.CONTROLS_TWO_KEYS_X[0],
            self.settings.CONTROLS_TEXTS_Y[1] - self.move_left_text.get_height(),
            self.moving_left_key_1.get_width(),
            self.moving_left_key_1.get_height(),
        )
        self.moving_left_key_2_rect = pygame.Rect(
            self.settings.CONTROLS_TWO_KEYS_X[1],
            self.settings.CONTROLS_TEXTS_Y[1] - self.move_left_text.get_height(),
            self.moving_left_key_2.get_width(),
            self.moving_left_key_2.get_height(),
        )
        self.move_right_text = self.settings.font_controls.render(
            self.settings.CONTROLS_TEXTS[2], True, self.settings.FONT_COLOR
        )
        self.moving_right_key_1_rect = pygame.Rect(
            self.settings.CONTROLS_TWO_KEYS_X[0],
            self.settings.CONTROLS_TEXTS_Y[2] - self.move_right_text.get_height(),
            self.moving_right_key_1.get_width(),
            self.moving_right_key_1.get_height(),
        )
        self.moving_right_key_2_rect = pygame.Rect(
            self.settings.CONTROLS_TWO_KEYS_X[1],
            self.settings.CONTROLS_TEXTS_Y[2] - self.move_right_text.get_height(),
            self.moving_right_key_2.get_width(),
            self.moving_right_key_2.get_height(),
        )
        self.hard_drop_text = self.settings.font_controls.render(
            self.settings.CONTROLS_TEXTS[3], True, self.settings.FONT_COLOR
        )
        self.hard_drop_key_rect = pygame.Rect(
            self.settings.CONTROLS_ONE_KEY_X,
            self.settings.CONTROLS_TEXTS_Y[3] - self.hard_drop_text.get_height(),
            self.hard_drop_key.get_width(),
            self.hard_drop_key.get_height(),
        )
        self.rotate_left_text = self.settings.font_controls.render(
            self.settings.CONTROLS_TEXTS[4], True, self.settings.FONT_COLOR
        )
        self.rotate_left_key_rect = pygame.Rect(
            self.settings.CONTROLS_ONE_KEY_X,
            self.settings.CONTROLS_TEXTS_Y[4] - self.rotate_left_text.get_height(),
            self.rotate_left_key.get_width(),
            self.rotate_left_key.get_height(),
        )
        self.rotate_right_text = self.settings.font_controls.render(
            self.settings.CONTROLS_TEXTS[5], True, self.settings.FONT_COLOR
        )
        self.rotate_right_key_1_rect = pygame.Rect(
            self.settings.CONTROLS_TWO_KEYS_X[0],
            self.settings.CONTROLS_TEXTS_Y[5] - self.rotate_right_text.get_height(),
            self.rotate_right_key_1.get_width(),
            self.rotate_right_key_1.get_height(),
        )
        self.rotate_right_key_2_rect = pygame.Rect(
            self.settings.CONTROLS_TWO_KEYS_X[1],
            self.settings.CONTROLS_TEXTS_Y[5] - self.rotate_right_text.get_height(),
            self.rotate_right_key_2.get_width(),
            self.rotate_right_key_2.get_height(),
        )

    def draw_controls(self) -> None:
        '''Draws the controls'''
        self.screen.blit(
            self.move_down_text,
            (
                self.settings.CONTROLS_TEXTS_X - self.move_down_text.get_width() / 2,
                self.settings.CONTROLS_TEXTS_Y[0]
                - self.move_down_text.get_height() / 2,
            ),
        )
        self.screen.blit(
            self.moving_down_key_1,
            self.moving_down_key_1.get_rect(center=self.move_down_key_1_rect.center),
        )
        self.screen.blit(
            self.moving_down_key_2,
            self.moving_down_key_2.get_rect(center=self.move_down_key_2_rect.center),
        )
        self.screen.blit(
            self.move_left_text,
            (
                self.settings.CONTROLS_TEXTS_X - self.move_left_text.get_width() / 2,
                self.settings.CONTROLS_TEXTS_Y[1]
                - self.move_left_text.get_height() / 2,
            ),
        )
        self.screen.blit(
            self.moving_left_key_1,
            self.moving_left_key_1.get_rect(center=self.moving_left_key_1_rect.center),
        )
        self.screen.blit(
            self.moving_left_key_2,
            self.moving_left_key_2.get_rect(center=self.moving_left_key_2_rect.center),
        )
        self.screen.blit(
            self.move_right_text,
            (
                self.settings.CONTROLS_TEXTS_X - self.move_right_text.get_width() / 2,
                self.settings.CONTROLS_TEXTS_Y[2]
                - self.move_right_text.get_height() / 2,
            ),
        )
        self.screen.blit(
            self.moving_right_key_1,
            self.moving_right_key_1.get_rect(
                center=self.moving_right_key_1_rect.center
            ),
        )
        self.screen.blit(
            self.moving_right_key_2,
            self.moving_right_key_2.get_rect(
                center=self.moving_right_key_2_rect.center
            ),
        )
        self.screen.blit(
            self.hard_drop_text,
            (
                self.settings.CONTROLS_TEXTS_X - self.hard_drop_text.get_width() / 2,
                self.settings.CONTROLS_TEXTS_Y[3]
                - self.hard_drop_text.get_height() / 2,
            ),
        )
        self.screen.blit(
            self.hard_drop_key,
            self.hard_drop_key.get_rect(center=self.hard_drop_key_rect.center),
        )
        self.screen.blit(
            self.rotate_left_text,
            (
                self.settings.CONTROLS_TEXTS_X - self.rotate_left_text.get_width() / 2,
                self.settings.CONTROLS_TEXTS_Y[4]
                - self.rotate_left_text.get_height() / 2,
            ),
        )
        self.screen.blit(
            self.rotate_left_key,
            self.rotate_left_key.get_rect(center=self.rotate_left_key_rect.center),
        )
        self.screen.blit(
            self.rotate_right_text,
            (
                self.settings.CONTROLS_TEXTS_X - self.rotate_right_text.get_width() / 2,
                self.settings.CONTROLS_TEXTS_Y[5]
                - self.rotate_right_text.get_height() / 2,
            ),
        )
        self.screen.blit(
            self.rotate_right_key_1,
            self.rotate_right_key_1.get_rect(
                center=self.rotate_right_key_1_rect.center
            ),
        )
        self.screen.blit(
            self.rotate_right_key_2,
            self.rotate_right_key_2.get_rect(
                center=self.rotate_right_key_2_rect.center
            ),
        )

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
        self.draw_controls()
        self.settings.draw_go_back_btn()
        while True:
            if self.check_events():
                return
            self.settings.check_go_back_btn_hover()
            pygame.display.update()
