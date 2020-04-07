import pygame
import sys

from main.settings import Setting
from main.ship import Ship
from main.bullet import Bullet

class AlienInvasion:
    """ Overall Class to manage game assets and behavior """

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        setting.screen_width = self.screen.get_rect().width
        setting.scree_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

    def _check_events(self):
        # watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_events(self, event):
        """Respond ot keypress"""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _check_keyup_event(self, event):
        """Respond to key release"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        # Redraw the screen during each pass through the loop
        self.screen.fill(setting.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Make the most recently drawn screen visible.
        pygame.display.flip()


# creating setting instance
setting = Setting()

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
