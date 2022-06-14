import pygame, pytmx
from game import Game
from settings import Settings

def main():
    pygame.init()
    pygame.display.set_caption("Pixel Civilisations Demo")
    settings = Settings()
    screen = pygame.display.set_mode([
        settings.display_settings["screen_width"],
        settings.display_settings["screen_height"]
        ])
    game = Game(settings)
    clock = pygame.time.Clock()
    done = False
    
    while not done:
        done = game.processEvents()
        game.update()
        game.draw(screen)
        clock.tick(settings.time_settings["fps"])
      
    pygame.quit()

if __name__ == "__main__":
    main()