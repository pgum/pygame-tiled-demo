from settings import Settings
from map import Level

class World(object):
    def __init__(self, s: Settings):
        self.turn_settings = {
            "current" : 0,
            "startingNumber" : 0,
            "increment" : 1,
        }
        self.s = s
        self.maps = []
        for x in self.s.map_settings["files"]:
            map_path=self.s.map_settings["folder"]+x
            print("Loading map: ",x, " from: ",map_path)
            map_to_add=Level(map_path)
            self.maps.append(map_to_add)
        self.currentMapNumber = self.s.map_settings["startingNumber"]
        self.currentMap = self.maps[self.currentMapNumber]
        print("Current map index: ", self.currentMapNumber)
        print("Current turn: ", self.turn_settings["current"])

    def nextTurn(self):
        self.turn_settings["current"]= self.turn_settings["current"] + self.turn_settings["increment"]
        print("current turn: ",self.turn_settings["current"])
        return self

    def update(self):
        pass
    
