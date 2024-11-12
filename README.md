Making a known board game LOTR The Confrontation a digital experience!

Assumptions:
1. Game will have all the same mechanics, rules and logics as the physical version
2. Game will automatically make moves that can be automated (ex. shuffle characters on the same region after every move)
3. Game will not allow illegal moves (ex. player can't move a character to the location that already reach the limit of characters on it)

Current status:
1. Server, networking, clients setup
2. Sides assigned to players randomly (to implement possibility to choose sides)
3. Board built accordingly for each player depending on which side a player plays
4. Setup turn works properly (each player makes initial setup of their characters in legal regions)
# actually limits on starting positions are off, there can be only one character on starting region with exception for Shire(4) and Mordor(4). Needs fixing #
5. Start game done (after both players finish setup all the characters are distributed on the board, opponent's character having hidden names, though)
6. Limits work after game start
7. Moving characters and shuffling characters on given region works
# the x and y coordinates don't update properly after shuffling. Needs fixing #
8. Fight recognized properly. Fight mechanic not implemented
9. Cards initialized and shown on the board, logic not implemented yet.

To be done:
1. Characters unique abilities
2. Fight
3. fixes to movements and limits (point 5 and 7 above)
4. rules for winning / losing

How to run:
1. run **python3 server.py**
2. in another terminal window in the same directory run **python3 client.py** (1st player)
3. in yet another terminal window run **pythin3 client.py** again (2nd players)