from ..action_parent import ActionParent
from .maxwell_game_screen import LaserHuntGame


class MaxwellGameAction(ActionParent):
    def __init__(self, screen):
        super().__init__(screen)

    def activate(self):
        super().activate()
        self.hunt_game_screen = LaserHuntGame(self.screen)

    def get_the_action_screen(self):
        return self.hunt_game_screen
