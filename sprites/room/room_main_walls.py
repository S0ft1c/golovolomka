import pygame
from random import choice
from ..player.animated_player import AnimatedPlayer, player


class MainWall(pygame.sprite.Sprite):
    def __init__(self, rd_walls_list: list, x: int, y: int):
        super().__init__()
        self.image = choice(rd_walls_list)
        self.rect: pygame.Rect = self.image.get_rect(topleft=(x, y))
        self.last_speed = player.v  # получаем скорость персонажа изначально

    def check_collision(self, player: AnimatedPlayer):
        if self.rect.colliderect(player.rect):  # если пересекаются коллизии
            return True
        else:
            return False


# TODO: надо бы тут выбрать только определенные имена стен, думаю надо просто отобрать их в папке
rd_walls_list = [pygame.transform.rotozoom(
    pygame.image.load(f'static/room_assets/1_Tiles/IndustrialTile_{i:02d}.png').convert(),
    0, 2
)
    for i in range(1, 40 + 1, 1)
]
room_main_walls = pygame.sprite.Group()

# для начала верхний слой (каждая картинка будет на 64 пикселя после rotozoom)
for x in range(0, 1024, 64):
    wall = MainWall(rd_walls_list, x, 0)
    room_main_walls.add(wall)

# теперь добавляем слева
for y in range(64, 896, 64):
    wall = MainWall(rd_walls_list, 0, y)
    room_main_walls.add(wall)

# снизу
for x in range(64, 1024, 64):
    wall = MainWall(rd_walls_list, x - 64, 896 - 64)
    room_main_walls.add(wall)

# справа
for y in range(64, 896, 64):
    wall = MainWall(rd_walls_list, 1024 - 64, y)
    room_main_walls.add(wall)
