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
                    char.draw(win, (reg_in.x, reg_in.y), side)

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
                utils.handleRegClick(char_selected, pos, side_regs, n, side)

        redrawWindow(win, game, n, side)

main()