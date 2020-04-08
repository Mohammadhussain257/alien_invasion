import pygame
from pygame.sprite import Sprite
import os
from main.settings import Setting


class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its react attribute
        filePath = os.path.dirname(__file__)
        self.image = pygame.image.load(os.path.join(filePath, "..\\images\\alien.bmp"))
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """ Move the alien to the right"""
        self.x += setting.alien_speed
        self.rect.x = self.x


setting = Setting()
