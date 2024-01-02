import pygame
import sys
from funcs.load_image import load_image
from custom_events import *
from ..screen_parent import ScreenParent


class TerminalCompleted:
    def __init__(self, screen):
        self.screen = screen

        # Цвета
        self.green = (0, 255, 0)
        self.cyan = (0, 255, 255)

        # Загрузка шрифта
        self.font = pygame.font.Font(None, 36)

        # Текст
        self.text = "Данный терминал пройден"

        # Опции текста
        self.text_position = (self.screen.get_width() // 2, self.screen.get_height() // 2)
        self.text_color = self.green
        self.text_bg_color = None  # None для прозрачного фона

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(CLOSE_TERMINAL))

        # Отображение текста
        self.screen.fill((0, 0, 0))
        text_surface = self.font.render(self.text, True, self.text_color, self.text_bg_color)
        text_rect = text_surface.get_rect(center=self.text_position)
        self.screen.blit(text_surface, text_rect)

        pygame.display.flip()

