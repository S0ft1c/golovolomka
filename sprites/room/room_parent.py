class RoomParent:
    def __init__(self):
        pass

    def update(self):
        """
        Отвечает за отображение необходимого, а также и счета нажатий и клавиш.
        :return: None
        """
        print('Не определен метод update')

    def get_objs(self):
        """
        Это метод, который необходим для подсчета всех элементов, что могут иметь коллизию.
        :return: list, в котором лежат все такие элементы
        """
        print('Не определен метод get_objs')

    """
    Если это комната с терминалом, то надо еще добавить метод get_terminal_action() который будет выглядеть вот так:
    
    def get_terminal_action(self):
        for terminal in [<тут все объекты, что за терминалы>]:
            if terminal.get_using():  # если терминал используется
                return terminal.action
    
    """
