import pygame
import random

from brick import Brick


class field:

    def __init__(self, screen:pygame.display, type:str, tilesize:int, randomnessBricks:float, tiles):
        self.s = screen
        self.y = type.lower() #accepted types (case independent) are : normal, big, small, U
        self.f = []
        self.size_of_field = pygame.Vector2()
        self.t = tilesize
        self.r = randomnessBricks
        self.tiles = tiles
        self.generateSelf()


    def updateSize(self):
        self.size_of_field.x = len(self.f[0])
        self.size_of_field.y = len(self.f)
    
    def transformMap(self, map):
        map_to_send = map
        for x in range(len(map)):
            for y in range(len(map[0])):
                if map[x][y] == "b":
                    map_to_send[x][y] = Brick(self.t, (y, x), self.s)
        return map_to_send

    def updateCells(self, tiles):
        self.tiles = tiles
        self.generateSelf()

    def generateSelf(self):
        self.f = self.tiles
        self.updateSize()

    def draw(self):	
        wall = pygame.image.load(r"sprites\wallblock.jpg").convert()
        scale = self.t
        wall = pygame.transform.scale(wall, (scale, scale))
        for x in range(len(self.f)):
            for y in range(len(self.f[0])):
                if self.f[x][y] == "w":
                    self.s.blit(wall, pygame.Vector2(y*self.t, self.t*x))
                if type(self.f[x][y]) == Brick:
                    self.f[x][y].draw()

    def field(self):
        return self.f


