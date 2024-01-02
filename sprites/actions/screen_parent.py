import pygame


class ScreenParent:
    def __init__(self, screen: pygame.Surface):  # обязательно получаем screen.
        super().__init__()
        self.screen = screen

    def update(self):  # метод, что отвечает за отображение элементов терминала, а также считывание клавиш, нажатий...
        print('Не определен метод update в Screen')
