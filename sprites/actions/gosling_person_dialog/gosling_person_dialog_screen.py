import pygame.font
import os
from custom_events import *
from funcs.load_image import load_image


class GoslingPersonDialogScreen:
    def __init__(self, screen):
        self.screen = screen

        self.background = load_image('Cyberpunk Backgrounds/Bridge.png')
        self.background_rect = self.background.get_rect(topleft=(0, 0))
        self.font = pygame.font.Font(os.path.join('data', 'futuremillennium/FutureMillennium.ttf'), 36)

        # рендер текста
        self.dialog_text = 'Up and down'
        self.dialog_text_surf = self.font.render(
            self.dialog_text, False, (0, 0, 0), (255, 255, 255)
        )
        self.dialog_text_rect = self.dialog_text_surf.get_rect(topleft=(50, 700))

        # картинка гослинга
        self.px_art_gosling = pygame.transform.rotozoom(
            load_image('gosling_pixel_art.png'), 0, 0.5
        )
        self.px_art_gosling_rect = self.px_art_gosling.get_rect(topleft=(1024 - 500, 250))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(CLOSE_TERMINAL))

        # draw background
        self.screen.blit(self.background, self.background_rect)

        # draw gosling px art
        self.screen.blit(self.px_art_gosling, self.px_art_gosling_rect)

        # draw the text
        self.screen.blit(self.dialog_text_surf, self.dialog_text_rect)
