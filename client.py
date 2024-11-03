import pickle
import pygame
from classes.Board import Board
from network import Network
from classes.Region import Region
from utils.regionsData import get_regions
from classes.Button import Button
import utils.utils as utils

pygame.init()

width = 900
height = 900
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Confrontation")

start = Button('Start game', (200, 200, 250))


def redrawWindow(win, game, regions, n, side):
    win.fill((0, 168, 168))

    if not(game.connected()):
        utils.waitForPlayer(win, width, height)
    else:
        utils.drawBoard(win, Board, regions, game)

        if game.turn == 0:
            y = 10
            for f, char in game.chars.items():
                if char.side == side:
                    if char.x == 0 and char.y == 0:
                        char.x = 750
                        char.y = y
                        n.send(char)
                    print(char.x)
                    char.draw(win, (char.x, char.y))
                    y += 80

            start.draw(win)
        else:
            start.text = 'end turn'
            start.draw(win)

    pygame.display.update()

def main():
    running = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.get_p())
    print("You are player", player)

    while running:
        clock.tick(60)
        try:
            game = n.send("get")
        except Exception as e:
            running = False
            print("Couldn't get game", e)
            break

        side = game.players[player]['side']

        regions_data = get_regions(side)
        regions = [Region(region_info['name'], '', False, player, region_info['position']) for region_name, region_info
                   in regions_data.items()]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if start.click(pos):
                    n.send('next_turn')

                for f, char in game.chars.items():
                    char.selected = False
                    if char.clicked(pos):
                        char.selected = True
                    n.send(char)

                for r in regions:
                    r.selected = False
                    #n.send(f'update,RSELECTED,{r.name},false')
                    if r.clicked(pos):
                        r.selected = True
                        #n.send(f'update,RSELECTED,{r.name},true')

        redrawWindow(win, game, regions, n, side)

main()