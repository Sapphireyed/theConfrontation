import socket
from _thread import *
import pickle

from pygame.display import update

from game import Game

server = "192.168.0.192"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0

def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))
    reply = ""

    while True:
        try:
            raw_data = conn.recv(4096)
            try:
                data = raw_data.decode()
                if gameId in games:
                    game = games[gameId]

                    if not data:
                        break
                    elif data.startswith('next_turn'):
                        print('next turn')
                        cmd, player = data.split(',')
                        game.next_turn(int(player))
                        print('turn: ', game.turn)
                        conn.sendall(pickle.dumps(game))
                    else:
                        conn.sendall(pickle.dumps(game))
                else:
                    break
            # if data comes as object or smth else not string
            except UnicodeDecodeError:
                try:
                    if gameId in games:
                        game = games[gameId]
                        data = pickle.loads(raw_data)

                        if data['msg'] == 'init_regions':
                            game.init_regions(data['regions'], data['side'])
                        elif data['msg'] == 'char_update':
                            char = data['char']
                            game.update_chars(char)
                        elif data['msg'] == 'reg_update':
                            reg = data['reg']
                            game.update_regions(reg, data['side'])
                        conn.sendall(pickle.dumps(game))

                except pickle.UnpicklingError:
                    print("Failed to unpickle data: data might be corrupted or not a valid pickled object.")
                except AttributeError as e:
                    print(f"Attribute error: {e}. Make sure the object has the correct attributes.")

            except Exception as e:
                print('no raw data', e)
        except Exception as e:
            print(e)

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1


    start_new_thread(threaded_client, (conn, p, gameId))