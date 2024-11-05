import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.192"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def get_p(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            initial_data = self.client.recv(4096*4).decode()
            #print('network data received in connect: ', initial_data)
            return initial_data

        except:
            print('Connection refused')

    def send(self, data):
        try:
            if isinstance(data, str):
                self.client.send(str.encode(data))
            else:
                self.client.send(pickle.dumps(data))

            response = self.client.recv(4096*4)
            decoded_response = pickle.loads(response)
            return decoded_response
        except TypeError as e:
            print("error in sending in network.py: ", e)
        except socket.error as e:
            print("error in sending in network.py, socket error: ", e)