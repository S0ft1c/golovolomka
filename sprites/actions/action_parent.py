from custom_events import OPEN_TERMINAL
import pygame


class ActionParent:
    def __init__(self, screen):  # обязательно надо получать screen.
        super().__init__()
        self.screen = screen

    def activate(self):
        """
        Активируем событие, оно означает открытие терминала (OPEN_TERMINAL из папки events) и создаем объект класса
        Screen, который и будет игрой в терминале. Обязательно в наследнике дописывать вызов объекта!
        :return: None
        """
        pygame.event.post(pygame.event.Event(OPEN_TERMINAL))

    def get_the_action_screen(self):
        """
        Тут возвращаем просто объект, что за screen.
        :return: Объект, унаследованный от ScreenParent
        """
        print('Не определен метод get_the_action_screen')
