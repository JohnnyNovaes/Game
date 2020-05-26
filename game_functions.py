import sys
import pygame
from bullet import Bullet


# Watch for keyboard and mouse events
def check_events(ai_settings, background, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # If the user press some key this event occurs
        elif event.type == pygame.KEYDOWN:

            check_keydown_events(event, ai_settings, background, ship, bullets)

        # If the user release the key - Right or Left - this event occurs
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, background, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:

        # Move the ship to the right
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:

        # Move the ship to the right
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group
        new_bullet = Bullet(ai_settings, background.image, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, background, ship, bullets):

    # Redraw the screen during each pass through the loop
    #screen.fill(ai_settings.screen_color)

    # Draw background and ship
    background.blitme()
    ship.blitme()

    # Make the most recently draw screen visible
    pygame.display.flip()

    for bullet in bullets.sprites():
        bullet.draw_bullet()


