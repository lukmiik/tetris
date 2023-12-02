import sys
from typing import TYPE_CHECKING

import pygame

from db.models.user import User

if TYPE_CHECKING:
    from settings import Settings


class Leaderboard:
    '''Class for the leaderboard screen'''

    def __init__(self, settings: 'Settings') -> None:
        '''Initializes the leaderboard object'''
        self.settings = settings
        self.screen = self.settings.screen
        self.create_title()
        self.create_header()

    def create_title(self) -> None:
        '''Creates the title of the leaderboard'''
        self.title_rendered = self.settings.font_leaderboard_title.render(
            self.settings.LEADERBOARD_TITLE, True, self.settings.FONT_COLOR
        )
        self.title_rendered_width = self.title_rendered.get_width()
        self.title_coordinates = (
            self.settings.SCREEN_WIDTH / 2 - self.title_rendered_width / 2,
            self.settings.LEADERBOARD_TITLE_Y,
        )

    def draw_title(self) -> None:
        '''Draws the leaderboard title'''
        self.screen.blit(
            self.title_rendered,
            (self.title_coordinates),
        )

    def create_header(self) -> None:
        '''Creates the header of the leaderboard'''
        self.header_rect = pygame.Rect(
            self.settings.LEADERBOARD_BORDER_X,
            self.settings.LEADERBOARD_HEADER_Y,
            self.settings.LEADERBOARD_WIDTH,
            self.settings.LEADERBOARD_HEADER_HEIGHT,
        )
        self.header_rank_text = self.settings.font_leaderboard_header.render(
            self.settings.LEADERBOARD_HEADERS_TEXTS[0], True, self.settings.FONT_COLOR
        )
        self.header_username_text = self.settings.font_leaderboard_header.render(
            self.settings.LEADERBOARD_HEADERS_TEXTS[1], True, self.settings.FONT_COLOR
        )
        self.header_score_text = self.settings.font_leaderboard_header.render(
            self.settings.LEADERBOARD_HEADERS_TEXTS[2], True, self.settings.FONT_COLOR
        )
        self.header_lvl_text = self.settings.font_leaderboard_header.render(
            self.settings.LEADERBOARD_HEADERS_TEXTS[3], True, self.settings.FONT_COLOR
        )
        self.header_games_played_text = self.settings.font_leaderboard_header.render(
            self.settings.LEADERBOARD_HEADERS_TEXTS[4], True, self.settings.FONT_COLOR
        )

    def draw_header(self) -> None:
        '''Draws the leaderboard header'''
        pygame.draw.rect(
            self.screen,
            self.settings.LEADERBOARD_BORDER_COLOR,
            self.header_rect,
            self.settings.LEADERBOARD_HEADER_BORDER_WIDTH,
        )
        self.screen.blit(
            self.header_rank_text,
            (
                self.settings.LEADERBOARD_TEXT_X[0]
                - self.header_rank_text.get_width() / 2,
                self.settings.LEADERBOARD_HEADER_TEXT_Y
                - self.header_rank_text.get_height() / 2,
            ),
        )
        self.screen.blit(
            self.header_username_text,
            (
                self.settings.LEADERBOARD_TEXT_X[1]
                - self.header_username_text.get_width() / 2,
                self.settings.LEADERBOARD_HEADER_TEXT_Y
                - self.header_username_text.get_height() / 2,
            ),
        )
        self.screen.blit(
            self.header_score_text,
            (
                self.settings.LEADERBOARD_TEXT_X[2]
                - self.header_score_text.get_width() / 2,
                self.settings.LEADERBOARD_HEADER_TEXT_Y
                - self.header_score_text.get_height() / 2,
            ),
        )
        self.screen.blit(
            self.header_lvl_text,
            (
                self.settings.LEADERBOARD_TEXT_X[3]
                - self.header_lvl_text.get_width() / 2,
                self.settings.LEADERBOARD_HEADER_TEXT_Y
                - self.header_lvl_text.get_height() / 2,
            ),
        )
        self.screen.blit(
            self.header_games_played_text,
            (
                self.settings.LEADERBOARD_TEXT_X[4]
                - self.header_games_played_text.get_width() / 2,
                self.settings.LEADERBOARD_HEADER_TEXT_Y
                - self.header_games_played_text.get_height() / 2,
            ),
        )

    def create_leaderboard(self) -> None:
        '''Creates the leaderboard'''

        for idx, user in enumerate(self.users):
            self.create_draw_row(idx + 1, user)

    def create_draw_row(self, rank: int, user: User) -> None:
        '''Creates and draws a row of the leaderboard'''
        row_y = (
            self.settings.LEADERBOARD_FIRST_ROW_Y
            + (rank - 1) * self.settings.LEADERBOARD_ROW_HEIGHT
        )
        row_rect = pygame.Rect(
            self.settings.LEADERBOARD_BORDER_X,
            row_y,
            self.settings.LEADERBOARD_WIDTH,
            self.settings.LEADERBOARD_ROW_HEIGHT,
        )
        pygame.draw.rect(
            self.screen,
            self.settings.LEADERBOARD_BORDER_COLOR,
            row_rect,
            self.settings.LEADERBOARD_BORDER_WIDTH,
        )
        rank_text = self.settings.font_leaderboard.render(
            str(rank), True, self.settings.FONT_COLOR
        )
        username_text = self.settings.font_leaderboard.render(
            str(user.username), True, self.settings.FONT_COLOR
        )
        highest_score_text = self.settings.font_leaderboard.render(
            str(user.highest_score), True, self.settings.FONT_COLOR
        )
        lvl_text = self.settings.font_leaderboard.render(
            str(user.lvl), True, self.settings.FONT_COLOR
        )
        games_played_text = self.settings.font_leaderboard.render(
            str(user.games_played), True, self.settings.FONT_COLOR
        )
        self.screen.blit(
            rank_text,
            (
                self.settings.LEADERBOARD_TEXT_X[0] - rank_text.get_width() / 2,
                row_y
                + self.settings.LEADERBOARD_ROW_HEIGHT / 2
                - rank_text.get_height() / 2.5,
            ),
        )
        self.screen.blit(
            username_text,
            (
                self.settings.LEADERBOARD_TEXT_X[1] - username_text.get_width() / 2,
                row_y
                + self.settings.LEADERBOARD_ROW_HEIGHT / 2
                - username_text.get_height() / 2.5,
            ),
        )
        self.screen.blit(
            highest_score_text,
            (
                self.settings.LEADERBOARD_TEXT_X[2]
                - highest_score_text.get_width() / 2,
                row_y
                + self.settings.LEADERBOARD_ROW_HEIGHT / 2
                - highest_score_text.get_height() / 2.5,
            ),
        )
        self.screen.blit(
            lvl_text,
            (
                self.settings.LEADERBOARD_TEXT_X[3] - lvl_text.get_width() / 2,
                row_y
                + self.settings.LEADERBOARD_ROW_HEIGHT / 2
                - lvl_text.get_height() / 2.5,
            ),
        )
        self.screen.blit(
            games_played_text,
            (
                self.settings.LEADERBOARD_TEXT_X[4] - games_played_text.get_width() / 2,
                row_y
                + self.settings.LEADERBOARD_ROW_HEIGHT / 2
                - games_played_text.get_height() / 2.5,
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
        '''Main function of the leaderboard screen that draws everything and checks for events'''
        self.users = User.select().order_by(User.highest_score.desc()).limit(10)
        self.screen.fill(self.settings.BG_COLOR)
        self.settings.draw_tetris_title()
        self.draw_title()
        self.draw_header()
        self.create_leaderboard()
        self.settings.draw_go_back_btn()
        pygame.display.update()
        while True:
            if self.check_events():
                return
            self.settings.check_go_back_btn_hover()
