import pygame
from sprites import AnimatedPlayer, MainWall


def player_movement_inputs_check(player: AnimatedPlayer, objs: list):

    lx, ly = player.rect.x, player.rect.y  # сохраняем последние координаты персонажа

    # сначала двигаемся
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.move_left()
    elif keys[pygame.K_d]:
        player.move_right()
    elif keys[pygame.K_w]:
        player.move_up()
    elif keys[pygame.K_s]:
        player.move_down()
    else:
        player.stop_moving()

    # проверяем на коллизии главных стен (после движения)
    walls_collision = False
    for obj in objs:
        if obj.check_collision(player):
            walls_collision = True
            break

    if walls_collision:  # если же коллизия есть, то меняем на то, что было до нарушения
        player.rect.x, player.rect.y = lx, ly
