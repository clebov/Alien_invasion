""" creat an empty pygame window by creating a class to represent the game"""

import sys
import pygame


class AlienInvasion:
    """Overall class to mange game assets and behavior."""

    def __init__(self):
        """initialize the game, and create game resources."""
        pygame.init()
        # create the game screen with the size of 1200x800 then assign it to an attribute to call
        # throughout the program
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Aliean Invasion")

        # Set the background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # if the exit button on screen is clicked close the program
                    sys.exit()

            # redraw the screen during each pass throught the loop
            self.screen.fill(self.bg_color)

            # make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    # make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
