import pygame
from sprites.actions import MaxwellGameAction, TerminalCompletedAction
from ..terminal1_room.terminal1_room import Terminal1Room
from utils import place_terminal
from funcs.load_image import load_image


class Terminal1RoomMaxwellCat(Terminal1Room):
    def __init__(self, screen, player, exits, compl=False):
        super().__init__(screen, player, exits)

        if not compl:
            self.maxwell_terminal = place_terminal(410, 500, MaxwellGameAction(self.screen))
        else:
            self.maxwell_terminal = place_terminal(410, 500, TerminalCompletedAction(self.screen))

        # дальше все для гифки
        self.maxwell_cat = []
        for idx in range(0, 56 + 1):
            self.maxwell_cat.append(pygame.transform.rotozoom(
                load_image(f'maxwell_cat/frame_{idx:02}_delay-0.1s.gif'),
                0,
                0.5,
            ))

        self.frame_delay = 100
        self.start_time = pygame.time.get_ticks()

        # для текста
        # Создаем объект шрифта
        font = pygame.font.Font(None, 36)  # Вы можете выбрать другой шрифт и размер

        # Создаем изображение текста
        self.text_surface = font.render('I have your IP address', True, pygame.Color('white'))

        # Получаем прямоугольник, содержащий изображение текста
        self.text_rect = self.text_surface.get_rect()

        # Устанавливаем координаты текста
        self.text_rect.topleft = (200, 180)

    def update(self):
        super().update()
        self.maxwell_terminal.update(self.screen, self.player)

        elapsed_time = pygame.time.get_ticks() - self.start_time
        current_frame = int((elapsed_time // self.frame_delay) % 57)

        self.screen.blit(self.maxwell_cat[current_frame], (200, 200))
        # Отображаем текст на экране
        self.screen.blit(self.text_surface, self.text_rect)

    def get_objs(self):
        objs = super().get_objs()
        objs.append(self.maxwell_terminal)
        return objs
    
    def get_terminal_action(self):
        for terminal in [self.maxwell_terminal]:
            if terminal.get_using():  # если терминал используется
                return terminal.action
