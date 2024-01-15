from ..action_parent import ActionParent
from .gosling_person_dialog_screen import GoslingPersonDialogScreen


class GoslingPersonDialogAction(ActionParent):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen = GoslingPersonDialogScreen(screen)

    def activate(self):
        super().activate()

    def get_the_action_screen(self):
        return self.screen
