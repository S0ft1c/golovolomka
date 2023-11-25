import pygame
from ..player.animated_player import AnimatedPlayer


class Terminal(pygame.sprite.Sprite):
    def __init__(self, image, x, y, action):
        super().__init__()

        self.image: pygame.Surface = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.action = action
        self.is_near = False

    def update(self, screen):
        # TODO: сделать анимацию подсказки для терминала на буковку E

        # просто обновляем информацию по поводу терминала
        screen.blit(self.image, self.rect)

    def check_collision(self, player: AnimatedPlayer):
        if self.rect.colliderect(player.rect):  # если пересекаются коллизии
            return True
        else:
            return False


image = pygame.transform.rotozoom(
    pygame.image.load('static/room_assets/terminal.png'),
    0, 0.5
).convert()

terminal = Terminal(image, 250, 250, None)
