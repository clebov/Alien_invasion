import pygame
from settings import Settings


class Ship:
    """A class to mange the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = Settings()
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/player-enemies/playerShip2_blue.png')
        self.rect = self.image.get_rect()
        self.ship_speed = 20

        # create a flag to check if there is movement
        self.moving_right = False
        self.moving_left = False

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        self.abs_x = float(self.rect.x)  # <- we set an absolute X position here
        self._last_draw_rect = self.rect.copy()  # <- we set the copy for logging our last draw position here

    def update(self, time_delta):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.abs_x += self.ship_speed * time_delta
        if self.moving_left and self.rect.left > 0:
            self.abs_x -= self.ship_speed * time_delta
        self._last_draw_rect = self.rect.copy()  # <- IMPORTANT: before we update it make a copy of it for this frame
        self.rect.x = int(self.abs_x)  # <- update the rect X with the absolute position converted to an int here

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.settings.bg_img, self._last_draw_rect,
                         self._last_draw_rect)  # <- we use the draw rect rather than the rect
        self.screen.blit(self.image, self.rect)  # but not here, we use rect for the ship, not the background
