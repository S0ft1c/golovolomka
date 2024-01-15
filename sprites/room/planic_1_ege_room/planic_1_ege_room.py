from ..terminal1_room.terminal1_room import Terminal1Room
from utils import create_main_walls_with_exits, place_terminal
from sprites import AnimatedPlayer
from funcs.load_image import load_image


class Planic1EgeRoom(Terminal1Room):
    def __init__(self, screen, player, exits, compl=False):
        super().__init__(screen, player, exits)
        self.background = load_image('/room_assets/2 Background/planic_1_background.png')
        self.ege_terminal = place_terminal(447, 268, None)  # TODO: do the action

    def update(self):
        super().update()
        self.screen.blit(self.background, (0, 0))
        self.ege_terminal.update(self.screen, self.player)

    def get_objects(self):
        objs = self.room_main_walls.sprites()
        objs.append(self.brain_terminal)
        return objs
