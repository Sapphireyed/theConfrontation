import pygame
import random
import utils.ifChecks as ifChecks
from classes.Region import Region
from utils.regionsData import get_regions

# def turn_text(win, text):
#     font = pygame.font.SysFont("comicsans", 40)
#     text = font.render(text, 1, (255, 0, 0), (128, 128, 128))
#     win.blit(text, (700 / 2 - text.get_width() / 2, 20))

def waitForPlayer(win, width, height):
    font = pygame.font.SysFont("comicsans", 80)
    text = font.render("Waiting for Player...", 1, (128, 128, 128), True)
    win.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))

def drawBoard(win, Board, regions, n, side):
    board = Board()
    board.draw(win, side)

    for r in regions:
        r.draw(win)
        if r.x == 0 and r.y == 0:
            n.send({'msg': 'reg_update', 'reg': r, 'side': side})

    # image = pygame.image.load('assets/board.png')
    # image = pygame.transform.scale(image, (750, 800))
    #
    # if side == 0:
    #     image = pygame.transform.rotate(image, 180)
    # win.blit(image, (-20, 150))

def initialize_regions(side, n):
    regions_data = get_regions(side)

    regions = [Region(
        region_info['name'],
        '',
        region_info['position'],
        region_info['limit'],
        region_info['top_to'],
        region_info['next_to'],
        region_info['bottom_to']) for region_name, region_info in regions_data.items()]

    n.send({'msg': 'init_regions', 'regions': regions, 'side': side})

def createOverlay(width, height):
    overlay_surface = pygame.Surface((width, height))
    overlay_color = (50, 50, 50)
    overlay_alpha = 150
    overlay_surface.set_alpha(overlay_alpha)
    overlay_surface.fill(overlay_color)

    return overlay_surface

def drawCards(win, game, player):
    for card in game.players[player]['cards']:
        card.draw(win)
    for card in game.players[player]['enemy_cards']:
        card.draw(win)

def getRegIn(game, side, char):
    reg_in = next((reg for reg in game.regions[side] if reg.name.lower() == char.region.lower()), None)

    if reg_in and not len(reg_in.chars) > 0:
        reg_in_enemy = next(
            (reg for reg in game.regions[0 if side == 1 else 1] if reg.name.lower() == char.region.lower()), None)
        reg_in = next((reg for reg in game.regions[side] if reg.name.lower() == reg_in_enemy.name.lower()), None)
        reg_in.chars = reg_in_enemy.chars

    return reg_in

def coverInactivePlayer(win, game, side, overlay):
    if not ifChecks.is_active_player(game, side):
        win.blit(overlay, (0, 0))

def handleCharClick(game, side, pos, n, player):
    side_chars = filter(lambda char: char[1].side == side, game.chars.items())
    for reg in game.regions[side]:
        reg.color = reg.orgColor
        n.send({'msg': 'reg_update', 'reg': reg, 'side': side})

    for f, char in side_chars:
        char.selected = False

        if char.clicked(pos):
            char.selected = True
        n.send({'msg': 'char_update', 'char': char, 'clicked': True})

        highlightAvailableRegions(char, side, game, n)

def handleRegClick(char_selected, pos, side_regs, n, side, game, player):
    for r in side_regs:
        r.selected = False

        if r.clicked(pos) and game.players[player]['hisTurn']:
            r.selected = True

            if char_selected:
                prev_reg = next(
                    (reg for reg in game.regions[side] if reg.name.lower() == char_selected[1].region.lower()), None)

                if (r.population < r.limit and
                    ((r.name in char_selected[1].starts and not ifChecks.both_ready(game)) or
                     (ifChecks.isLegalMove(prev_reg, r, game, player)))
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

                    if prev_reg:
                        prev_reg.population -= 1
                        prev_reg.chars = [f for f in prev_reg.chars if f.name.lower() != char_selected[1].name.lower()]
                        n.send({'msg': 'reg_update', 'reg': prev_reg, 'side': side})

                    move_chas(char_selected, r, player, n)
                    random.shuffle(r.chars)
                    if game.turn > 0 and (ifChecks.is_active_player(game, side)):
                        n.send(f'next_turn,{player}')
                elif len(r.chars) > 0 and r.chars[0].side != char_selected[1].side and ifChecks.isLegalMove(prev_reg, r, game, player):
                    print('FIGHT')
                    move_chas(char_selected, r, player, n)
                else:
                    r.color = (200, 100, 100)

        n.send({'msg': 'reg_update', 'reg': r, 'side': side})

def handleCardClick(pos, n, game, player):
    for card in game.players[player]['cards']:
        card.selected = False
        if card.clicked(pos):
            card.selected = True

def highlightAvailableRegions(char, side, game, n):
    if not ifChecks.both_ready(game):
        available_regions = filter(
            lambda reg: reg.name in char.starts and reg.population < reg.limit and char.selected,
            game.regions[side]
        )

        for reg in available_regions:
            reg.color = (100, 255, 100)
            n.send({'msg': 'reg_update', 'reg': reg, 'side': side})

def move_chas(char_selected, r, player, n):
    char_selected[1].region = r.name
    n.send({'msg': 'char_update', 'char': char_selected[1]})
    n.send({'msg': 'moves_update', 'player': player})
    r.population += 1
    r.chars.append(char_selected[1])