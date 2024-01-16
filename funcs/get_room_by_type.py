from sprites import SpawnRoom, Terminal1Room, Terminal1RoomMaxwellCat
from sprites.room.terminal1room_gosling.terminal1room_gosling import Terminal1RoomGosling
from sprites.room.terminal1room_ping_pong.terminal1room_ping_pong import Terminal1RoomPingPong
from sprites.room.terminal1room_snake.terminal1room_snake import Terminal1RoomSnake



def get_room_by_type(type: str, screen, player, exits=None):
    """
    Возвращает, какая комната соответствует определенной надписи в room_labirint
    :param exits: параметр, что позволяет классу комнаты понять, где рыть выходы
    :param player: Объект игрока, необходим, чтобы создать класс
    :param screen: Surface главного экрана
    :param type: какого типа надо открыть комнату
    :return: объект нужной комнаты
    """
    nt = type.replace('_compl', '')
    if nt == 'spawn_room':
        return SpawnRoom(screen, player)
    if nt == 'terminal1_room':
        return Terminal1Room(screen, player, exits)
    if nt == 'terminal1room_maxwell_cat':
        return Terminal1RoomMaxwellCat(screen, player, exits, compl=('_compl' in type))
    if nt == 'terminal1room_ping_pong':
        return Terminal1RoomPingPong(screen, player, exits, compl=('_compl' in type))
    if nt == 'terminal1room_gosling':
        return Terminal1RoomGosling(screen, player, exits, compl=('_compl' in type))
    if nt == 'terminal1room_snake':
        return Terminal1RoomSnake(screen, player, exits, compl=('_compl' in type))
