
def is_active_player(game, side):
    return game.turn % 2 == 0 and side == 0 or game.turn % 2 != 0 and side == 1

def isLegalMove(prev_reg, r, game, player):
    return prev_reg and r.name in prev_reg.top_to and both_ready and game.players[player]['moveCount'] < 1 and game.turn > 0

def both_ready(game):
    return game.players[0]['ready'] and game.players[1]['ready']