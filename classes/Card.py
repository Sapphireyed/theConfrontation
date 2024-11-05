import pygame

class Card():
    def __init__(self, side, pos, text):
        self.color = (0, 0, 0) if side == 1 else (255, 255, 255)
        self.pos = pos
        self.x = 780
        self.y = self.calculateY(pos)
        self.side = side
        self.width = 100
        self.height = 30
        self.text = text
        self.discarded = False

    def calculateY(self, pos):
        y = 0
        if pos == 0:
            y = 200
        elif pos == 1:
            y = 240
        elif pos == 2:
            y = 280
        elif pos == 3:
            y = 320
        elif pos == 4:
            y = 360
        elif pos == 5:
            y = 400
        elif pos == 6:
            y = 440
        elif pos == 7:
            y = 480
        elif pos == 8:
            y = 520
        elif pos == 9:
            y = 560

        return y

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        if self.selected:
            border = (0, 255, 0)
            pygame.draw.rect(win, border, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("cosmicsans", 26)
        text_color = (0, 0, 0) if self.side == 0 else (255, 255, 255)
        text = font.render(str(self.text), 1, text_color)
        win.blit(
            text,
            (
                self.x + self.width / 2 - round(text.get_width() / 2),
                self.y + self.height / 2 - round(text.get_height() / 2)
            )
        )

    def clicked(self, pos):
        mouseX = pos[0]
        mouseY = pos[1]

        if self.x <= mouseX <= (self.x + self.width) and self.y <= mouseY <= (self.y + self.height):
            self.selected = True
            return True
        else:
            self.selected = False
            return False