import pygame
from pygame.sprite import Sprite

from main.settings import Setting


class Bullet(Sprite):
    """ A class to manage bullets fired form the ship"""

    def __init__(self, ai_game):
        """ Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen

        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet
        self.y -= settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, settings.bullet_color, self.rect)


settings = Setting()
