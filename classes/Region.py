import pygame
pygame.font.init()

class Region:
    def __init__(self, name, skill, position, height, limit, top_to, next_to, bottom_to, side):
        self.x = 0
        self.y = 0
        self.width = 180
        self.height = height
        self.color = (170, 170, 255)
        self.orgColor = (170, 170, 255)
        self.position = position
        self.name = name
        self.skill = skill
        self.numOfFig = 0
        self.selected = False
        self.available = False
        self.limit = limit
        self.population = 0
        self.chars = []
        self.side = side
        self.calculate_position()
        self.top_to = top_to
        self.next_to = next_to
        self.bottom_to = bottom_to

    def calculate_position(self):
        def_h = 90
        start_h = 140 if self.side == 0 else 120
        m_h = 60
        if self.position == 1:
            self.x = 700 / 2 - self.width / 2
            self.y = self.y = 200 + start_h + def_h * 4 + m_h
        elif self.position == 2:
            self.x = 700 / 2 - self.width
            self.y = self.y = 200 + start_h + def_h * 3 + m_h
        elif self.position == 3:
            self.x = 700 / 2
            self.y = self.y = 200 + start_h + def_h * 3 + m_h
        elif self.position == 4:
            self.x = 700 / 2 - self.width * 1.5
            self.y = self.y = 200 + start_h + def_h * 2 + m_h
        elif self.position == 5:
            self.x = 700 / 2 - self.width / 2
            self.y = self.y = 200 + start_h + def_h * 2 + m_h
        elif self.position == 6:
            self.x = 700 / 2 + self.width / 2
            self.y = self.y = 200 + start_h + def_h * 2 + m_h
        elif self.position == 7:
            self.x = 700 / 2 - self.width * 2
            self.y = self.y = 200 + start_h + def_h * 2
        elif self.position == 8:
            self.x = 700 / 2 - self.width
            self.y = self.y = 200 + start_h + def_h * 2
        elif self.position == 9:
            self.x = 700 / 2
            self.y = self.y = 200 + start_h + def_h * 2
        elif self.position == 10:
            self.x = 700 / 2 + self.width
            self.y = self.y = 200 + start_h + def_h * 2
        elif self.position == 16:
            self.x = 700 / 2 - self.width / 2
            self.y = 200
        elif self.position == 15:
            self.x = 700 / 2 - self.width
            self.y = 200 + start_h
        elif self.position == 14:
            self.x = 700 / 2
            self.y = 200 + start_h
        elif self.position == 13:
            self.x = 700 / 2 - self.width * 1.5
            self.y = self.y = 200 + start_h + def_h
        elif self.position == 12:
            self.x = 700 / 2 - self.width / 2
            self.y = self.y = 200 + start_h + def_h
        elif self.position == 11:
            self.x = 700 / 2 + self.width / 2
            self.y = self.y = 200 + start_h + def_h
        else:
            self.x = 0
            self.y = 0


    def clicked(self, pos):
        mouseX = pos[0]
        mouseY = pos[1]
        print('ttt')

        if self.x <= mouseX <= (self.x + self.width) and self.y <= mouseY <= (self.y + self.height):
            self.selected = True
            return True
        else:
            self.selected = False
            return False

    def draw(self, win):
        if self.selected or self.available:
            rect_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

            semi_transparent_color = (*self.color, 255 * 0.2)  # RGB + Alpha (255 * 0.8 = 204 for 80%)
            rect_surface.fill(semi_transparent_color)

            win.blit(rect_surface, (self.x, self.y))

        # border_color = (0, 0, 0)  # Replace with another color if needed
        # pygame.draw.rect(win, border_color, (self.x, self.y, self.width, self.height), 1)

        # font = pygame.font.SysFont("cosmicsans", 20)
        # text = font.render(self.name, True, (0, 0, 0))  # Text is opaque (fully visible)
        # win.blit(text, (
        #     self.x + round(self.width / 2) - round(text.get_width() / 2),
        #     self.y + round(self.height / 2) - round(text.get_height() / 2)
        # ))

    def update_regions(self, player):
        pass