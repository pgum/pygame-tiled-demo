from tokenize import String
from deck import Deck
from entity import Entity
import pygame
from world import World

class Player(Entity):
    def __init__(self, x:int,y:int,w: World,sprite_sheet:String):
        Entity.__init__(self,x,y,w,sprite_sheet)
        self.spritesheetFilename=sprite_sheet
        #Players current level, set after object initialized in game constructor
    def nextTurn(self):
        return Player(self.x, self.y, self.w, self.spritesheetFilename)
        
    def update(self):
       pass
