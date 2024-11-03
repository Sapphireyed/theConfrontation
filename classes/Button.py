import pygame
pygame.font.init()

class Button:
    def __init__(self, text, color):
        self.text = text
        self.color = color
        self.width = 150
        self.height = 50
        self.id = "main_button"
        self.x = 725
        self.y = 800

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("cosmicsans", 30)
        text = font.render(self.text, 1, (255, 255, 255))
        win.blit(
            text,
            (
                self.x + self.width / 2 - round(text.get_width()/2),
                self.y + round(text.get_height()/2)
            )
        )

    def click(self, pos):
        mouseX = pos[0]
        mouseY = pos[1]
        if self.x <= mouseX <= (self.x + self.width) and self.y <= mouseY <= (self.y + self.height):
            return True
        else:
            return False


