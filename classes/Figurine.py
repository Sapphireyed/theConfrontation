import pygame
pygame.font.init()

class Figurine:
    def __init__(self, name, skill, position):
        self.x = 0
        self.y = 0
        self.width = 60
        self.height = 40
        self.name = name
        self.skill = skill
        self.position = position
        self.selected = False

    def draw(self, win):
        self.x = self.position[0]
        self.y = self.position[1]
        pygame.draw.rect(win, (170, 170, 255), (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("cosmicsans", 40)
        text = font.render(self.name, 1, (0, 0, 0))
        win.blit(text, (self.x + round(self.width / 2) - round(text.get_width() / 2),
                         self.y + round(self.height / 2) - round(text.get_height() / 2)))