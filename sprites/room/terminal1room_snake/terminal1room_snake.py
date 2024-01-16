import pygame
from sprites.actions import SnakeGameAction, TerminalCompletedAction
from ..terminal1_room.terminal1_room import Terminal1Room
from utils import create_main_walls_with_exits, place_terminal
import os
from funcs.load_image import load_image
from sprites.terminal.border import Border


class Terminal1RoomSnake(Terminal1Room):
    def __init__(self, screen, player, exits, compl=False):
        super().__init__(screen, player, exits)

        if not compl:
            self.ping_pong_terminal = place_terminal(410, 500, SnakeGameAction(self.screen))
        else:
            self.ping_pong_terminal = place_terminal(410, 500, TerminalCompletedAction(self.screen))

        self.hole = pygame.transform.rotozoom(
                load_image('snake/snakes.png'),
                0,
                0.20,
            )

        self.hole_border = Border(self.hole, 500, 150)  # даём дыре колизию

    def update(self):
        super().update()
        self.ping_pong_terminal.update(self.screen, self.player)
        self.hole_border.update(self.screen, self.player)

    def get_objs(self):
        objs = super().get_objs()
        objs.append(self.ping_pong_terminal)
        objs.append(self.hole_border)
        return objs

    def get_terminal_action(self):
        for terminal in [self.ping_pong_terminal]:
            if terminal.get_using():  # если терминал используется
                return terminal.action
