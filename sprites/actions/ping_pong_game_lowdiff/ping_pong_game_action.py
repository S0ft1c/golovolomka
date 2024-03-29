from ..action_parent import ActionParent
from .ping_pong_game_screen import PingPongGame


class PingPongGameAction(ActionParent):
    def __init__(self, screen):
        super().__init__(screen)

    def activate(self):
        super().activate()
        self.ping_pong_game_screen = PingPongGame(self.screen)

    def get_the_action_screen(self):
        return self.ping_pong_game_screen
