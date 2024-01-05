import pygame
from pygame.sprite import Sprite
import random
from funcs.load_image import load_image


class LaserPoint(Sprite):
    def __init__(self, screen_rect):
        super(LaserPoint, self).__init__()
        self.image = pygame.transform.rotozoom(
            load_image("mine_craft_apple.png"),
            0,
            0.25
        )
        self.rect = self.image.get_rect()
        self.screen_rect = screen_rect
        self.rect.x = random.randint(0, self.screen_rect.width - self.rect.width)
        self.rect.y = random.randint(-50, -10)  # Новые квадратики появляются сверху экрана
        self.speed = random.randint(1, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > self.screen_rect.bottom:
            self.rect.y = random.randint(-50, -10)
            self.rect.x = random.randint(0, self.screen_rect.width - self.rect.width)
