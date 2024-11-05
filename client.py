import pygame
from classes.Board import Board
from network import Network
from classes.Button import Button
import utils.utils as utils
from utils.setupTurn import setupTurn

pygame.init()

width = 900
height = 900
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Confrontation")
image = pygame.image.load('assets/board.png')

start = Button('Start game', (200, 200, 250))


def redrawWindow(win, game, n, side):
    win.fill((0, 168, 168))
    regions = game.regions[side]

    if not(game.connected()):
        utils.waitForPlayer(win, width, height)
    else:
        utils.drawBoard(win, Board, regions, n, side)

        if game.turn == 0:
            setupTurn(game, side, n, win, start)
        else:
            start.text = 'end turn'
            start.draw(win)
            if utils.bothReady(game):
                for f, char in game.chars.items():
                    reg_in = next((reg for reg in game.regions[side] if reg.name.lower() == char.region.lower()), None)

                    if not len(reg_in.chars) > 0:
                        reg_in_enemy = next((reg for reg in game.regions[0 if side == 1 else 1] if reg.name.lower() == char.region.lower()), None)
                        reg_in = next((reg for reg in game.regions[side] if reg.name.lower() == reg_in_enemy.name.lower()), None)
                        reg_in.chars = reg_in_enemy.chars

                    if len(reg_in.chars) > 0:
                        if reg_in.limit == 2:
                            x = reg_in.x + reg_in.width/2 - char.width/2
                            y = reg_in.y + 10 if reg_in.chars[0].name.lower() == char.name.lower() else reg_in.y + 50
                            char.draw(win, (x, y), side)
                        elif reg_in.limit == 4:
                            x, y = 0, 0
                            if char.name.lower() == reg_in.chars[0].name.lower():
                                x = reg_in.x + 10
                                y = reg_in.y + 10
                            elif char.name.lower() == reg_in.chars[1].name.lower():
                                x = reg_in.x + 10
                                y = reg_in.y + 40
                            elif char.name.lower() == reg_in.chars[2].name.lower():
                                x = reg_in.x + reg_in.width/2
                                y = reg_in.y + 10
                            elif char.name.lower() == reg_in.chars[3].name.lower():
                                x = reg_in.x  + reg_in.width/2
                                y = reg_in.y + 40
                        else:
                            x = reg_in.x + reg_in.width / 2 - char.width / 2
                            y = reg_in.y + reg_in.height / 2 - char.height / 2

                        char.draw(win, (x, y), side)


    pygame.display.update()

def main():
    running = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.get_p())
    print("You are player", player)

    try:
        game = n.send("get")
        side = game.players[player]['side']

    except Exception as e:
        running = False
        print("Couldn't get game", e)
        return

    utils.initialize_regions(side, player, n)

    while running:
        clock.tick(60)
        try:
            game = n.send("get")
            side = game.players[player]['side']
        except Exception as e:
            running = False
            print("Couldn't get game", e)
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                char_selected = next(filter(lambda char: char[1].selected, game.chars.items()), None)
                side_regs = game.regions[side]

                if start.click(pos):
                    n.send(f'next_turn,{player}')

                utils.handleCharClick(game, side, pos, n)
                utils.handleRegClick(char_selected, pos, side_regs, n, side, game)

        redrawWindow(win, game, n, side)

main()