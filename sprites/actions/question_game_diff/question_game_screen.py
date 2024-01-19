import pygame
from .adds.cyberpunk_terminal import CyberpunkTerminal
from .adds.dead_screen import DeadScreen


class QuestionGame:
    def __init__(self, screen, quest, anw1, anw2, anw3, anw4, true):
        pygame.init()

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.font1 = pygame.font.Font(None, 50)
        self.font = pygame.font.Font(None, 150)

        self.quest = quest
        self.anw1 = anw1
        self.anw2 = anw2
        self.anw3 = anw3
        self.anw4 = anw4
        self.true = true
        self.attempts = 3

        self.input_text = '|'
        self.input_tick = 30

        self.clock = pygame.time.Clock()

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
            if pygame.key.get_pressed()[pygame.K_1]:
                self.input_text = '1'
            if pygame.key.get_pressed()[pygame.K_2]:
                self.input_text = '2'
            if pygame.key.get_pressed()[pygame.K_3]:
                self.input_text = '3'
            if pygame.key.get_pressed()[pygame.K_4]:
                self.input_text = '4'
            if pygame.key.get_pressed()[pygame.K_5]:
                self.input_text = '5'
            if pygame.key.get_pressed()[pygame.K_6]:
                self.input_text = '6'
            if pygame.key.get_pressed()[pygame.K_7]:
                self.input_text = '7'
            if pygame.key.get_pressed()[pygame.K_8]:
                self.input_text = '8'
            if pygame.key.get_pressed()[pygame.K_9]:
                self.input_text = '9'
            if pygame.key.get_pressed()[pygame.K_TAB]:
                if int(self.input_text) == int(self.true):
                    self.completed = True
                else:
                    self.died = True
            self.draw()

    def draw(self):
        self.screen.fill((0, 0, 0))

        text_surface1 = self.font1.render(f'{self.quest}', True, (0, 255, 0))
        self.screen.blit(text_surface1, (30, 40))

        text_surface1 = self.font1.render(f'1.){self.anw1}', True, (0, 255, 0))
        self.screen.blit(text_surface1, (80, 200))

        text_surface1 = self.font1.render(f'2.){self.anw2}', True, (0, 255, 0))
        self.screen.blit(text_surface1, (280, 200))

        text_surface1 = self.font1.render(f'3.){self.anw3}', True, (0, 255, 0))
        self.screen.blit(text_surface1, (480, 200))

        text_surface1 = self.font1.render(f'4.){self.anw4}', True, (0, 255, 0))
        self.screen.blit(text_surface1, (710, 200))

        text_surface1 = self.font1.render(f'В ответ введите только номер правильного ответа', True, (0, 255, 0))
        self.screen.blit(text_surface1, (30, 400))

        text_surface1 = self.font1.render(f'Чтобы проверить ответ нажмите Tab', True, (0, 255, 0))
        self.screen.blit(text_surface1, (30, 500))

        input_rect = pygame.Rect(440, 600, 130, 130)
        pygame.draw.rect(self.screen, (100, 100, 100), input_rect)
        if len(self.input_text):
            text_surface = self.font.render(f'{self.input_text}', True, (0, 220, 0))
            self.screen.blit(text_surface, (475, 615))
        pygame.display.flip()

