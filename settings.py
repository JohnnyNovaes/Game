class Settings:

    # Class save all settings for the game.
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (230, 230, 230)
        self.screen_title = "Alien Invasion"
        # Ship settings
        self.ship_speed_factor = 10.5
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 100, 100, 100
