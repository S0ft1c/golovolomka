from ..action_parent import ActionParent
from .termial_completed import TerminalCompleted


class TerminalCompletedAction(ActionParent):
    def __init__(self, screen):
        super().__init__(screen)
        self.terminal_completed = TerminalCompleted(screen)

    def activate(self):
        super().activate()

    def get_the_action_screen(self):
        return self.terminal_completed
