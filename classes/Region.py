import pygame
from utils.regionsData import get_regions
pygame.font.init()

class Region:
    def __init__(self, name, skill, player, position, limit):
        self.x = 0
        self.y = 0
        self.width = 180
        self.height = 100
        self.color = (170, 170, 255)
        self.position = position
        self.name = name
        self.skill = skill
        self.numOfFig = 0
        self.region_state = get_regions(player)[self.name]
        self.selected = False
        self.limit = limit
        self.population = 0
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
        elif self.position == 7:
            self.x = 700 / 2 - self.width * 2
            self.y = 500
        elif self.position == 8:
            self.x = 700 / 2 - self.width
            self.y = 500
        elif self.position == 9:
            self.x = 700 / 2
            self.y = 500
        elif self.position == 10:
            self.x = 700 / 2 + self.width
            self.y = 500
        elif self.position == 16:
            self.x = 700 / 2 - self.width / 2
            self.y = 200
        elif self.position == 15:
            self.x = 700 / 2 - self.width
            self.y = 300
        elif self.position == 14:
            self.x = 700 / 2
            self.y = 300
        elif self.position == 13:
            self.x = 700 / 2 - self.width * 1.5
            self.y = 400
        elif self.position == 12:
            self.x = 700 / 2 - self.width / 2
            self.y = 400
        elif self.position == 11:
            self.x = 700 / 2 + self.width / 2
            self.y = 400
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
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        border = (0, 0, 0) if not self.selected else (0, 255, 0)
        pygame.draw.rect(win, border, (self.x, self.y, self.width, self.height), 3)
        font = pygame.font.SysFont("cosmicsans", 40)
        text = font.render(self.name, 1, (0, 0, 0))
        win.blit(text, (self.x + round(self.width / 2) - round(text.get_width() / 2),
                        self.y + round(self.height / 2) - round(text.get_height() / 2)))

    def update_regions(self, player):
        pass