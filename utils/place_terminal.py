import pygame
from funcs.load_image import load_image
from sprites import Terminal


def place_terminal(x: int, y: int, action=None):
    image = pygame.transform.rotozoom(
        load_image('room_assets/terminal.png'),
        0, 0.5
    ).convert()

    terminal = Terminal(image, x, y, action)
    return terminal
