from tokenize import String
import pygame, pytmx

class Level(object):
    def __init__(self, fileName: String):
        print("Map is being created with filename", fileName)
        #Create map object from PyTMX
        self.mapObject = pytmx.load_pygame(fileName)
        print("Level debug1: ",self.mapObject)
        #Create list of layers for map
        self.layers = []
        layers_count=len(self.mapObject.layers)
        
        #Amount of level shift left/right
        self.levelShift = 0

        print("Map dimentions: ",self.mapObject.width, self.mapObject.height, " number of layers: ", layers_count)
        
    #Update layer
    def draw(self, screen):
        pass
        for layer in self.layers:
            layer.draw(screen)
            
class Layer(object):
    def __init__(self, index, mapObject):
        print("* Layer index #",index)
        #Layer index from tiled map
        self.index = index

    #Draw layer
    def draw(self, screen):
        pass

#Tile class with an image, x and y
class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pass
