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
        self.regions_state = {}
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

    def next_turn(self):
        self.turn += 1

    def update_chars(self, name, x, y, selected):
        self.chars[name].x = int(x)
        self.chars[name].y = int(y)
        self.chars[name].selected = selected
        print(self.chars[name].x)

    def update_player(self):
        pass

    def update_regions_state(self, name, val):
        if isinstance(val, str):
            val = val.lower() == 'true'

        self.regions_state[name] = {
            'selected': val
        }
        print(f'Updated region {name} selected state to: {val}')


