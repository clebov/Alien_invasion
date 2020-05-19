""" creat an empty pygame window by creating a class to represent the game"""

import sys
import pygame


class AlienInvasion:
    """Overall class to mange game assets and behavior."""

    def __init__(self):
        """initilize the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Aliean Invasion")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # whatch for keyboard and ouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    # make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
