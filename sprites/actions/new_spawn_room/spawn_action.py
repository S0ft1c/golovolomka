from ..action_parent import ActionParent
from .spawn_screen import NewSpawnGame


class NewSpawnGameAction(ActionParent):
    def __init__(self, screen):
        super().__init__(screen)

    def activate(self):
        super().activate()
        self.snake_game_screen = NewSpawnGame(self.screen)

    def get_the_action_screen(self):
        return self.snake_game_screen
