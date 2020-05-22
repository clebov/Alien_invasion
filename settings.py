import pygame


class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the games's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bg_img = pygame.image.load("images/background/black_2.png")
        self.bg_color = (230, 230, 230)
