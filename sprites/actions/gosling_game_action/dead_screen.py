import pygame
import sys
from funcs.load_image import load_image
from custom_events import *


class DeadScreen:
    def __init__(self, screen):

        self.width = 1024
        self.height = 896
        self.screen = screen
        self.start_time = pygame.time.get_ticks()

        # Load images
        self.angry_gosling = [pygame.transform.rotozoom(
            load_image(f"rayan_gosling_angry/frame_{i:03}_delay-0.1s.gif").convert(),
            0,
            1,
        ) for i in range(187 + 1)]

        self.sad_gosling = [pygame.transform.rotozoom(
            load_image(f"sad_gosling/frame_{i:03}_delay-0.03s.gif"),
            0,
            0.8
        ) for i in range(136 + 1)]

        self.font = pygame.font.Font("data/futuremillennium/FutureMillennium.ttf", 36)
        self.text = self.font.render("YOU LOST GOSLING'S GAME?!?!!11!?11111", True, (255, 0, 0))
        self.text_rext = self.text.get_rect(center=(1024 / 2, 896 / 2))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(TERMINAL_LOST))

        # Blit the background image
        self.screen.fill((255, 255, 255))

        # render text
        self.screen.blit(self.text, self.text_rext)

        # render gifs
        elapsed_time = pygame.time.get_ticks() - self.start_time

        # angry gosling
        current_frame = int((elapsed_time // 100) % 187)
        self.screen.blit(self.angry_gosling[current_frame], (0, 0))

        # sad gosling
        current_frame = int((elapsed_time // 30) % 136)
        self.screen.blit(self.sad_gosling[current_frame], self.sad_gosling[current_frame].get_rect(bottomright=(1024, 896)))

        pygame.display.flip()
