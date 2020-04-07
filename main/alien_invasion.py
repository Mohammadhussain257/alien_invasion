import pygame
import sys

from main.settings import Setting
from main.ship import Ship


class AlienInvasion:
    """ Overall Class to manage game assets and behavior """

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        # watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # Redraw the screen during each pass through the loop
        self.screen.fill(setting.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

# creating setting instance
setting = Setting()

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
