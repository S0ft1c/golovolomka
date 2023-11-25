import sys
import pygame
import sprites as sp
import utils


def main(screen: pygame.Surface):
    # create a timer
    clock = pygame.time.Clock()

    # background creation
    background = pygame.transform.rotozoom(
        pygame.image.load('static/room_assets/2 Background/1.png'),
    0, 4,
    )
    background_rect = background.get_rect()

    # main loop
    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # exit
                running = False

        # проверяем, надо ли показывать подсказку с буковой E
        utils.terminal_hint_check(sp.terminal, sp.player)

        # check for the movement inputs
        objs = sp.room_main_walls.sprites()  # тут мы создаем список всех активных объектов
        objs.append(sp.terminal)
        utils.player_movement_inputs_check(sp.player, objs)

        screen.blit(background, background_rect)  # clear all the screen

        # player logic
        sp.player.update()
        sp.player.draw(screen)

        # main walls logic
        sp.room_main_walls.draw(screen)

        # terminal logic
        sp.terminal.update(screen)

        pygame.display.flip()  # update the screen
        clock.tick(60)

    pygame.quit()
    sys.exit()
