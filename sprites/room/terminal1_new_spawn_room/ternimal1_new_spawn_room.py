import pygame
from sprites.actions import NewSpawnGameAction, TerminalCompletedAction
from ..terminal1_room.terminal1_room import Terminal1Room
from utils import place_terminal
from funcs.load_image import load_image
from sprites.terminal.border import Border


class Terminal1RoomNewSpawn(Terminal1Room):
    def __init__(self, screen, player, exits, compl=False):
        super().__init__(screen, player, exits)

        if not compl:
            self.ping_pong_terminal = place_terminal(410, 500, NewSpawnGameAction(self.screen))
        else:
            self.ping_pong_terminal = place_terminal(410, 500, TerminalCompletedAction(self.screen))

        self.background = load_image("room_assets/2 Background/spawn_background.png")

    def update(self):
        super().update()
        self.ping_pong_terminal.update(self.screen, self.player)

    def get_objs(self):
        objs = super().get_objs()
        objs.append(self.ping_pong_terminal)
        return objs

    def get_terminal_action(self):
        for terminal in [self.ping_pong_terminal]:
            if terminal.get_using():  # если терминал используется
                return terminal.action
