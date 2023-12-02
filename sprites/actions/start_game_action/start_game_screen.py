import pygame
from ..screen_parent import ScreenParent
from custom_events import CLOSE_TERMINAL, CREATE_NEW_GAME


class StartGameScreen(ScreenParent):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.background_color = pygame.color.Color('#3a87fa')
        self.font = pygame.font.Font(None, 36)  # TODO: добавить шрифт
        self.small_font = pygame.font.Font(None, 20)  # TODO: добавить шрифт

        # текст начала игры
        self.starttext = self.font.render("Нажмите Enter для начала новой игры!", True, (255, 255, 255))
        self.starttext_rect = self.starttext.get_rect(center=(1024 / 2, 896 / 2))

        # текст выхода
        self.exittext = self.small_font.render("или нажмите esc, чтобы вернуться", True, (255, 255, 255))
        self.exittext_rect = self.exittext.get_rect(center=(1024 / 2, 750))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(CLOSE_TERMINAL))  # посылаем событие на закрытие
            return
        if keys[pygame.K_RETURN]:
            pygame.event.post(pygame.event.Event(CREATE_NEW_GAME))  # вызываем событие по началу создания лабиринта
            return

        self.screen.fill(self.background_color)
        self.screen.blit(self.starttext, self.starttext_rect)
        self.screen.blit(self.exittext, self.exittext_rect)
