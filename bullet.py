import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_game):
        """create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/player-enemies/laserBlue07.png')

        # create a bullet rect at (0,0) and then set correct position.
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)
        self._last_draw_rect = self.rect.copy()

    def update(self, time_delta):
        """move the bullet up the screen."""
        # update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed * time_delta
        # update the rect position.
        self._last_draw_rect = self.rect.copy()
        self.rect.y = int(self.y)

    def draw_bullet(self):
        """draw the bullet to the screen"""
        self.screen.blit(self.settings.bg_img, self._last_draw_rect,
                         self._last_draw_rect)
        self.screen.blit(self.image, self.rect)


