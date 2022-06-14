import pygame, pytmx
from player import Player
from settings import Settings
from world import World
from map import Level

class Game(object):
    def __init__(self, s: Settings):
        #Set up a level to load
        self.settings = s
        self.world = World(s)
        self.players = []
        self.players.append(Player(x = 300, y = 140, w=self.world))
        for p in self.players: p.currentMap = self.world.currentMap
        self.player = self.players[0]
        
    def processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            #Get keyboard input and move player accordingly
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.goLeft()
                elif event.key == pygame.K_RIGHT:
                    self.player.goRight()
                elif event.key == pygame.K_UP:
                    self.player.jump()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and self.player.changeX < 0:
                    self.player.stop()
                elif event.key == pygame.K_RIGHT and self.player.changeX > 0:
                    self.player.stop()
            
        return False
        
    def update(self):
        #Update player movement and collision logic
        for p in self.players: p.update()
        self.world.update()
    
    def draw(self, screen):
        BACKGROUND = (40, 40, 40)
        screen.fill(BACKGROUND)
        self.world.currentMap.draw(screen)
        for p in self.players: p.draw(screen)
        pygame.display.flip()
     