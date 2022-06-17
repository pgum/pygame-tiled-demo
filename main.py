import pygame, pytmx
from game import Game
from settings import Settings

def main():
    pygame.init()
    pygame.display.set_caption("Pixel Civilisations Demo")
    s = Settings()
    screen = pygame.display.set_mode([
        s.screen_settings["width"],
        s.screen_settings["height"]
        ])
    game = Game(s)
    clock = pygame.time.Clock()
    done = False
    gameMap = pytmx.load_pygame('resources/maps/map.tmx')

    while not done:
        done = game.processEvents()
        game.update()
        pygame.display.update()
        game.draw(screen)
        clock.tick(s.time_settings["fps"])
        
    pygame.quit()

if __name__ == "__main__":
    main()