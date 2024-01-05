import pygame
from .adds.bar import Bar
from .adds.ball import Ball
from .adds.cyberpunk_terminal import CyberpunkTerminal
from .adds.dead_screen import DeadScreen
from random import choice
from funcs.load_image import load_image


class PingPongGame:
    def __init__(self, screen):
        pygame.init()

        self.screen = screen

        self.clock = pygame.time.Clock()
        self.screen_rect = self.screen.get_rect()

        self.ball = Ball(self.screen_rect)
        self.bar = Bar(self.screen_rect)

        self.font = pygame.font.Font(None, 36)

        self.score = 0
        self.attempts = 3

        self.background_1 = pygame.transform.rotozoom(
            load_image('ping_pong/bg.png'),
            0,
            3,
        )
        self.background_2 = pygame.transform.rotozoom(
            load_image('ping_pong/bg-2.png'),
            0,
            3.8,
        )

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
            self.bar.update(keys)
            self.ball.update()

            if self.ball.rect.colliderect(self.bar.rect):
                if self.ball.rect.bottom < self.bar.rect.bottom - 33:
                    if self.ball.change_x <= 40:
                        self.ball.change_x += choice([0.5, 1, 3, 5, 8])
                    if self.ball.change_y <= 18:
                        self.ball.change_y += choice([1, 2, 3])
                    self.ball.change_y = -self.ball.change_y
                    self.score += 1

            if self.ball.rect.bottom >= self.bar.rect.bottom - 5:
                self.attempts -= 1
                self.ball.rect.x = self.screen_rect.right // 2
                self.ball.rect.y = self.screen_rect.top + 65
                self.ball.change_y = 5
                self.ball.change_x = 5

            self.draw()

            if self.attempts <= 0:
                self.died = True

            if self.score >= 30:
                self.completed = True

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background_1, (0, 0))
        self.screen.blit(self.background_2, (0, self.screen_rect.bottom - self.background_2.get_rect().bottom))
        self.ball.draw(self.screen)
        self.bar.blitme(self.screen)

        score_text_surface = self.font.render(f'Счёт: {self.score} / 30', True, (255, 255, 255))
        self.screen.blit(score_text_surface, (10, 10))

        attempts_text_surface = self.font.render(f'Попытки: {self.attempts}', True, (255, 255, 255))
        self.screen.blit(attempts_text_surface, (10, 40))

        pygame.display.flip()
