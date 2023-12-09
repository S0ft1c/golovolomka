from sprites import AnimatedPlayer
import pygame
from custom_events import *


class RoomParent:
    def __init__(self, screen: pygame.Surface, player: AnimatedPlayer):
        self.screen = screen
        self.player = player

    def update(self):
        """
        Отвечает за отображение необходимого, а также и счета нажатий и клавиш.
        :return: None
        """
        # TODO: добавить больше методов обработки комнат
        if self.player.rect.x - self.screen.get_rect().width > 30:
            pygame.event.post(pygame.event.Event(PLAYER_OUT_OF_RIGHT))
            return
        elif self.player.rect.x < 30:
            pygame.event.post(pygame.event.Event(PLAYER_OUT_OF_LEFT))
            return
        elif self.player.rect.y < 30:
            pygame.event.post(pygame.event.Event(PLAYER_OUT_OF_UP))
            return
        elif self.player.rect.y - self.screen.get_rect().height > 30:
            pygame.event.post(pygame.event.Event(PLAYER_OUT_OF_DOWN))
            return

    def get_objs(self):
        """
        Это метод, который необходим для подсчета всех элементов, что могут иметь коллизию.
        :return: list, в котором лежат все такие элементы
        """
        print('Не определен метод get_objs')

    """
    Если это комната с терминалом, то надо еще добавить метод get_terminal_action() который будет выглядеть вот так:
    
    def get_terminal_action(self):
        for terminal in [<тут все объекты, что за терминалы>]:
            if terminal.get_using():  # если терминал используется
                return terminal.action
    
    """
