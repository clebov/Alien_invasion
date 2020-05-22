import pygame
from settings import Settings
import time

class Ship:
    """A class to mange the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = Settings()
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/player-enemies/playerShip1_red.png')
        self.rect = self.image.get_rect()

        # create a flag to check if there is movement
        self.moving_right = False
        self.moving_left = False

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        Clock = pygame.time.Clock()
        self.delta = Clock.tick(60) / 1000

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 1 * self.delta
        if self.moving_left:
            self.rect.x -= 1 * self.delta
        self.rect.x = int(self.rect.x)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.settings.bg_img, self.rect, self.rect)  # clear the screen where the ship is
        self.screen.blit(self.image, self.rect)
