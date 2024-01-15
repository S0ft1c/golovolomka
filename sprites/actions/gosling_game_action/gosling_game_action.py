from ..action_parent import ActionParent
from .gosling_game_screen import GoslingGameScreen


class GoslingGameAction(ActionParent):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen = GoslingGameScreen(screen)

    def activate(self):
        super().activate()

    def get_the_action_screen(self):
        return self.screen
