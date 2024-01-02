import pygame
from random import choice
from ..player.animated_player import AnimatedPlayer, player


class MainWall(pygame.sprite.Sprite):
    def __init__(self, rd_walls_list: list, x: int, y: int):
        super().__init__()
        self.image = choice(rd_walls_list)
        self.rect: pygame.Rect = self.image.get_rect(topleft=(x, y))
        self.last_speed = player.v  # получаем скорость персонажа изначально

    def check_collision(self, player: AnimatedPlayer):
        if self.rect.colliderect(player.rect):  # если пересекаются коллизии
            return True
        else:
            return False
