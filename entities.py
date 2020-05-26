class Entity(object):

    def __init__(self, game_ref):
        self.game = game_ref

    def update(self, dt):
        raise NotImplemented


class Ship(Entity):

    def __init__(self, game_ref):
        super().__init__(game_ref)
        self.image_key = 'player'
        self.rect = self.image.get_rect().copy()  # always make a copy when you're going to mess with a rect
        self.speed = 150
        self.move_right = False
        self.move_left = False
        self.fire = False
        self.fire_counter = 0
        self.fire_interval = 0.15  # how fast we can shoot in seconds
        self.abs_x = 0.0
        # now we can position everything
        self.rect.midbottom = self.game.screen.get_rect().midbottom
        self.abs_x = float(self.rect.x)
        # and lastly we make our 'last position' rect
        self.last_position = self.rect.copy()
        # just a flag to note if we're still alive
        self.alive = True

    @property
    def image(self):
        return self.game.images[self.image_key]

    def update(self, dt):
        # this logic can mostly stay the same
        if self.move_right and self.rect.right < self.game.screen.get_rect().right:
            self.abs_x += self.speed * dt
        if self.move_left and self.rect.left > 0:
            self.abs_x -= self.speed * dt
        self.last_position = self.rect.copy()
        self.rect.x = int(self.abs_x)
        # handle pewpew here
        # increment our fire counter, note that there's no need to update the counter if it's past the interval
        # since it will trigger when fire is activated
        if self.fire_counter < self.fire_interval:
            self.fire_counter += dt
        # if 'fire' and the counter is past our interval, we can shoot
        if self.fire and self.fire_counter > self.fire_interval:
            # inject a new bullet into the entities
            self.game.entities.append(Bullet(self.game, self))
            self.fire_counter = 0.0  # reset our counter


class Bullet(Entity):

    def __init__(self, game_ref, parent):
        super().__init__(game_ref)
        self.image_key = 'bullet'
        self.parent = parent  # should be a ship
        self.rect = self.image.get_rect().copy()  # always make a copy when you're going to mess with a rect
        self.speed = 350
        self.abs_y = 0.0
        # we want this to be positioned at the center of the ship and in front, we can adjust this as needed
        self.rect.midbottom = self.parent.rect.midtop
        self.abs_y = float(self.rect.y)
        # and lastly we make our 'last position' rect
        self.last_position = self.rect.copy()
        self.alive = True

    @property
    def image(self):
        return self.game.images[self.image_key]

    def update(self, dt):
        # all we care about right now, is if we've exited the screen
        if self.rect.bottom < 0:
            self.alive = False
        if self.alive:
            self.abs_y -= self.speed * dt
        self.last_position = self.rect.copy()
        self.rect.y = int(self.abs_y)