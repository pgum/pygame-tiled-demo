from deck import Deck
import pygame
from world import World
from map import Level
from tokenize import String

#Sprit sheet class to load sprites from player spritesheet
class SpriteSheet(object):
    def __init__(self, fileName: String):
        self.sheet = pygame.image.load(fileName)

    def image_at(self, rectangle):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size, pygame.SRCALPHA, 32).convert_alpha()
        image.blit(self.sheet, (0, 0), rect)
        return image

class Sprite(object):
    #Draw sprite
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y, self.x+16, self.y+16))
        
    def __init__(self,x,y,fileName):
        self.x=x
        self.y=y
        self.sprites = SpriteSheet("resources/"+fileName)
    
        self.stillLeft = self.sprites.image_at((0, 42, 30, 42))
        self.stillRight = self.sprites.image_at((0, 51, 16, 66))
        self.stillUp = self.sprites.image_at((0, 17, 16, 32))
        self.stillDown = self.sprites.image_at((0, 0, 16, 16))
        self.image=self.stillDown
    
    def update(self, context):
        pass