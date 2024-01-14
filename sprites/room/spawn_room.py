from .room_parent import RoomParent
from utils import create_main_walls_with_exits, place_terminal
from sprites import AnimatedPlayer
from funcs.load_image import load_image


class SpawnRoom(RoomParent):
    def __init__(self, screen, player: AnimatedPlayer):
        super().__init__(screen, player)
        self.background = load_image("room_assets/2 Background/spawn_background.png")
        self.room_main_walls = create_main_walls_with_exits('left', 'right')
        self.brain_terminal = place_terminal(500, 500, None)

    def update(self):
        super().update()
        self.screen.blit(self.background, (0, 0))  # blit the background
        self.room_main_walls.draw(self.screen)
        self.brain_terminal.update(self.screen, self.player)

    def get_objs(self):
        objs = self.room_main_walls.sprites()
        objs.append(self.brain_terminal)
        return objs

    def get_terminal_action(self):  # Просто надо писать эту функцию
        pass
        # for terminal in [self.brain_terminal]:
        #     if terminal.get_using():  # если терминал используется
        #         return terminal.action
