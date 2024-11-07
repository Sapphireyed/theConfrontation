import pygame
from classes.Board import Board
from network import Network
from classes.Button import Button
import utils.utils as utils
from utils.setupTurn import setupTurn
import utils.ifChecks as ifChecks
import utils.calculations as calc

pygame.init()

width = 900
height = 900
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Confrontation")

overlay = utils.createOverlay(width, height)


def redrawWindow(win, game, n, side, start, player):
    global image
    win.fill((0, 168, 168))
    regions = game.regions[side]

    if not(game.connected()):
        utils.waitForPlayer(win, width, height)
    else:
        utils.drawBoard(win, Board, regions, n, side)

        if game.turn == 0:
            setupTurn(game, side, n, win, start)
        else:
            utils.coverInactivePlayer(win, game, side, overlay)
            utils.drawCards(win, game, player)

            for f, char in game.chars.items():
                reg_in = utils.getRegIn(game, side, char)

                if reg_in and len(reg_in.chars) > 0:
                    x, y = calc.get_char_coordinates_init(win, reg_in, char, side)
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
        start = Button('Start game')
    except Exception as e:
        running = False
        print("Couldn't get game", e)
        return

    utils.initialize_regions(side, n)

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

                if start.click(pos) and game.turn == 0:
                    n.send(f'next_turn,{player}')

                utils.handleCharClick(game, side, pos, n, player)
                utils.handleRegClick(char_selected, pos, side_regs, n, side, game, player)
                if ifChecks.both_ready(game):
                    utils.handleCardClick(pos, n, game, side)

        redrawWindow(win, game, n, side, start, player)

main()