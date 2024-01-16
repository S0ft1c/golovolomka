import pygame.transform
from funcs.load_image import load_image
from ..terminal1_room.terminal1_room import Terminal1Room
from utils import place_terminal
from sprites.actions import TerminalCompletedAction
from sprites import Person
from sprites.actions import GoslingPersonDialogAction
from sprites.actions import GoslingGameAction


class Terminal1RoomGosling(Terminal1Room):
    def __init__(self, screen, player, exits, compl=False):
        super().__init__(screen, player, exits)

        if not compl:
            self.gosling_terminal = place_terminal(300, 400, GoslingGameAction(screen))
        else:
            self.gosling_terminal = place_terminal(300, 400, TerminalCompletedAction(screen))

        # теперь добавляем человека
        self.person = Person(
            self.screen,
            self.player,
            [
                pygame.transform.rotozoom(load_image(f'free-townspeople-cyberpunk-pixel-art/5/Idle_{i}.png'), 0, 3)
                for i in range(1, 4 + 1, 1)
            ],
            (700, 700),
            True,
            GoslingPersonDialogAction(screen),
            300,
        )

        # гифка сиреневой девки
        self.purple_girl = []
        for idx in range(0, 60, 4):
            self.purple_girl.append(pygame.transform.scale(
                load_image(f'purple_girl/frame_{idx:02}_delay-0.02s.gif'),
                (448, 448 * 0.42 - 2)
            ))

        print(len(self.purple_girl))

        # гифка гослинга
        self.gosling_looking = []
        for idx in range(0, 15):
            self.gosling_looking.append(pygame.transform.scale(
                load_image(f'gosling_looking/frame_{idx:02}_delay-0.07s.gif'),
                (448, 448 * 0.42 - 2)
            ))

        self.start_time = pygame.time.get_ticks()

    def update(self):
        super().update()
        self.gosling_terminal.update(self.screen, self.player)

        # смотрим, какое время прошло
        elapsed_time = pygame.time.get_ticks() - self.start_time

        # обновляем положение девки
        current_frame = int((elapsed_time // 100) % 14)
        self.screen.blit(self.purple_girl[current_frame], (66, 70))

        # обновляем положение гослинга
        current_frame = int((elapsed_time // 500) % 14)
        self.screen.blit(self.gosling_looking[current_frame], (60 + 448, 70))

        # обновляем нашего человека
        self.person.update()

    def get_objs(self):
        objs = super().get_objs()
        objs.append(self.gosling_terminal)
        objs.append(self.person)
        return objs

    def get_terminal_action(self):
        for terminal in [self.gosling_terminal, self.person]:
            if terminal.get_using():  # если терминал используется
                return terminal.action
