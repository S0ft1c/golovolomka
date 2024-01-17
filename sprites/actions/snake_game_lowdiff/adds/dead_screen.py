import pygame
from custom_events import *
from funcs.load_image import load_image


class DeadScreen:
    def __init__(self, screen):
        self.screen = screen
        self.bsod_image = pygame.transform.rotozoom(
            load_image("snake/angry_snake.png"),
            0,
            0.75
        )
        self.font = pygame.font.SysFont("Arial", 32)
        self.custom_message = f"Ты проиграл игру в змейку!"
        self.custom_message_2 = "За это ты потеряешь одну жизнь!"
        self.hint_text = "Нажмите ESC чтобы выйти"

        # цвета
        self.white = (255, 255, 255)

    def display_dead_screen(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(TERMINAL_LOST))

        # заполняем экран
        self.screen.fill((0, 250, 0))

        # отображаем картинку
        self.screen.blit(self.bsod_image, (300, 0))

        # отображение текста
        text = self.font.render(self.custom_message, True, self.white)
        text_rect = text.get_rect(center=(1024 // 2, 896 // 2 + 100))
        self.screen.blit(text, text_rect)
        text = self.font.render(self.custom_message_2, True, self.white)
        text_rect = text.get_rect(center=(1024 // 2, 896 // 2 + 150))
        self.screen.blit(text, text_rect)

        # Отображение текста подсказки
        hint = self.font.render(self.hint_text, True, self.white)
        hint_rect = hint.get_rect(center=(1024 // 2, 896 - 50))
        self.screen.blit(hint, hint_rect)

        pygame.display.flip()
