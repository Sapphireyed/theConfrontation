import pygame

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