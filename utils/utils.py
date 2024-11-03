import pygame

def waitForPlayer(win, width, height):
    font = pygame.font.SysFont("comicsans", 80)
    text = font.render("Waiting for Player...", 1, (255, 0, 0), True)
    win.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))

def drawBoard(win, Board, regions, game):
    board = Board()
    board.draw(win)

    for r in regions:
        if r.name in game.regions_state:
            r.selected = game.regions_state[r.name]['selected']
        r.draw(win)