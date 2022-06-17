import pygame
from player import Player
from settings import Settings
from world import World

class Game(object):
    def __init__(self, s: Settings):
        self.s = s
        self.world = World(s)
        self.players = []
        
    def processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("This could be go back in turn")
                    pass
                if event.key == pygame.K_UP:
                    print("This suppose to be create player event from Key UP")
                    self.players.append(Player(12,13,self.world,"PlayerCharacter.png"))
                elif event.key == pygame.K_RIGHT:
                    print("This is key event key RIGHT")
                    self.world.nextTurn()
        return False
        
    def update(self):
        for p in self.players: p.update()
        self.world.update()
    
    def nextTurn(self):
        for p in self.players: p.nextTurn()
        self.world.nextTurn()
    
    def draw(self, screen):
        BACKGROUND = (40, 40, 40)
        screen.fill(BACKGROUND)
        self.world.currentMap.draw(screen)
        for p in self.players: p.draw(screen)
        pygame.display.flip()
     