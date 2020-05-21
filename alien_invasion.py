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
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        """respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # if the exit button on screen is clicked close the program
                sys.exit()

    def _update_screen(self):
        # redraw the screen during each pass thought the loop and Set the background color from settings.py.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
