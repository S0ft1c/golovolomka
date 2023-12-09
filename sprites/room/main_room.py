from utils import create_main_walls, place_terminal
from .room_parent import RoomParent
from sprites.actions import StartGameAction
from sprites import AnimatedPlayer


class MainRoom(RoomParent):
    def __init__(self, screen, player: AnimatedPlayer):
        super().__init__(screen, player)
        self.room_main_walls = create_main_walls()  # create the main walls
        self.start_game_action = StartGameAction(screen)
        self.start_game_terminal = place_terminal(250, 250, self.start_game_action)  # create the terminal start game

    def update(self):  # это метод отвечающий за обновление всех элементов комнаты
        super().update()
        self.room_main_walls.draw(self.screen)
        self.start_game_terminal.update(self.screen, self.player)

    def get_objs(self):
        objs = self.room_main_walls.sprites()
        objs.append(self.start_game_terminal)
        return objs

    def get_terminal_action(self):  # комната с терминалами, так что
        for terminal in [self.start_game_terminal]:
            if terminal.get_using():  # если терминал используется
                return terminal.action
