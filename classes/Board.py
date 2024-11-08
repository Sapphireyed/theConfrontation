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
        # pygame.draw.rect(win, self.color, (0, 0, self.width, self.height))
        self.drawBg(win, side)
        self.drawOverlay(win)
        self.drawMainBoard(win, side)

    def drawOverlay(self, win):
        overlay = pygame.Surface((900, 900))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(50)
        win.blit(overlay, (0, 0))

    def drawBg(self, win, side):
        bg = pygame.image.load('assets/lotr-bg-rivendel.jpg') if side == 0 else pygame.image.load('assets/lotr-bg-mordor.png')
        bg = pygame.transform.scale(bg, (bg.get_width() * 0.9, bg.get_height() * 0.9))
        cords = (-200, 0) if side == 0 else (-530, 0)
        win.blit(bg, cords)

    def drawMainBoard(self, win, side):
        image = pygame.image.load('assets/board-no-bg.png')
        image = pygame.transform.scale(image, (700, 700))
        if side == 1:
            image = pygame.transform.rotate(image, 180)
        win.blit(image, (0, 170))