import pygame
import socket
from field import field
from player import Player
pygame.init()

class ClientInstance:

    def __init__(self, targetIP:list[int]):
        self.ip = targetIP[0]
        self.port = targetIP[1]
        self.clientID = 0
        self.map = []
        self.field = 0
        self.socket = 0

    def connectToServer(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, self.port))
        chaine = "ask for tiles"
        self.socket.send(chaine.encode())
        self.map = eval(self.socket.recv(5096).decode())

    def updateField(self, field):
        self.map = field

    def setField(self, field):
        self.field = field

    def getFieldSize(self):
        return [len(self.field), len(self.field[0])]

    def getTileSize(self):
        chaine = "ask for tilesize"
        self.socket.send(chaine.encode())
        result = eval(self.socket.recv(5096).decode())
        print(result)
        return result


if __name__ == "__main__":
    client=ClientInstance(["192.168.59.178", 9090])
    client.connectToServer()
    #<----------------CONSTANTS----------------->
    tilesize = client.getTileSize()

    screen = pygame.display.set_mode((15*tilesize, 15*tilesize))
    Field = field(screen,"normal", tilesize, 0.80, client.map)
    client.setField(Field)
    client.updateField(Field.transformMap(client.map))

    screen = pygame.display.set_mode((Field.size_of_field.x*tilesize, Field.size_of_field.y*tilesize))
    clock = pygame.time.Clock()
    pygame.key.set_repeat(1, 100)

    p_client = Player(screen, "Cocci", "purple", tilesize/5*4, 1, [tilesize+10, tilesize+10], tilesize, client.socket, [client.ip, client.port])


    while True:

        #SELF THINGS

        screen.fill("darkgreen")
        if p_client.updateCells()[0]:
            Field.updateCells(p_client.updateCells()[1])
        Field.generateSelf()
        Field.draw()
        p_client.checkKeys()
        p_client.draw()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                
            if event.type == pygame.QUIT:
                pygame.quit()

        #PRINT OTHER GUYS
                

        pygame.display.flip()


    pygame.quit()