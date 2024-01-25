import random
import socket
import pygame
import threading
from brick import Brick
from client import ClientInstance

        



class Server:

    def __init__(self, IP:list[int], nb_players:int, randomFactor:int, tilesize:int):
        self.ip = IP[0]
        self.port = IP[1]
        self.socket = 0
        self.nbp = nb_players
        self.csockets = [0]
        self.r = randomFactor
        self.t = tilesize
        self.caddress = [0]

        self.map = [["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
                    ["w","sp","sp","","","","","","","","","","sp","sp","w"],
                    ["w","sp","w","","w","","w","","w","","w","","w","sp","w"],
                    ["w","","","","","","","","","","","","","","w"],
                    ["w","","w","","w","","w","","w","","w","","w","","w"],
                    ["w","","","","","","","","","","","","","","w"],
                    ["w","","w","","w","","w","","w","","w","","w","","w"],
                    ["w","","","","","","","","","","","","","","w"],
                    ["w","","w","","w","","w","","w","","w","","w","","w"],
                    ["w","","","","","","","","","","","","","","w"],
                    ["w","","w","","w","","w","","w","","w","","w","","w"],
                    ["w","","","","","","","","","","","","","","w"],
                    ["w","sp","w","","w","","w","","w","","w","","w","sp","w"],
                    ["w","sp","sp","","","","","","","","","","sp","sp","w"],
                    ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"]]

        self.replaceBricks()

        self.serverParams = [(len(self.map), len(self.map[0]))]

        self.setupServer()

    def replaceBricks(self):
        for x in range(len(self.map)):
            for y in range(len(self.map[0])):
                if self.map[x][y] != "w" and self.map[x][y] != "sp" and random.random()<= self.r:
                    self.map[x][y] = "b"
                if self.map[x][y] == "sp":
                    self.map[x][y] = ""

    def setupServer(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.ip, self.port))
        self.socket.listen()
        self.csockets[0], self.caddress[0] = self.socket.accept()

        self.mainloop()

    def receiveConnection(self, client_socket, client_address):
        self.csockets.append(client_socket)
        self.caddress.append(client_address)

    def mainloop(self):
        
        while self.nbp > len(self.csockets):
            print(len(self.csockets))
            client_socket, client_address = self.socket.accept()
            threading.Thread(target=self.receiveConnection, args=(client_socket, client_address)).start()
        while True:
            for client in self.csockets:
                sent_data = []
                data = client.recv(2048).decode()
                if data == "ask for tiles":
                    sent_data = self.map
                if data == "ask for tilesize":
                    sent_data = self.t
                else: 
                    data == "['void']"
                client.send(str(sent_data).encode())
                self.socket.listen()


server = Server(["192.168.59.178", 9090], 1, 0.9, 40)

# while True:
#     data = client_socket.recv(1024).decode()
#     if data == "space":
#         tiles[1][5] = "w"
#         client_socket.send(str(tiles).encode())
#     client_socket.send(str(tiles).encode())
#     server_socket.close()
#     server_socket.listen()
#     playLoop()




