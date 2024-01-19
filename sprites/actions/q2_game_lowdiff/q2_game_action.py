from ..action_parent import ActionParent
from sprites.actions.question_game_diff.question_game_action import QuestionGame


class Q2GameAction(ActionParent):
    def __init__(self, screen):
        super().__init__(screen)

    def activate(self):
        super().activate()
        self.snake_game_screen = QuestionGame(self.screen, 'Вычислите ((2 + 1) * 3)! ', '720', '945 932',
                                              '362 880', '54 881', 3)

    def get_the_action_screen(self):
        return self.snake_game_screen
