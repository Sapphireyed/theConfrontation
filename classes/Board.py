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
        image = pygame.image.load('assets/board.png')
        image = pygame.transform.scale(image, (700, 700))
        if side == 0:
            image = pygame.transform.rotate(image, 180)
        win.blit(image, (0, 190))