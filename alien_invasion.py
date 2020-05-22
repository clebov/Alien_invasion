""" create an empty pygame window by creating a class to represent the game"""
import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to mange game assets and behavior."""

    def __init__(self):
        """initialize the game, and create game resources."""
        pygame.init()

        # create the game screen with the size of 1200x800 from settings.py then assign it to an attribute to call
        # throughout the program
        self.settings = Settings()
        # draw the background image
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        # redraw the screen during each pass thought the loop and Set the background color from settings.py.
        self.screen.blit(self.settings.bg_img, (0, 0))
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # if the exit button on screen is clicked close the program
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # if right arrow is pressed move right.
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # if left arrow is pressed move left
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        # draw the ship

        self.ship.blitme()
        # make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
