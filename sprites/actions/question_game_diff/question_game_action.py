from ..action_parent import ActionParent
from .question_game_screen import QuestionGame


class QuestionGameAction(ActionParent):
    def __init__(self, screen):
        super().__init__(screen)

    def activate(self):
        super().activate()
        self.snake_game_screen = QuestionGame(self.screen, 'Как называется столица Гавайев?', 'Окаху', 'Кахулуи',
                                              'Гонолулу', 'Пёрл-сити', 3)

    def get_the_action_screen(self):
        return self.snake_game_screen
