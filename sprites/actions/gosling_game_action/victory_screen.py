import pygame
from custom_events import *


class VictoryScreen:
    def __init__(self, screen):

        self.width = 1024
        self.height = 896
        self.screen = screen

        # Set font and size for the congrats text
        self.font = pygame.font.Font("data/futuremillennium/FutureMillennium.ttf", 36)

    def display_victory_screen(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(TERMINAL_COMPLETED))

        # Display victory screen
        pygame.draw.rect(self.screen, (0, 255, 0), (0, 0, self.width, self.height))
        congrats_text = self.font.render("Congratulations!", True, (255, 255, 255))
        self.screen.blit(congrats_text, (self.width // 2 - congrats_text.get_width() // 2,
                                          self.height // 2 - congrats_text.get_height() // 2))

        pygame.display.flip()