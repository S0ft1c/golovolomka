import pygame
from funcs.load_image import load_image
from sprites import MainWall


def create_main_walls_with_exits(*args):
    """
    Делает главные стенки, в зависимости от принимаемых параметров в args
    :param args: где надо сделать дырки: 'up', 'down', 'left', 'right'
    :return: room_main_walls - pygame.sprites.Group
    """

    rd_walls_list = [pygame.transform.rotozoom(
        load_image(f'room_assets/1_Tiles/IndustrialTile_{i:02d}.png').convert(),
        0, 2
    )
        for i in range(1, 40 + 1, 1)
    ]
    room_main_walls = pygame.sprite.Group()

    # для начала верхний слой (каждая картинка будет на 64 пикселя после rotozoom)
    for x in range(0, 1024, 64):
        if 'up' in args and (x == 512 or x == 448):  # если у нас должна быть дырень
            continue

        wall = MainWall(rd_walls_list, x, 0)
        room_main_walls.add(wall)

    # теперь добавляем слева
    for y in range(64, 896, 64):
        if 'left' in args and (y == 512 or y == 448):  # если у нас должна быть дырень
            continue

        wall = MainWall(rd_walls_list, 0, y)
        room_main_walls.add(wall)

    # снизу
    for x in range(64, 1024, 64):
        if 'down' in args and (x == 512 or x == 448):  # если у нас должна быть дырень
            continue

        wall = MainWall(rd_walls_list, x - 64, 896 - 64)
        room_main_walls.add(wall)

    # справа
    for y in range(64, 896, 64):
        if 'right' in args and (y == 512 or y == 448):  # если у нас должна быть дырень
            continue

        wall = MainWall(rd_walls_list, 1024 - 64, y)
        room_main_walls.add(wall)

    return room_main_walls
