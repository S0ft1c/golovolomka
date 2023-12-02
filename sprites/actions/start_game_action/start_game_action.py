from .start_game_screen import StartGameScreen
from ..action_parent import ActionParent


class StartGameAction(ActionParent):
    def __init__(self, screen):
        super().__init__(screen)

    def activate(self):  # активируем событие, которое означает открытие терминала
        super().activate()  # *ЭТО НАДО ПИСАТЬ*
        self.start_game_screen = StartGameScreen(self.screen)

    def get_the_action_screen(self):
        return self.start_game_screen
