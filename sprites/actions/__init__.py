# импортировать сюда следует исключительно Action

from .start_game_action.start_game_action import StartGameAction
from .load_save_action.load_save_action import LoadSaveAction
from .maxwell_game_lowdiff.maxwell_game_action import MaxwellGameAction
from .ping_pong_game_lowdiff.ping_pong_game_action import PingPongGameAction
from .snake_game_lowdiff.snake_game_action import SnakeGameAction
from .question_game_diff.question_game_action import QuestionGameAction
from .q2_game_lowdiff.q2_game_action import Q2GameAction
from .new_spawn_room.spawn_action import NewSpawnGameAction

from sprites.actions.terminal_completed_action.termial_completed import TerminalCompleted
from .terminal_completed_action.terminal_completed_action import TerminalCompletedAction
from .gosling_person_dialog.gosling_person_dialog_action import GoslingPersonDialogAction
from .gosling_game_action.gosling_game_action import GoslingGameAction
