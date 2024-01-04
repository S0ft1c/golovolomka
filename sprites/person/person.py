import pygame


class Person:
    def __init__(self,
                 screen: pygame.Surface, player, imgs: list, position: tuple, flip: bool, action, update_interval):
        self.screen = screen
        self.imgs = imgs
        self.position = position
        self.flip = flip
        self.action = action
        self.player = player

        if self.flip:
            self.imgs = [pygame.transform.flip(image, True, False) for image in self.imgs]

        self.cur_image_idx = 0
        self.last_update_time = 0
        self.update_interval = update_interval
        self.using = False
        self.rect = self.imgs[self.cur_image_idx].get_rect(topleft=position)

    def update(self):
        # отображение анимации
        self.screen.blit(self.imgs[self.cur_image_idx], self.rect)

        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.last_update_time

        if elapsed_time >= self.update_interval:
            self.cur_image_idx = (self.cur_image_idx + 1) % len(self.imgs)
            self.last_update_time = current_time

        # работа с взаимодействием
        length = ((self.player.rect.x - self.rect.x) ** 2 + (self.player.rect.y - self.rect.y) ** 2) ** 0.5
        if length <= 100:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_e]:  # если он нажал кнопку E
                self.talk()

    def talk(self):
        self.using = True
        self.action.activate()

    def check_collision(self, player):
        return self.rect.colliderect(player.rect)

    def get_using(self):
        return self.using
