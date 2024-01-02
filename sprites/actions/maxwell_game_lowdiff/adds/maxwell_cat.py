import pygame
from pygame.sprite import Sprite
from funcs.load_image import load_image


class MaxwellCat(Sprite):
    def __init__(self, screen_rect):
        super(MaxwellCat, self).__init__()
        self.image = load_image('maxwell_cat_pic.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen_rect
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < self.screen_rect.right:
            self.rect.x += 5

    def blitme(self, screen):
        screen.blit(self.image, self.rect)
