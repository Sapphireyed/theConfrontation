import random
from utils.charsData import chars
from classes.Figurine import Figurine

sides = [0, 1]
sideP1 = random.choice(sides)
sideP2 = sides[0] if sideP1 == 1 else sides[1]

class Game:
    def __init__(self, id):
        self.id = id
        self.ready = False
        self.turn = 0
        self.regions = {
            0: [],
            1: []
        }
        self.players = {
            0: {
                'side': sideP1
            },
            1: {
                'side': sideP2
            }
        }
        self.chars = {
            char_info['name']: Figurine(char_info['name'], char_info['skill'], char_info['strength'], char_info['side'])
            for char_info in chars[0] + chars[1]
        }

    def connected(self):
        return self.ready

    def init_regions(self, regions, side):
        self.regions[side] = regions

    def next_turn(self):
        self.turn += 1

    def update_chars(self, char):
        name = char.name
        self.chars[name].x = int(char.x)
        self.chars[name].y = int(char.y)
        self.chars[name].selected = char.selected
        self.chars[name].region = char.region

    def update_player(self):
        pass

    def update_regions(self, reg, side):
        for i, r in enumerate(self.regions[side]):
            if r.name == reg.name:
                self.regions[side][i].x = reg.x
                self.regions[side][i].y = reg.y
                self.regions[side][i].selected = reg.selected
                break



