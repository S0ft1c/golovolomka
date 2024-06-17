import pygame
import sys
from funcs.load_image import load_image
from custom_events import *


class CyberpunkTerminal:
    def __init__(self, screen):
        self.screen = screen

        # Загрузка изображений
        self.image1 = pygame.transform.rotozoom(
            load_image("winner.png"),
            0,
            0.5
        )

        # Подсказка
        self.hint_font = pygame.font.Font(None, 24)
        self.hint_text = "Нажмите ESC, чтобы закрыть"

    def display_cyberpunk_screen(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(TERMINAL_COMPLETED))

        hint_timer = 0

        # Отображение поздравительного текста
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render("Поздравляю с прохождением терминала!", True, (0, 255, 0))
        self.screen.blit(text, ((self.screen.get_width() - text.get_width()) // 2, self.screen.get_height() // 4))

        # Отображение картинок
        self.screen.blit(self.image1, (self.screen.get_width() // 4, self.screen.get_height() // 2))

        # Отображение подсказки
        if hint_timer < 60:  # Отображаем подсказку в течение 60 кадров (примерно 1 секунда)
            hint_surface = self.hint_font.render(self.hint_text, True, (255, 255, 255))
            self.screen.blit(hint_surface, (
                (self.screen.get_width() - hint_surface.get_width()) // 2, self.screen.get_height() - 40))
            hint_timer += 1

        pygame.display.flip()


if __name__ == "__main__":
    cyberpunk_terminal = CyberpunkTerminal()
    cyberpunk_terminal.display_cyberpunk_screen()
