import pygame
from custom_events import *

class NewSpawnGame:
    def __init__(self, screen):
        pygame.init()

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.font1 = pygame.font.Font(None, 50)
        self.font = pygame.font.Font(None, 150)

    def update(self):
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(TERMINAL_COMPLETED))

        self.draw()

    def draw(self):
        self.screen.fill((0, 0, 0))
        text_surface1 = self.font1.render(f'Привет! Реши все головоломки, чтобы пройти игру!', True, (0, 255, 0))
        self.screen.blit(text_surface1, (30, 40))

        text_surface1 = self.font1.render(f'Но будь внимателен, ведь у тебя всего 3 жизни!!!', True, (0, 255, 0))
        self.screen.blit(text_surface1, (30, 200))

        text_surface1 = self.font1.render(f'Если жизни закончатся, то игра завершиться', True, (0, 255, 0))
        self.screen.blit(text_surface1, (30, 400))

        text_surface1 = self.font1.render(f'Удачи!', True, (0, 255, 0))
        self.screen.blit(text_surface1, (30, 400))

        text_surface1 = self.font1.render(f'Разработчики: Кудинов Павел и Дольский Степан', True, (0, 255, 0))
        self.screen.blit(text_surface1, (30, 600))

        text_surface1 = self.font1.render(f'Нажмите ESC, чтобы выйти', True, (0, 255, 0))
        self.screen.blit(text_surface1, (30, 800))

        pygame.display.flip()

