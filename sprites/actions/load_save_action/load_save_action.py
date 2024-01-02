from ..action_parent import ActionParent
from .load_save_screen import LoadSaveScreen


class LoadSaveAction(ActionParent):
    def __init__(self, screen):
        super().__init__(screen)

    def activate(self):
        super().activate()
        self.load_save_screen = LoadSaveScreen(self.screen)

    def get_the_action_screen(self):
        return self.load_save_screen

    def get_load_save_id(self):
        return self.load_save_screen.get_selected_saves()
