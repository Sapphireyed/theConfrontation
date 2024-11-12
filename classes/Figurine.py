import pygame
pygame.font.init()

class Figurine:
    def __init__(self, name, skill, strength, side, turn):
        self.x = 0
        self.y = 0
        self.width = 100
        self.height = 25
        self.name = name
        self.skill = skill
        self.side = side
        self.color = (0,0, 0) if self.side == 1 else (255, 255, 255)
        self.strength = strength
        self.selected = False
        self.region = 'None'
        self.clickable = True if turn == 0 or (self.side == 0 and turn % 2 == 0) or (self.side == 1 and turn % 2 != 0) else False
        self.starts = ['shire', 'good1', 'good2', 'good3', 'good4', 'good5'] \
            if self.side == 0 \
            else ['mordor', 'evil1', 'evil2', 'evil3', 'evil4', 'evil5']


    def change_position(self, position):
        self.x, self.y = position

    def draw(self, win, position, side):
        self.x = position[0]
        self.y = position[1]
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        border = (0, 255, 0) if self.selected and side == self.side else (0, 0, 0)
        pygame.draw.rect(win, border, (self.x, self.y, self.width, self.height), 3)

        if side == self.side:
            font = pygame.font.SysFont("cosmicsans", 22)
            text_color = (0, 0, 0) if self.side == 0 else (255, 255, 255)
            text = font.render(self.name + '  ' + str(self.strength), 1, text_color)
            win.blit(text, (self.x + round(self.width / 2) - round(text.get_width() / 2),
                             self.y + round(self.height / 2) - round(text.get_height() / 2)))

    def clicked(self, pos):
        mouseX = pos[0]
        mouseY = pos[1]
        if self.x <= mouseX <= (self.x + self.width) and self.y <= mouseY <= (self.y + self.height):
            self.selected = True
            return True
        else:
            self.selected = False
            return False