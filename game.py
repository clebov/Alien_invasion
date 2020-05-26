"""
This is the main game controller class, I kept the name for simplicity.
"""
import pygame
from settings import *
from entities import Ship


class AlienInvasion(object):

    def __init__(self):
        # we don't init pygame here, we do that prior to this being launched, we come into this object presuming
        # that PyGame has been initialized, so first we need the display, since Surfaces don't function until the
        # display is initialized
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # we can initialize our images here, so we can ensure they don't try to load prior to our screen being setup
        self.images = {
            'player': pygame.image.load(os.path.join(IMAGES_PE_DIR, 'playerShip2_blue.png')).convert_alpha(),
            'bullet': pygame.image.load(os.path.join(IMAGES_PE_DIR, 'laserBlue07.png')).convert_alpha(),
            'background': pygame.image.load(os.path.join(IMAGES_BG_DIR, 'Background.png')).convert_alpha()
        }
        # I didn't know what square image was being used for, so I didn't load it

        # we also don't pass around a settings object, it's easier, and a bit clearer to just have a settings module
        # that can be imported wherever, this is just a personal preference really.

        # we don't need to blit the BG here either, nor do we run flip, that only needs to happen when we're ready to
        # draw the screen to the buffer, we can set the caption here, that isn't super important, but I'm going to set
        # it below so I can add a FPS meter to it

        self.player = Ship(self)  # we can initialize the player here, that's perfectly fine
        self.clock = pygame.time.Clock()  # the clock and time delta as before
        self.time_delta = 0.016
        # well use an entity manager here, in this case, just a simple list.  You can use Sprite.Group if you'd prefer
        # I never use Sprites so I always just roll my own.  This list will just contain entities in the world, we'll
        # go ahead and add the player to this.
        self.entities = []
        self.entities.append(self.player)
        # this is the control flag, it'll be used by the game loop, this is for cleaner shutdowns then using sys.exit
        self.running = True
        # these are a couple helpers for our event checks, we have a tuple (immuntable and cheaper on memory) of keys
        self._move_left_keys = (pygame.K_a, pygame.K_LEFT)
        self._move_right_keys = (pygame.K_d, pygame.K_RIGHT)
        # joining two tuples can be done with concatenation
        self.move_keys = self._move_left_keys + self._move_right_keys

    def run_game(self):
        # the game loop will be about the same, with some tweaks to names
        # draw our main bg first
        self.screen.blit(self.images['background'], (0, 0))
        while self.running:
            self.process_events()
            self.handle_logic()
            self.handle_render()
            # update the time-step
            self.time_delta = self.clock.tick(60) / 1000
            # let's set our caption here
            pygame.display.set_caption(f"Alien Invasion - FPS: {int(self.clock.get_fps())} - Entities: {len(self.entities)}")
            # refresh the screen here
            pygame.display.flip()

    def process_events(self):
        for event in pygame.event.get():
            # handle quit events and K_q (key Q)
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_q):
                self.running = False
            # handle movement keys, bundling them into tuples isn't required, but IMO makes it more read-able
            # key-pressed
            if event.type == pygame.KEYDOWN and event.key in self.move_keys:
                if event.key in self._move_left_keys:
                    self.player.move_left = True
                if event.key in self._move_right_keys:
                    self.player.move_right = True
            # handle pewpew
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.player.fire = True
            # key-released
            if event.type == pygame.KEYUP and event.key in self.move_keys:
                if event.key in self._move_left_keys:
                    self.player.move_left = False
                if event.key in self._move_right_keys:
                    self.player.move_right = False
            # handle pewpew
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                self.player.fire = False

    def handle_logic(self):
        dead_entities = []  # handle entities that can go away
        for entity in self.entities:
            entity.update(self.time_delta)
            if not entity.alive:
                dead_entities.append(entity)
        # we handle it like this because you never want to modify a list while you're iterating it
        if dead_entities:
            for entity in dead_entities:
                self.entities.remove(entity)

    def handle_render(self):
        # There's some issues with how this is being done, we should have to draw our entity unless it moved, but that's
        # a challenge for another day, this handles clearing their position and rendering them separate, this is in case
        # entities overlap, if we cleared then drew, any entities below (rendered before) would be cleared and we'd get
        # some weird looking images.
        # walk the entities, clear their last position
        for entity in self.entities:
            self.screen.blit(self.images['background'], entity.last_position, entity.last_position)
        # walk them one more time, this time drawing the entities
        for entity in self.entities:
            self.screen.blit(entity.image, entity.rect)