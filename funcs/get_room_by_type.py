from sprites import SpawnRoom, Terminal1Room


def get_room_by_type(type: str, screen, player, exits=None):
    """
    Возвращает, какая комната соответствует определенной надписи в room_labirint
    :param exits: параметр, что позволяет классу комнаты понять, где рыть выходы
    :param player: Объект игрока, необходим, чтобы создать класс
    :param screen: Surface главного экрана
    :param type: какого типа надо открыть комнату
    :return: объект нужной комнаты
    """
    if type == 'spawn_room':
        return SpawnRoom(screen, player)
    if type == 'terminal1_room':
        return Terminal1Room(screen, player, exits)
