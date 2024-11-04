import pygame
from classes.Region import Region
from utils.regionsData import get_regions

def waitForPlayer(win, width, height):
    font = pygame.font.SysFont("comicsans", 80)
    text = font.render("Waiting for Player...", 1, (255, 0, 0), True)
    win.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))

def drawBoard(win, Board, regions, n, side):
    board = Board()
    board.draw(win)

    for r in regions:
        r.draw(win)
        if r.x == 0 and r.y == 0:
            n.send({'msg': 'reg_update', 'reg': r, 'side': side})

def initialize_regions(side, player, n):
    regions_data = get_regions(side)
    regions = [Region(region_info['name'], '', player, region_info['position'], region_info['limit']) for region_name, region_info in regions_data.items()]

    n.send({'msg': 'init_regions', 'regions': regions, 'side': side})

def bothReady(game):
    return game.players[0]['ready'] and game.players[1]['ready']

def handleCharClick(game, side, pos, n):
    side_chars = filter(lambda char: char[1].side == side, game.chars.items())

    for f, char in side_chars:
        char.selected = False
        if char.clicked(pos):
            char.selected = True
        n.send({'msg': 'char_update', 'char': char})
    char_selected = next(filter(lambda char: char[1].selected, game.chars.items()), None)
    print(char_selected)

def handleRegClick(char_selected, pos, side_regs, n, side):
    for r in side_regs:
        r.selected = False

        if r.clicked(pos):
            r.selected = True
            print(char_selected)

            if char_selected:
                if r.population < r.limit:
                    char_selected[1].x = r.x + r.width / 2 - char_selected[1].width / 2
                    char_selected[1].y = r.y + r.height / 2 - char_selected[1].height / 2
                    char_selected[1].region = r.name
                    n.send({'msg': 'char_update', 'char': char_selected[1]})
                    r.population += 1
                else:
                    r.color = (200, 0, 0, 0.2)

        n.send({'msg': 'reg_update', 'reg': r, 'side': side})