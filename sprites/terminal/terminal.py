import pygame
from ..player.animated_player import AnimatedPlayer
from .terminal_parent import TerminalParent


class Terminal(TerminalParent):
    def __init__(self, image, x, y, action):
        super().__init__(image, x, y, action)

    def update(self, screen, player: AnimatedPlayer):
        # смотрим, может ли игрок нажать по расстоянию
        length = ((player.rect.x - self.rect.x) ** 2 + (player.rect.y - self.rect.y) ** 2) ** 0.5
        if length <= 100:  # если расстояние от персонажа и до терминала меньше 10ти пикселей
            keys = pygame.key.get_pressed()
            if keys[pygame.K_e]:  # если он нажал кнопку E
                self.use_terminal()

        # TODO: сделать анимацию подсказки для терминала на буковку E

        # просто обновляем информацию по поводу терминала
        screen.blit(self.image, self.rect)
