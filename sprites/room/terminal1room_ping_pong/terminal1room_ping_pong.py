import pygame
from sprites.actions import PingPongGameAction, TerminalCompletedAction
from ..terminal1_room.terminal1_room import Terminal1Room
from utils import create_main_walls_with_exits, place_terminal
import os
from funcs.load_image import load_image


class Terminal1RoomPingPong(Terminal1Room):
    def __init__(self, screen, player, exits, compl=False):
        super().__init__(screen, player, exits)

        if not compl:
            self.snake_terminal = place_terminal(410, 500, PingPongGameAction(self.screen))
        else:
            self.snake_terminal = place_terminal(410, 500, TerminalCompletedAction(self.screen))

    def update(self):
        super().update()
        self.snake_terminal.update(self.screen, self.player)

    def get_objs(self):
        objs = super().get_objs()
        objs.append(self.snake_terminal)
        return objs

    def get_terminal_action(self):
        for terminal in [self.snake_terminal]:
            if terminal.get_using():  # если терминал используется
                return terminal.action
