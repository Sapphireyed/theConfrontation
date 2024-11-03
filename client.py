import pygame
from classes.Board import Board
from network import Network
from classes.Figurine import Figurine
from classes.Region import Region
from utils.regionsData import get_regions
from classes.Button import Button

pygame.init()

width = 900
height = 900
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Confrontation")

start = Button('Start game', (200, 200, 250))


def redrawWindow(win, game, player, regions):
    win.fill((0, 168, 168))

    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", 1, (255,0,0), True)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        board = Board()
        board.draw(win)

        for r in regions:
            if r.name in game.regions_state:
                r.selected = game.regions_state[r.name]['selected']
            r.draw(win)

        if game.turn == 0:
            f1 = Figurine('frodo', '', (750, 50))
            f1.draw(win)
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
            run = False
            print("Couldn't get game", e)
            break

        regions_data = get_regions(game.players[player]['side'])
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

                for r in regions:
                    r.selected = False
                    #n.send(f'update,RSELECTED,{r.name},false')
                    if r.clicked(pos):
                        r.selected = True
                        #n.send(f'update,RSELECTED,{r.name},true')

        redrawWindow(win, game, player, regions)

main()