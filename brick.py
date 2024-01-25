import pygame
import random


class Brick:

    def __init__(self, tilesize:int, position:tuple, screen):
        self.s = screen
        self.i = pygame.image.load(r"sprites\brickblock.webp").convert()
        self.i = pygame.transform.scale(self.i, (tilesize, tilesize))
        self.t = tilesize
        self.x = position[0]
        self.y = position[1]
    
    def draw(self):
        self.s.blit(self.i, pygame.Vector2(self.y*self.t, self.t*self.x))