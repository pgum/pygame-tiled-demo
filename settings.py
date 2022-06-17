class Settings(object):
    def __init__(self):
        self.screen_settings = {
            "width" : 1680,
            "height" : 1050
        }
        self.time_settings = {
            "fps" : 100
        }
        self.map_settings = {
            "startingNumber" : 0,
            "folder" : "resources/maps/",
            "files" : [ "map.tmx" ]
        }
        
    def update(self):
        pass
