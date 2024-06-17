import pygame
from sprites.actions import TerminalCompletedAction, QuestionGameAction
from sprites.room.terminal1_room.terminal1_room import Terminal1Room
from utils import place_terminal
from funcs.load_image import load_image


class Terminal1RoomQuestion(Terminal1Room):
    def __init__(self, screen, player, exits, compl=False):
        super().__init__(screen, player, exits)

        if not compl:
            self.q1_terminal = place_terminal(430, 500, QuestionGameAction(self.screen))
        else:
            self.q1_terminal = place_terminal(430, 500, TerminalCompletedAction(self.screen))

        self.hole = pygame.transform.rotozoom(
                load_image('q1/questionmark.png'),
                0,
                1.2,
            )

    def update(self):
        super().update()
        self.q1_terminal.update(self.screen, self.player)
        self.screen.blit(self.hole, (400, 100))

    def get_objs(self):
        objs = super().get_objs()
        objs.append(self.q1_terminal)
        return objs

    def get_terminal_action(self):
        for terminal in [self.q1_terminal]:
            if terminal.get_using():  # если терминал используется
                return terminal.action
