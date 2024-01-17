import pygame
from .adds.snake import Snake
from .adds.cyberpunk_terminal import CyberpunkTerminal
from .adds.dead_screen import DeadScreen
from random import choice, randrange
from funcs.load_image import load_image


class SnakeGame:
    def __init__(self, screen):
        pygame.init()

        self.screen = screen

        self.clock = pygame.time.Clock()
        self.screen_rect = self.screen.get_rect()

        self.snake = Snake(self.screen_rect)
        self.food_size = 40
        self.fps = 5
        self.food_pos = (randrange(1, (self.screen_rect.right // self.snake.snake_size)) * self.snake.snake_size,
                         randrange(1, (self.screen_rect.bottom // self.snake.snake_size)) * self.snake.snake_size)

        self.font = pygame.font.Font(None, 36)

        self.score = 0

        self.background_1 = pygame.transform.scale(load_image('snake/back1.png'), (1024, 896))

        self.completed = False  # пройдена головоломка или нет
        self.died = False  # проиграл он или нет

        # это экраны для смерти и победы
        self.ct = CyberpunkTerminal(self.screen)
        self.ds = DeadScreen(self.screen)

    def update(self):
        if self.died:
            self.ds.display_dead_screen()
        elif self.completed:
            self.ct.display_cyberpunk_screen()
        else:
            keys = pygame.key.get_pressed()
            self.snake.update(keys)

            # проверка на удар со стенами
            head_x, head_y = self.snake.new_head_pos
            if head_x < 0 or head_x >= self.screen_rect.right or head_y < 0 or head_y >= self.screen_rect.bottom:
                self.died = True

            self.snake.snake_pos.insert(0, self.snake.new_head_pos)

            # проверка на схаваную еду
            if self.snake.new_head_pos == self.food_pos:
                self.score += 1
                self.fps += 1
                self.food_pos = (
                    randrange(1, (self.screen_rect.right // self.snake.snake_size)) * self.snake.snake_size,
                    randrange(1, (self.screen_rect.bottom // self.snake.snake_size)) * self.snake.snake_size)

            else:
                # Если не съедено, удалить последний сегмент тела
                self.snake.snake_pos.pop()

            self.draw()

            if self.score >= 12:
                self.completed = True

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.background_1, (0, 0))
        self.snake.blitme(self.screen)
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.food_pos[0], self.food_pos[1], self.food_size,
                                                                  self.food_size))


        score_text_surface = self.font.render(f'Счёт: {self.score} / 12', True, (255, 255, 255))
        self.screen.blit(score_text_surface, (10, 10))

        pygame.display.flip()
        self.clock.tick(self.fps)
