import random
import time
from funcs.load_image import load_image
from ..screen_parent import ScreenParent
from .save_item_sprite import SaveItemSprite
from custom_events import CLOSE_TERMINAL
import pygame
from db_class import db


class LoadSaveScreen(ScreenParent):
    def __init__(self, screen):
        super().__init__(screen)
        self.neon_pink = (255, 0, 255)
        self.neon_light_blue = (0, 255, 255)
        self.width, self.height = 1024, 896
        self.start_time = time.time()
        self.arch_logo = pygame.transform.rotozoom(load_image('arch_logo.png'), 0, 0.5)
        self.arch_logo_rect = self.arch_logo.get_rect(center=(self.width // 2, self.height // 2))

        # get all the saves
        cur_y = 200
        self.saves_group = pygame.sprite.Group()
        for id in db.get_save_ids():
            self.saves_group.add(SaveItemSprite(self.screen, id, 200, cur_y))
            cur_y += 200

    def draw_mixed_lines(self, num_lines=50, line_length=100):
        for _ in range(num_lines):
            x1 = random.randint(0, self.width)
            y1 = random.randint(0, self.height)
            angle = random.uniform(0, 2 * 3.1416)
            x2 = x1 + int(line_length * random.uniform(0.5, 1.5) * pygame.math.Vector2(1, 0).rotate(angle).x)
            y2 = y1 + int(line_length * random.uniform(0.5, 1.5) * pygame.math.Vector2(0, 1).rotate(angle).y)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            pygame.draw.line(self.screen, color, (x1, y1), (x2, y2), 2)

    def draw_terminal(self, neon_pink_enabled, neon_light_blue_enabled):
        self.screen.fill((0, 0, 0))  # Fill screen with black
        pygame.draw.rect(self.screen, (255, 0, 255) if neon_pink_enabled else (0, 0, 0),
                         (0, 0, self.width, 10))  # Top border
        pygame.draw.rect(self.screen, (0, 255, 255) if neon_light_blue_enabled else (0, 0, 0),
                         (0, 10, self.width, 10))  # Bottom border

    def draw_arch_logo(self):
        self.screen.blit(self.arch_logo, self.arch_logo_rect)

    def draw_text_along_lines(self, text, x, y, num_lines=20, line_length=200):
        angle_increment = 2 * 3.1416 / num_lines
        font = pygame.font.Font(None, 36)
        color_phase = time.time() * 0.0005
        for i in range(num_lines):
            angle = i * angle_increment
            x_pos = x + int(line_length * 1.2 * pygame.math.Vector2(1, 0).rotate(angle).x)
            y_pos = y + int(line_length * 1.2 * pygame.math.Vector2(0, 1).rotate(angle).y)

            rotated_text = pygame.transform.rotate(font.render(text, True, self.neon_color(color_phase)),
                                                   -angle * 180 / 3.1416)
            self.screen.blit(rotated_text, rotated_text.get_rect(center=(x_pos, y_pos)))

    def neon_color(self, phase):
        # Convert phase to hue value, and use HSV to RGB conversion
        hue = (phase * 360) % 360
        rgb = self.hsv_to_rgb(hue, 1, 1)
        return pygame.Color(rgb[0], rgb[1], rgb[2])

    def hsv_to_rgb(self, h, s, v):
        if s == 0.0:
            return int(v * 255), int(v * 255), int(v * 255)
        i = int(h * 6.0)
        f = (h * 6.0) - i
        p = v * (1.0 - s)
        q = v * (1.0 - s * f)
        t = v * (1.0 - s * (1.0 - f))
        i = i % 6
        if i == 0:
            return int(v * 255), int(t * 255), int(p * 255)
        elif i == 1:
            return int(q * 255), int(v * 255), int(p * 255)
        elif i == 2:
            return int(p * 255), int(v * 255), int(t * 255)
        elif i == 3:
            return int(p * 255), int(q * 255), int(v * 255)
        elif i == 4:
            return int(t * 255), int(p * 255), int(v * 255)
        elif i == 5:
            return int(v * 255), int(p * 255), int(q * 255)

    def display_text(self, text, x, y, color=(255, 255, 255), font_size=24):
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def get_selected_saves(self):
        for save in self.saves_group.sprites():
            if save.get_selected():
                return save.get_item_id()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(CLOSE_TERMINAL))  # посылаем событие на закрытие
            return

        elapsed_time = time.time() - self.start_time
        if elapsed_time < 5:
            # Draw mixed lines for the first 5 seconds
            self.draw_mixed_lines()
            # Draw the Arch Linux logo
            self.draw_arch_logo()
        elif elapsed_time < 20:
            self.screen.fill((0, 0, 26))
            # Draw the terminal with neon pink and neon light blue borders2
            neon_pink_enabled = (int(elapsed_time) % 2) == 0  # Turn off neon pink every 2 seconds
            neon_light_blue_enabled = (int(elapsed_time) % 3) == 0  # Turn off neon light blue every 3 seconds
            self.draw_terminal(neon_pink_enabled, neon_light_blue_enabled)
            self.draw_text_along_lines("Die nazi", 100, 100, num_lines=20, line_length=0)
            self.display_text("Select the saved game", 300, 100, color=self.neon_pink, font_size=72)

            self.saves_group.draw(self.screen)  # draw all sprites
            self.saves_group.update()
