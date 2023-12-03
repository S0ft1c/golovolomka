import sys
import pygame
import sprites as sp
import utils
from funcs.load_image import load_image  # kinda cringe
from funcs.get_room_by_type import get_room_by_type
from custom_events import *


def main(screen: pygame.Surface):
    # create a timer
    clock = pygame.time.Clock()

    # background creation
    background = pygame.transform.rotozoom(
        load_image('room_assets/2 Background/1.png'),
        0, 4,
    )
    background_rect = background.get_rect()

    # логика на комнаты, тут такое происходит...
    was_room = 'main_room'  # тут храним, какая комната была еще до захода в терминал
    cur_state = 'main_room'
    room = sp.MainRoom(screen, sp.player)
    rooms_labirint = []
    terminal_action = None  # изначально пользователь не в терминале
    difficulty = 0

    # main loop
    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # exit
                running = False

            if event.type == OPEN_TERMINAL:  # если пользователь открывает терминал, то мы изменяем статус
                was_room = cur_state
                cur_state = 'interminal'

                # нам надо понять, какой именно терминал заработал
                terminal_action = room.get_terminal_action().get_the_action_screen()

            if event.type == CLOSE_TERMINAL:  # если мы закрываем терминал
                cur_state = was_room

            if event.type == CREATE_NEW_GAME:  # делаем новую игру
                # TODO: добавить создание нового сохранения
                difficulty = 1  # TODO: реализовать полноценную функцию по расчету ф-ии сложности
                rooms_labirint = utils.room_creation(difficulty)

                # сразу проставляем, где мы находимся
                cur_state = 1

        if cur_state != 'interminal':

            # если комната поменялась
            if was_room != cur_state:
                # получаем новую комнату
                room = get_room_by_type(rooms_labirint[cur_state]['type'], screen, sp.player)
                was_room = cur_state  # теперь мы окончательно здесь

            # проверяем коллизии
            objs = room.get_objs()
            utils.player_movement_inputs_check(sp.player, objs)

            screen.blit(background, background_rect)  # clear all the screen

            # player logic
            sp.player.update()
            sp.player.draw(screen)

            # room update logic
            room.update()
        else:
            terminal_action.update()

        pygame.display.flip()  # update the screen
        clock.tick(60)

    pygame.quit()
    sys.exit()
