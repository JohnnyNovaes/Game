import pygame as pyg


class Ship:

    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the image and get it's rect
        self.image = pyg.image.load('images/Ship.png')

        # Get rect from image and screen
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Start each new ship at the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):

        """Draw the ship at its current location"""
        rotate_image = pyg.transform.rotate(self.image, 90)
        self.screen.blit(rotate_image, self.rect)

