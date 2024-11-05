import pygame
import random
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
    for reg in game.regions[side]:
        reg.color = reg.orgColor
        n.send({'msg': 'reg_update', 'reg': reg, 'side': side})

    for f, char in side_chars:
        char.selected = False

        if char.clicked(pos):
            char.selected = True
        n.send({'msg': 'char_update', 'char': char})

        highlightAvailableRegions(char, side, game, n)

def handleRegClick(char_selected, pos, side_regs, n, side, game):
    for r in side_regs:
        r.selected = False

        if r.clicked(pos):
            r.selected = True

            if char_selected:
                if (len(r.chars) < r.limit and
                    ((r.name in char_selected[1].starts and not bothReady(game)) or
                     (bothReady(game)))
                ):
                    if len(r.chars) == 0 and r.limit == 2:
                        char_selected[1].x = r.x + r.width / 2 - char_selected[1].width / 2
                        char_selected[1].y = r.y + 10
                    elif len(r.chars) == 1 and r.limit == 2:
                        char_selected[1].x = r.x + r.width / 2 - char_selected[1].width / 2
                        char_selected[1].y = r.y + 50
                    elif len(r.chars) == 0 and r.limit == 4:
                        char_selected[1].x = r.x + 10
                        char_selected[1].y = r.y + 10
                    elif len(r.chars) == 1 and r.limit == 4:
                        char_selected[1].x = r.x + 10
                        char_selected[1].y = r.y + 50
                    elif len(r.chars) == 2 and r.limit == 4:
                        char_selected[1].x = r.x + r.width/2
                        char_selected[1].y = r.y + 10
                    elif len(r.chars) == 3 and r.limit == 4:
                        char_selected[1].x = r.x + r.width/2
                        char_selected[1].y = r.y + 50
                    else:
                        char_selected[1].x = r.x + r.width / 2 - char_selected[1].width / 2
                        char_selected[1].y = r.y + r.height / 2 - char_selected[1].height / 2

                    prev_reg = next((reg for reg in game.regions[side] if reg.name.lower() == char_selected[1].region.lower()), None)

                    if prev_reg:
                        prev_reg.population -= 1
                        prev_reg.chars = [f for f in prev_reg.chars if f.name.lower() != char_selected[1].name.lower()]
                        n.send({'msg': 'reg_update', 'reg': prev_reg, 'side': side})

                    char_selected[1].region = r.name
                    n.send({'msg': 'char_update', 'char': char_selected[1]})
                    r.population += 1
                    r.chars.append(char_selected[1])
                    random.shuffle(r.chars)
                else:
                    r.color = (200, 100, 100)

        n.send({'msg': 'reg_update', 'reg': r, 'side': side})

def highlightAvailableRegions(char, side, game, n):
    if not bothReady(game):
        available_regions = filter(
            lambda reg: reg.name in char.starts and reg.population < reg.limit and char.selected,
            game.regions[side]
        )

        for reg in available_regions:
            reg.color = (100, 255, 100)
            n.send({'msg': 'reg_update', 'reg': reg, 'side': side})