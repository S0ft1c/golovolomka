# TODO: после того, как будет сделана БД с сохранениями, мы будем выбирать сложность
def room_creation(difficulty: int):
    terminal_rooms_count = 3

    # default room
    spawn_room = {'left': 'end_level', 'right': 'terminal1_room', 'top': 'no', 'bottom': 'no'}
