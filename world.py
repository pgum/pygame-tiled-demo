import pygame, pytmx
from settings import Settings
from map import Level

class World(object):
    def __init__(self, s: Settings):
        self.s = s
        self.map_settings = {
            "startMapNumber" : 0,
            "map_files" : [ "level1.tmx" ],
            "map_collision_layer" : 1,
            "tiles" : "tiles.png",
        }
        self.time_settings = {
            "turn" : 0,
            "turn_increment" : 1,
        }
        self.maps = []
        for x in self.map_settings["map_files"]:
            map_resource = "resources/maps/"+x
            self.maps.append(Level(map_resource))
        self.currentMapNumber = self.map_settings["startMapNumber"]
        self.currentMap = self.maps[self.currentMapNumber]
        self.currentTurn = self.time_settings["turn"]
    def nextTurn(self):
        self.time_settings["turn"]= self.time_settings["turn"]+ self.time_settings["turn_increment"]
        
    def update(self):
        pass
