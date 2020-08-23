""" create an empty pygame window by creating a class to represent the game"""
import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to mange game assets and behavior."""

    def __init__(self):
        """initialize the game, and create game resources."""
        pygame.init()

        # create the game screen with the size of 1200x800 from settings.py then assign it to an attribute to call
        # throughout the program
        self.settings = Settings()

        # set the screen to the default size player can change by pressing 1 or 2
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen.blit(self.settings.bg_img, (0, 0))
        pygame.display.flip()
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        self.clock = pygame.time.Clock()  # <- add the clock here, we need it in our controller
        self.time_delta = 0.016  # 60/1000  # preset the time delta, you can use 0.016 as a starting value as
        # it's the result for 60fp

        # store live bullets fired
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()



    def run_game(self):
        """Start the main loop for the game"""
        # redraw the screen during each pass thought the loop and Set the background color from settings.py.

        while True:
            self._check_events()
            self.ship.update(self.time_delta)
            self.bullets.update(self.time_delta)
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # if the exit button on screen is clicked close the program
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        # draw the ship
        self.ship.blitme()
        self.aliens.draw(self.screen)
        # make the most recently drawn screen visible.
        pygame.display.flip()
        # bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    def _check_keydown_events(self, event):
        # if right arrow or D is pressed move right.
        if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
            self.ship.moving_right = True
        # if left arrow or A is pressed move left
        elif (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        # if q is pressed quit
        elif event.key == pygame.K_q:
            sys.exit()
        # if 1 is pressed enter full screen
        elif event.key == pygame.K_1:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
            self.screen.blit(self.settings.bg_img, (0, 0))
        # if 2 is pressed return game screen to original size
        elif event.key == pygame.K_2:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
            self.screen.blit(self.settings.bg_img, (0, 0))

    def _check_keyup_events(self, event):
        if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
            self.ship.moving_right = False
        elif (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """update position of bullets and get rid of old bullets."""
        # Update bullet positions.

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """create thefleet of aliens."""
        # make an alien
        alien = Alien(self)
        self.aliens.add(alien)


if __name__ == '__main__':
    # make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
