import pygame as pyg


class Background:

    def __init__(self, screen):

        self.screen = screen

        # Load image and get rect
        self.image = pyg.image.load('images/background.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Match the background with screen center position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        # Put the image in the screen
        self.screen.blit(self.image, self.rect)

