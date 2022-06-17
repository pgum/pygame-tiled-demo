from deck import Deck
import pygame
from sprite import Sprite
from world import World
from map import Level
from behaviour import StaticActionCostFunction
from tokenize import String


class Entity(pygame.sprite.Sprite):

    def __init__(self,x:int,y:int,w:World,sprite_sheet:String):
        pygame.sprite.Sprite.__init__(self)
        self.w = w
        self.proficiency = {
            "movement": 0,
            "resources": 0,
            "hp": 0,
            "population": 0,
            "deck": 0,
            "budget": 0,
        }
        self.stats = {
            "movement": 0,
            "resources": 100,
            "hp": 68,
            "population": 2,
            "deck": Deck(),
            "budget": 90,           
        }
        self.desires = {
            "wants_to_do": [ "hp", "deck", "budget" ],
            "hates_to_do": ["movement", "resources"],
            "hates_in_others": [ "hp", "budget" ],
            "hails_in_others": [ "population", "resources" ],
        }        
        self.actions = []
        
        self.cost_functions = StaticActionCostFunction()
        self.sprite = Sprite(x,y,sprite_sheet)
       
    def update(self):
        self.sprite.update(self)

    def draw(self, screen):
        self.sprite.draw(screen)
        