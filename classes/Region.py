import pygame
from utils.regionsData import get_regions
pygame.font.init()

class Region:
    def __init__(self, name, skill, player, position):
        self.x = 0
        self.y = 0
        self.width = 180
        self.height = 100
        self.position = position
        self.name = name
        self.skill = skill
        self.numOfFig = 0
        self.region_state = get_regions(player)[self.name]
        self.selected = False
        self.calculate_position()

    def calculate_position(self):
        if self.position == 1:
            self.x = 700 / 2 - self.width / 2
            self.y = 800
        elif self.position == 2:
            self.x = 700 / 2 - self.width
            self.y = 700
        elif self.position == 3:
            self.x = 700 / 2
            self.y = 700
        elif self.position == 4:
            self.x = 700 / 2 - self.width * 1.5
            self.y = 600
        elif self.position == 5:
            self.x = 700 / 2 - self.width / 2
            self.y = 600
        elif self.position == 6:
            self.x = 700 / 2 + self.width / 2
            self.y = 600
        else:
            self.x = 0
            self.y = 0


    def clicked(self, pos):
        mouseX = pos[0]
        mouseY = pos[1]

        if self.x <= mouseX <= (self.x + self.width) and self.y <= mouseY <= (self.y + self.height):
            self.selected = True
            return True
        else:
            self.selected = False
            return False

    def draw(self, win):
        pygame.draw.rect(win, (170, 170, 255), (self.x, self.y, self.width, self.height))
        border = (0, 0, 0) if not self.selected else (0, 255, 0)
        pygame.draw.rect(win, border, (self.x, self.y, self.width, self.height), 3)
        font = pygame.font.SysFont("cosmicsans", 40)
        text = font.render(self.name, 1, (0, 0, 0))
        win.blit(text, (self.x + round(self.width / 2) - round(text.get_width() / 2),
                        self.y + round(self.height / 2) - round(text.get_height() / 2)))

    def update_regions(self, player):
        pass