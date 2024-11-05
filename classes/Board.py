import pygame

class Board:
    rect = (113, 113, 525, 525)

    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 700
        self.height = 900
        self.color = (128, 128, 128)

    def draw(self, win, side):
        pygame.draw.rect(win, self.color, (0, 0, self.width, self.height))