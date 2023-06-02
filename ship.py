import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set it's starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Loading  ships image and get its rect
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom and center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False

        # Store decimal value for ship's horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Update ship position based on the movement flag"""
        if self.moving_right:
            self.rect.x +=1
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.rect.x -=1

    def blitme(self):
        """Draw the ship at it's current location."""
        self.screen.blit(self.image, self.rect)


    