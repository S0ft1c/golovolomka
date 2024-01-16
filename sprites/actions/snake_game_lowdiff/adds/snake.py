import pygame
from pygame.sprite import Sprite
from funcs.load_image import load_image


class Snake(Sprite):
    def __init__(self, screen_rect):
        super(Snake, self).__init__()
        self.screen_rect = screen_rect
        self.snake_size = 40
        self.snake_speed = 40
        self.snake_pos = [(200, 200)]
        self.snake_direction = ['LEFT']

    def update(self, keys):
        if keys[pygame.K_UP] and self.snake_direction != 'DOWN':
            self.snake_direction = 'UP'
        if keys[pygame.K_DOWN] and self.snake_direction != 'UP':
            self.snake_direction = 'DOWN'
        if keys[pygame.K_LEFT] and self.snake_direction != 'RIGHT':
            self.snake_direction = 'LEFT'
        if keys[pygame.K_RIGHT] and self.snake_direction != 'LEFT':
            self.snake_direction = 'RIGHT'

        head_x, head_y = self.snake_pos[0]
        if self.snake_direction == 'UP':
            head_y -= self.snake_speed
        elif self.snake_direction == 'DOWN':
            head_y += self.snake_speed
        elif self.snake_direction == 'LEFT':
            head_x -= self.snake_speed
        elif self.snake_direction == 'RIGHT':
            head_x += self.snake_speed
        self.new_head_pos = (head_x, head_y)

    def blitme(self, screen):
        for pos in self.snake_pos:
            pygame.draw.rect(screen, (173, 216, 230), pygame.Rect(pos[0], pos[1], self.snake_size, self.snake_size))
