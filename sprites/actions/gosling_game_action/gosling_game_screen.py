import pygame.font
import os
from custom_events import *
from funcs.load_image import load_image
import sys
import random
from .dead_screen import DeadScreen
from .victory_screen import VictoryScreen


class Car(pygame.sprite.Sprite):
    def __init__(self, image, x, y, speed, w, h):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed
        self.WIDTH = w
        self.HEIGHT = h

    def move(self, dx=0, dy=0):
        self.rect.x += dx
        self.rect.y += dy


class PlayerCar(Car):
    def handle_input(self):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0

        if keys[pygame.K_UP] and self.rect.top > 0:
            dy = -self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < self.HEIGHT:
            dy = self.speed

        self.move(dx, dy)


class EnemyCar(Car):
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.respawn()

    def respawn(self):
        self.rect.x = self.WIDTH + random.randint(20, 100)
        self.rect.y = random.randint(0, self.HEIGHT - 43)


class GoslingGameScreen:
    def __init__(self, screen):
        # Constants
        self.WIDTH, self.HEIGHT = 1024, 896
        self.FPS = 60
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.CAR_WIDTH, self.CAR_HEIGHT = 50, 30
        self.ENEMY_CAR_WIDTH, self.ENEMY_CAR_HEIGHT = 52, 43
        self.CAR_SPEED = 5
        self.ENEMY_CAR_SPEED = 5
        self.HEALTH = 3
        self.TIMER = 120  # seconds
        self.END_TIME = pygame.time.get_ticks() + self.TIMER * 1000  # convert seconds to milliseconds

        # Set up the game window
        self.screen = screen

        self.ds = DeadScreen(self.screen)
        self.vs = VictoryScreen(self.screen)

        # Load images
        self.car_image = load_image("free-bosses-pixel-art-sprite-sheet-pack/2/Walk1.png")
        self.enemy_car_image = load_image("free-bosses-pixel-art-sprite-sheet-pack/1/Walk1.png")

        # Create player car sprite
        self.player_car = PlayerCar(self.car_image, 50, self.HEIGHT // 2, self.CAR_SPEED, self.WIDTH, self.HEIGHT)
        self.player_group = pygame.sprite.GroupSingle(self.player_car)

        self.font = pygame.font.Font('./data/futuremillennium/FutureMillennium.ttf', 30)

        # Create enemy cars sprites
        self.enemy_group = pygame.sprite.Group()
        for _ in range(15):
            self.spawn_enemy_car()

    def spawn_enemy_car(self):
        x = self.WIDTH + random.randint(20, 100)
        y = random.randint(self.ENEMY_CAR_HEIGHT // 2, self.HEIGHT - self.ENEMY_CAR_HEIGHT // 2)
        enemy_car = EnemyCar(self.enemy_car_image, x, y, self.ENEMY_CAR_SPEED, self.WIDTH, self.HEIGHT)
        self.enemy_group.add(enemy_car)

    def move_cars(self):
        self.enemy_group.update()

    def check_collisions(self):
        # Check for collisions with the enemy cars
        if pygame.sprite.spritecollide(self.player_car, self.enemy_group, dokill=True):
            self.HEALTH -= 1

    def respawn_enemy_cars(self):
        if len(self.enemy_group) < 15:
            self.spawn_enemy_car()

        for enemy_car in self.enemy_group:
            if enemy_car.rect.right < 0:
                self.enemy_group.remove(enemy_car)
                self.spawn_enemy_car()

    def draw_objects(self):
        # Draw everything
        self.screen.fill(self.BLACK)
        self.player_group.draw(self.screen)
        self.enemy_group.draw(self.screen)

        # Display health and time
        health_text = self.font.render(f"Health: {self.HEALTH}", True, (255, 255, 255))
        time_text = self.font.render(f"Time: {self.TIMER - pygame.time.get_ticks() // 1000}", True, (255, 255, 255))
        self.screen.blit(health_text, (10, 10))
        self.screen.blit(time_text, (10, 40))

        pygame.display.flip()

    def update(self):
        # Game timer

        if self.HEALTH <= 0:
            self.ds.update()
            return

        # Check game timer
        current_time = pygame.time.get_ticks()
        if current_time > self.END_TIME and self.HEALTH > 0:
            self.vs.display_victory_screen()
            return

        self.player_car.handle_input()
        self.move_cars()
        self.check_collisions()
        self.respawn_enemy_cars()
        self.draw_objects()
