class Setting:
    """ A class to stroe all setting for Alien Invasion"""

    def __init__(self):
        """ Initialize the game's settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5

        # bullet setting
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represent right -1 represent left
        self.fleet_direction = 1