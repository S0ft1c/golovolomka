from ..room_parent import RoomParent
from utils import create_main_walls_with_exits, place_terminal


class Terminal1Room(RoomParent):
    def __init__(self, screen, player, exits):
        super().__init__(screen, player)
        self.room_main_walls = create_main_walls_with_exits(*exits)
        # self.brain_terminal = place_terminal(410, 500, None)

    def update(self):
        super().update()
        self.room_main_walls.draw(self.screen)
        # self.brain_terminal.update(self.screen, self.player)

    def get_objs(self):
        objs = self.room_main_walls.sprites()
        # objs.append(self.brain_terminal)
        return objs

    def get_terminal_action(self):
        for terminal in [self.brain_terminal]:
            if terminal.get_using():  # если терминал используется
                return terminal.action
