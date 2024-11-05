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
                'side': sideP1,
                'ready': False
            },
            1: {
                'side': sideP2,
                'ready': False
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

    def next_turn(self, player):
        if self.turn == 0:
            self.players[player]['ready'] = True
        if self.players[0]['ready'] and self.players[1]['ready']:
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
            if r and r.name and r.name == reg.name:
                self.regions[side][i] = reg
                break

            val = 0 if side == 1 else 1
            reg_enemy = next((r for r in self.regions[val] if r.name.lower() == reg.name), None )
            reg_enemy.population = reg.population




