import random

from pygame.examples.grid import Player

from utils.charsData import chars
from classes.Figurine import Figurine
from classes.Card import Card
from utils.cardsData import cards

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
                'ready': False,
                'moveCount': 0,
                'cards': self.init_cards(sideP1),
                'hisTurn': True
            },
            1: {
                'side': sideP2,
                'ready': False,
                'moveCount': 0,
                'cards': self.init_cards(sideP2),
                'hisTurn': True
            }
        }
        self.evilP = self.players[0] if sideP1 == 1 else self.players[1]
        self.goodP = self.players[0] if sideP1 == 0 else self.players[1]
        self.chars = {
            char_info['name']: Figurine(char_info['name'], char_info['skill'], char_info['strength'], char_info['side'], self.turn)
            for char_info in chars[0] + chars[1]
        }

    def connected(self):
        return self.ready

    def init_regions(self, regions, side):
        self.regions[side] = regions

    def init_cards(self, side):
        char_cards = []
        for i, card in enumerate(cards[side]):
            card = Card(side, i, card)
            char_cards.append(card)
        return char_cards

    def next_turn(self, player):
        if self.turn == 0:
            self.players[player]['ready'] = True
        if self.players[0]['ready'] and self.players[1]['ready']:
            self.turn += 1

            if self.turn > 0  and self.turn % 2 == 0:
                self.goodP['moveCount'] = 0
                self.goodP['hisTurn'] = True
                self.evilP['hisTurn'] = False
            elif self.turn > 0  and self.turn % 2 != 0:
                self.evilP['moveCount'] = 0
                self.goodP['hisTurn'] = False
                self.evilP['hisTurn'] = True

    def update_chars(self, char):
        if char.clickable:
            name = char.name
            self.chars[name].x = int(char.x)
            self.chars[name].y = int(char.y)
            self.chars[name].selected = char.selected
            self.chars[name].region = char.region

    def update_player_moves(self, player):
        if self.turn > 0:
            self.players[player]['moveCount'] = 1

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

