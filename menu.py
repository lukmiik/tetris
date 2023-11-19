import pygame
import sys
from settings import Settings


class Menu:
    def __init__(self):
        self.settings = Settings()
        self.screen = self.settings.screen
        self.font = self.settings.font

    def create_buttons(self):
        # text
        self.start_text = self.font.render("Start game", True, self.settings.font_color)
        self.controls_text = self.font.render("Controls", True, self.settings.font_color)
        self.rules_text = self.font.render("Rules", True, self.settings.font_color)
        self.quit_text = self.font.render("Quit", True, self.settings.font_color)
        # btn
        btn_height = 100
        gap = 20
        btn_start_y = 250
        self.start_btn = pygame.Rect(
            self.settings.screen_width / 2 - self.start_text.get_width() / 2 - 10,
            btn_start_y,
            self.start_text.get_width() + 20,
            btn_height,
        )
        self.controls_btn = pygame.Rect(
            self.settings.screen_width / 2 - self.controls_text.get_width() / 2 - 10,
            btn_start_y + btn_height + gap,
            self.controls_text.get_width() + 20,
            btn_height,
        )
        self.rules_btn = pygame.Rect(
            self.settings.screen_width / 2 - self.rules_text.get_width() / 2 - 1,
            btn_start_y + 2 * btn_height + 2 * gap,
            self.rules_text.get_width() + 20,
            btn_height,
        )
        self.quit_btn = pygame.Rect(
            self.settings.screen_width / 2 - self.quit_text.get_width() / 2 - 10,
            btn_start_y + 3 * btn_height + 3 * gap,
            self.quit_text.get_width() + 20,
            btn_height,
        )

    def draw_buttons(self):
        pygame.draw.rect(self.screen, self.settings.bg_color, self.start_btn)
        self.screen.blit(
            self.start_text,
            (
                self.start_btn.centerx - self.start_text.get_width() / 2,
                self.start_btn.centery - self.start_text.get_height() / 2,
            ),
        )
        pygame.draw.rect(self.screen, self.settings.bg_color, self.controls_btn)
        self.screen.blit(
            self.controls_text,
            (
                self.controls_btn.centerx - self.controls_text.get_width() / 2,
                self.controls_btn.centery - self.controls_text.get_height() / 2,
            ),
        )
        pygame.draw.rect(self.screen, self.settings.bg_color, self.rules_btn)
        self.screen.blit(
            self.rules_text,
            (
                self.rules_btn.centerx - self.rules_text.get_width() / 2,
                self.rules_btn.centery - self.rules_text.get_height() / 2,
            ),
        )
        pygame.draw.rect(self.screen, self.settings.bg_color, self.quit_btn)
        self.screen.blit(
            self.quit_text,
            (
                self.quit_btn.centerx - self.quit_text.get_width() / 2,
                self.quit_btn.centery - self.quit_text.get_height() / 2,
            ),
        )

    def controls(self):
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

    def rules(self):
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

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_btn.collidepoint(event.pos):
                    return True
                elif self.controls_btn.collidepoint(event.pos):
                    self.controls()
                elif self.rules_btn.collidepoint(event.pos):
                    self.rules()
                elif self.quit_btn.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

    def check_hover(self):
        if self.start_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif self.controls_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif self.rules_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif self.quit_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def main(self):
        self.create_buttons()
        while True:
            if self.check_events():
                return
            self.check_hover()
            self.screen.fill(self.settings.bg_color)
            self.settings.draw_tetris_title()
            self.draw_buttons()
            pygame.display.update()
