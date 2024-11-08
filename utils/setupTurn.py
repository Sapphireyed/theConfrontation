def setupTurn(game, side, n, win, start):
    y = 500
    for f, char in game.chars.items():
        if char.side == side:
            if char.x == 0 and char.y == 0:
                char.x = 750
                char.y = y
                n.send({'msg': 'char_update', 'char': char})
            char.draw(win, (char.x, char.y), side)
            y += 30

    start.draw(win, game, side)