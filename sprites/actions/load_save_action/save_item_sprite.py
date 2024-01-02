import pygame
from db_class import db
from custom_events import LOAD_GAME


class SaveItemSprite(pygame.sprite.Sprite):
    def __init__(self, screen, item_id, x, y):
        super().__init__()

        self.BLACK = (0, 0, 0)
        self.NEON_COLOR = (57, 255, 20)

        # Set the image and rect attributes for the sprite
        self.image = pygame.Surface((700, 150))
        self.image.fill(self.BLACK)
        self.screen = screen

        # Set the neon-colored border
        pygame.draw.rect(self.image, self.NEON_COLOR, self.image.get_rect(), 5)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Additional attributes for the item
        self.item_id = item_id
        self.load_data()

        # выбрали ли именно это сохранение
        self.selected = False

    def get_item_id(self):
        return self.item_id

    def get_selected(self):
        return self.selected

    def load_data(self):
        # Load data from the database
        item_data = db.get_save_info_by_id(self.item_id)
        if item_data:
            self.id = item_data[0]
            self.time = item_data[1]
            self.level_count = item_data[2]

    def update(self):
        self.draw_info()
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            mouse_buttons = pygame.mouse.get_pressed()
            if mouse_buttons[0]:
                self.selected = True  # если на нас нажали, значит мы выбраны
                pygame.event.post(pygame.event.Event(LOAD_GAME))  # отправляем событие о загрузке сохранения

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(self.rect.centerx + x, self.rect.centery + y))
        self.screen.blit(text_surface, text_rect)

    def draw_info(self):
        # Draw ID, time, and rooms_passed text on the sprite
        self.draw_text(f"ID: {self.id}", 30, self.NEON_COLOR, 0, -40)
        self.draw_text(f"Last time played: {self.time}", 30, self.NEON_COLOR, 0, -15)
        self.draw_text(f"Current level: {self.level_count}", 30, self.NEON_COLOR, 0, 10)
