# Structure
import pygame
from settings import Settings as sts
from ship import Ship
from background import Background
import game_functions as gf
from pygame.sprite import Group


def run_game():

    # Initialize game and create a screen object
    pygame.init()

    # Initialize the object Settings.
    ai_settings = sts()

    # Set Display size and Caption
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.screen_title)

    # Make a ship
    ship = Ship(screen, ai_settings)
    # Make a group to store the bullets in
    bullets = Group()
    # Build the background
    background = Background(screen)

    # Start the main loop of the game
    while True:

        # Check any events from mouse to keyboard
        gf.check_events(ai_settings, screen, ship, bullets)
        # Moves the ship
        ship.update()
        bullets.update()
        # Update screen with all images files
        gf.update_screen(ai_settings, screen, background, ship, bullets)


run_game()


