from multiprocessing.resource_tracker import register

from utils.regionsData import get_regions

class Game:
    def __init__(self, id):
        self.id = id
        self.ready = False
        self.turn = 0
        self.regions_state = {}

    def connected(self):
        return self.ready

    def update_regions_state(self, name, val):
        if isinstance(val, str):
            val = val.lower() == 'true'

        self.regions_state[name] = {
            'selected': val
        }
        print(f'Updated region {name} selected state to: {val}')


