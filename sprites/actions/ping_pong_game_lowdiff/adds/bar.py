import pygame
from pygame.sprite import Sprite
from funcs.load_image import load_image


class Bar(Sprite):
    def __init__(self, screen_rect):
        super(Bar, self).__init__()
        self.image = pygame.transform.rotozoom(load_image('ping_pong/bar.png'), 0, 0.09)
        self.rect = self.image.get_rect()
        self.screen_rect = screen_rect
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 20
        self.change_x = 0

    def update(self, keys):
        if (keys[pygame.K_DOWN] or keys[pygame.K_LEFT]) and self.rect.left > 0:
            self.rect.x -= 10
        if (keys[pygame.K_DOWN] or keys[pygame.K_RIGHT]) and self.rect.right < self.screen_rect.right:
            self.rect.x += 10

    def blitme(self, screen):
        screen.blit(self.image, self.rect.topleft)