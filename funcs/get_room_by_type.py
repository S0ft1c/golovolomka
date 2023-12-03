from sprites import SpawnRoom


def get_room_by_type(type: str, screen, player):
    """
    Возвращает, какая комната соответствует определенной надписи в room_labirint
    :param player: Объект игрока, необходим, чтобы создать класс
    :param screen: Surface главного экрана
    :param type: какого типа надо открыть комнату
    :return: объект нужной комнаты
    """
    if type == 'spawn_room':
        return SpawnRoom(screen, player)
