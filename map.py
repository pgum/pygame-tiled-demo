from tokenize import String
import pygame, pytmx

class Level(object):
    def __init__(self, fileName: String):
        print("Map is being created with filename", fileName)
        #Create map object from PyTMX
        self.mapObject = pytmx.load_pygame(fileName)
        
        #Create list of layers for map
        self.layers = []
        
        #Amount of level shift left/right
        self.levelShift = 0
        
        #Create layers for each layer in tile map
        for layer in range(len(self.mapObject.layers)):
            self.layers.append(Layer(index = layer, mapObject = self.mapObject))
    
    #Move layer left/right
    def shiftLevel(self, shiftX):
        self.levelShift += shiftX
        
        for layer in self.layers:
            for tile in layer.tiles:
                tile.rect.x += shiftX
    
    #Update layer
    def draw(self, screen):
        for layer in self.layers:
            layer.draw(screen)
            
class Layer(object):
    def __init__(self, index, mapObject):
        #Layer index from tiled map
        self.index = index
        
        #Create gruop of tiles for this layer
        self.tiles = pygame.sprite.Group()
        
        #Reference map object
        self.mapObject = mapObject
        
        #Create tiles in the right position for each layer
        for x in range(self.mapObject.width):
            for y in range(self.mapObject.height):
                img = self.mapObject.get_tile_image(x, y, self.index)
                if img:
                    self.tiles.add(Tile(image = img, x = (x * self.mapObject.tilewidth), y = (y * self.mapObject.tileheight)))

    #Draw layer
    def draw(self, screen):
        self.tiles.draw(screen)

#Tile class with an image, x and y
class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
