def setupTurn(game, side, n, win, start):
    y = 10
    for f, char in game.chars.items():
        if char.side == side:
            if char.x == 0 and char.y == 0:
                char.x = 750
                char.y = y
                n.send({'msg': 'char_update', 'char': char})
            char.draw(win, (char.x, char.y), side)
            y += 80

    start.draw(win)