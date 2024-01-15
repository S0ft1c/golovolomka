import pygame
from pygame.sprite import Sprite
from funcs.load_image import load_image


class Ball(Sprite):
    def __init__(self, screen_rect):
        super(Ball, self).__init__()
        self.image = pygame.transform.rotozoom(load_image("ping_pong/ball.png"), 0, 0.03)
        self.rect = self.image.get_rect()
        self.screen_rect = screen_rect
        self.change_x = 5
        self.change_y = 5
        self.rect.x = self.screen_rect.centerx
        self.rect.y = self.screen_rect.top + 50

    def update(self):
        if self.rect.right + self.change_x >= self.screen_rect.right or self.rect.left <= 0:
            self.change_x = -self.change_x
        self.rect.x += self.change_x

        if self.rect.bottom + self.change_y >= self.screen_rect.bottom or self.rect.top <= 0:
            self.change_y = -self.change_y
        self.rect.y += self.change_y

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)