import pygame
from ..player.animated_player import AnimatedPlayer
from .terminal_parent import TerminalParent

# штучка, чтобы давать колизию добавляемым в комнату объектам


class Border(TerminalParent):
    def __init__(self, image, x, y, action=None):
        super().__init__(image, x, y, action)

    def update(self, screen, player: AnimatedPlayer):
        screen.blit(self.image, self.rect)
