import pygame
import socket

class Player:

    def __init__(self, screen:pygame.display, name:str, color:pygame.color, size:int, speed:int, position:list[int], tilesize:int, clientSocket:socket.socket, IP:list[int]):
        self.s = screen
        self.n = name
        self.c = color
        self.z = size
        self.sp = speed
        self.p = position
        self.valid = []
        self.t = tilesize
        self.socket = clientSocket
        self.updateMap = False
        self.receivedmap = []
        pygame.key.set_repeat(1,10)
        self.ip = IP[0]
        self.port = IP[1]

    def getCurrentTile(self):
        return [(self.p[0]+(self.z/2))//self.t, (self.p[1]+(self.z/2))//self.t]

    def draw(self):
        pygame.draw.rect(self.s, self.c, pygame.Rect(self.p[0], self.p[1], self.z, self.z))

    def setLastValidPosition(self):
        self.valid = self.p

    def checkKeys(self):
        self.updateMap = False
        self.setLastValidPosition()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pygame.key.get_repeat()
                if event.key == pygame.K_z or event.key == pygame.K_UP:
                    self.moveUp()
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.moveDown()
                if (event.key == pygame.K_q or event.key == pygame.K_LEFT):
                    self.moveLeft()
                if (event.key == pygame.K_d or event.key == pygame.K_RIGHT):
                    self.moveRight()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    chaine="space"
                    try:
                        self.socket.connect((self.ip, self.port))
                        self.socket.send(chaine.encode())
                        map = self.socket.recv(5096).decode()
                        self.receivedmap = eval(map)
                        print(self.receivedmap)
                    except:
                        pass
                    self.updateMap = True
                        

    def updateCells(self):
        return [self.updateMap, self.receivedmap]

    def moveUp(self):
        self.p[1] -= self.sp

    def moveDown(self):
        self.p[1] += self.sp

    def moveLeft(self):
        self.p[0] -= self.sp
        
    def moveRight(self):
        self.p[0] += self.sp