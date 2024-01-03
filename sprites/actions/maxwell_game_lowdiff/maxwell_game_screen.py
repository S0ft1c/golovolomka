import pygame
from pygame.sprite import Group
from .adds.maxwell_cat import MaxwellCat
from .adds.laser_point import LaserPoint
from .adds.cyberpunk_terminal import CyberpunkTerminal
from .adds.dead_screen import DeadScreen
import time
from funcs.load_image import load_image


class LaserHuntGame:
    def __init__(self, screen):
        pygame.init()

        self.screen = screen

        self.clock = pygame.time.Clock()
        self.screen_rect = self.screen.get_rect()

        self.maxwell_cat = MaxwellCat(self.screen_rect)
        self.laser_points = Group()

        for _ in range(5):
            laser_point = LaserPoint(self.screen_rect)
            self.laser_points.add(laser_point)

        self.start_time = time.time()
        self.duration = 60  # Длительность игры в секундах
        self.missed_apples = 0  # Счетчик пропущенных яблок
        self.background_color = pygame.transform.rotozoom(
            load_image('gm_construct.png'),
            0,
            2.5,
        )

        self.font = pygame.font.Font(None, 36)

        self.completed = False  # пройдена головоломка или нет
        self.died = False  # проиграл он или нет

        # это экраны для смерти и победы
        self.ct = CyberpunkTerminal(self.screen)
        self.ds = DeadScreen(self.screen)

    def update(self):
        if self.died:
            self.ds.display_dead_screen()
        elif self.completed:
            self.ct.display_cyberpunk_screen()
        else:
            keys = pygame.key.get_pressed()
            self.maxwell_cat.update(keys)

            self.laser_points.update()

            collisions = pygame.sprite.spritecollide(self.maxwell_cat, self.laser_points, True)
            for _ in collisions:
                laser_point = LaserPoint(self.screen_rect)
                self.laser_points.add(laser_point)

            elapsed_time = time.time() - self.start_time
            if elapsed_time >= self.duration:
                self.completed = True
                pass

            for laser_point in self.laser_points:
                if laser_point.rect.bottom > self.screen_rect.bottom:
                    self.laser_points.remove(laser_point)
                    for _ in range(3):  # на замену одному потерянному яблоку будет еще 3 новых!
                        laser_point = LaserPoint(self.screen_rect)
                        self.laser_points.add(laser_point)
                    self.missed_apples += 1

            self.draw()

            if self.missed_apples >= 5:
                self.died = True
                pass  # TODO: терминал провален

    def draw(self):
        self.screen.fill((50, 50, 50))
        self.screen.blit(self.background_color, (0, 0))
        self.maxwell_cat.blitme(self.screen)
        self.laser_points.draw(self.screen)

        elapsed_time = time.time() - self.start_time
        remaining_time = max(0, self.duration - elapsed_time)
        minutes, seconds = divmod(int(remaining_time), 60)
        time_text = "{:02}:{:02}".format(minutes, seconds)

        timer_surface = self.font.render(time_text, True, (255, 255, 255))
        self.screen.blit(timer_surface, (10, 10))

        missed_apples_text = "Missed Apples: {}".format(self.missed_apples)
        missed_apples_surface = self.font.render(missed_apples_text, True, (255, 255, 255))
        self.screen.blit(missed_apples_surface, (10, 40))

        pygame.display.flip()

