import pygame
pygame.font.init()

class Figurine:
    def __init__(self, name, skill, strength, side):
        self.x = 0
        self.y = 0
        self.width = 60
        self.height = 40
        self.name = name
        self.skill = skill
        self.side = side
        self.strength = strength
        self.selected = False

    def change_position(self, position):
        self.x, self.y = position

    def draw(self, win, position):
        self.x = position[0]
        self.y = position[1]
        pygame.draw.rect(win, (170, 170, 255), (self.x, self.y, self.width, self.height))
        border = (0, 0, 0) if not self.selected else (0, 255, 0)
        pygame.draw.rect(win, border, (self.x, self.y, self.width, self.height), 3)
        font = pygame.font.SysFont("cosmicsans", 40)
        text = font.render(self.name + '  ' + str(self.strength), 1, (0, 0, 0))
        win.blit(text, (self.x + round(self.width / 2) - round(text.get_width() / 2),
                         self.y + round(self.height / 2) - round(text.get_height() / 2)))

    def clicked(self, pos):
        print(self.x)
        mouseX = pos[0]
        mouseY = pos[1]
        if self.x <= mouseX <= (self.x + self.width) and self.y <= mouseY <= (self.y + self.height):
            self.selected = True
            return True
        else:
            self.selected = False
            return False