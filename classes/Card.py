import pygame

class Card():
    def __init__(self, side, pos, text, mine):
        self.color = (0, 0, 0) if side == 1 else (255, 255, 255)
        self.pos = pos
        self.side = side
        self.x = 780 if mine else self.calculateX(pos)
        self.y = self.calculateY(pos) if mine else 20 if pos < 3 else 60 if 3 <= pos < 6 else 100
        self.width = 100
        self.height = 30
        self.text = text
        self.selected = False
        self.discarded = False

    def calculateX(self, pos):
        x = 20
        if pos % 3 == 0:
            x = 20
        elif pos % 3 == 1:
            x = 140
        else:
            x = 260

        return x

    def calculateY(self, pos):
        y = 500
        return y if pos == 0 else (y + 40 * pos)

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