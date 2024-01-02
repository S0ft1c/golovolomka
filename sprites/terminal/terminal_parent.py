import pygame
from ..player.animated_player import AnimatedPlayer


class TerminalParent(pygame.sprite.Sprite):
    def __init__(self, image, x, y, action):
        """
        Метод инициализации. Тут представлен абсолютный минимум.
        :param image: Сама картинка терминала
        :param x: Координата верхнего левого угла по x
        :param y: Координата верхнего левого угла по y
        :param action: объект класса, унаследованного от ActionParent
        """
        super().__init__()
        self.image: pygame.Surface = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.action = action
        self.is_near = False
        self.using = False

    def update(self, screen, player: AnimatedPlayer):
        """
        Метод, где прописываются все взаимодействия, а также отображения на экране.
        :param screen: Главный экран, где все отображается
        :param player: объект класса AnimatedPlayer. Необходим для работы функций взаимодействия
        :return: None
        """

        # пример ф-ии взаимодействия с терминалом.
        # length = ((player.rect.x - self.rect.x) ** 2 + (player.rect.y - self.rect.y) ** 2) ** 0.5
        # if length <= 100:  # если расстояние от персонажа и до терминала меньше 10ти пикселей
        #     keys = pygame.key.get_pressed()
        #     if keys[pygame.K_e]:  # если он нажал кнопку E
        #         self.use_terminal()

        print('Не определен метож update в Terminal')

    def check_collision(self, player: AnimatedPlayer):
        """
        Этот метод нужен для проверки на коллизии игрока и самого терминала.
        :param player: Объект класса AnimatedPlayer
        :return: bool
        """
        if self.rect.colliderect(player.rect):  # если пересекаются коллизии
            return True
        else:
            return False

    def use_terminal(self):
        """
        Если пользователь начинает взаимодействие, то включается это.
        :return: None
        """
        self.using = True
        self.action.activate()

    def get_using(self):
        """
        Геттер для возврата значения using
        :return: bool
        """
        return self.using
