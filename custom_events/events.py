import pygame

OPEN_TERMINAL = pygame.USEREVENT + 1  # открытие терминала
CLOSE_TERMINAL = pygame.USEREVENT + 2  # закрытие терминала

CREATE_NEW_GAME = pygame.USEREVENT + 3  # начало новой игры
LOAD_GAME = pygame.USEREVENT + 8  # загрузка сохранения

PLAYER_OUT_OF_RIGHT = pygame.USEREVENT + 4  # если игрок вышел за границы экрана направо
PLAYER_OUT_OF_LEFT = pygame.USEREVENT + 5  # если игрок вышел за границы налево
PLAYER_OUT_OF_UP = pygame.USEREVENT + 6  # если игрок вышел за границы вверх
PLAYER_OUT_OF_DOWN = pygame.USEREVENT + 7  # если игрок вышел за границы вниз

TERMINAL_COMPLETED = pygame.USEREVENT + 9  # если терминал пройден
TERMINAL_LOST = pygame.USEREVENT + 10  # если терминал был провален
