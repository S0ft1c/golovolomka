import pygame
from funcs.load_image import load_image


# TODO: сделать отзеркаленный массив для анимации бега назад (только назад и хватит)
class AnimatedPlayer(pygame.sprite.Sprite):

    def __init__(self, idle_img, images, x, y):
        super().__init__()

        self.idle_img = idle_img
        self.images = images
        self.current_image = 0
        self.frame_rate = 10

        self.rect = self.images[int(self.current_image)].get_rect()
        self.rect.x = x
        self.rect.y = y

        self.moving = False
        self.v = 5  # скорость перемещения

    def update(self):
        # Проверяем, движется ли спрайт
        if self.moving:
            # Обновляем кадр анимации
            self.current_image += 0.1  # спец задержка для +- красивой анимации
            if self.current_image >= len(self.images):
                self.current_image = 0

            self.image = self.images[int(self.current_image)]
        else:
            # Устанавливаем первый кадр анимации
            self.current_image = 0
            self.image = self.idle_img  # ставим кадр, где стоит

    def move_left(self):
        self.rect.x -= self.v
        self.start_moving()

    def move_right(self):
        self.rect.x += self.v
        self.start_moving()

    def move_up(self):
        self.rect.y -= self.v
        self.start_moving()

    def move_down(self):
        self.rect.y += self.v
        self.start_moving()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def start_moving(self):
        self.moving = True

    def stop_moving(self):
        self.moving = False

    def to_left_side(self):
        self.rect.x = 0 + 30

    def to_right_side(self):
        self.rect.x = 1024 - 30

    def to_down_side(self):
        self.rect.y = 896 - 30

    def to_up_side(self):
        self.rect.y = 0 + 30


# creation of the player
idle_img = pygame.transform.rotozoom(pygame.image.load("data/Cyborg/Cyborg_idle_0.png"), 0, 3).convert_alpha()
images = [  # TODO: добавить побольше кадров (они есть в статике, мне было просто лень)
    pygame.transform.rotozoom(load_image("Cyborg/Cyborg_run_0.png"), 0, 3).convert_alpha(),
    pygame.transform.rotozoom(load_image("Cyborg/Cyborg_run_1.png"), 0, 3).convert_alpha(),
    pygame.transform.rotozoom(load_image("Cyborg/Cyborg_run_2.png"), 0, 3).convert_alpha(),
    pygame.transform.rotozoom(load_image("Cyborg/Cyborg_run_3.png"), 0, 3).convert_alpha(),
]
player = AnimatedPlayer(idle_img, images, 100, 100)
