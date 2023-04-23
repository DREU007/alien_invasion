import random

import pygame.sprite


class Boost:
    """Drop a booster for a ship"""


    def __init__(self, ai_game):
        """Initialize attributes"""
        self.screen = ai_game.screen
        self.aliens = ai_game.aliens
        self.ship = ai_game.ship
        self.bullets = ai_game.bullets
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.active_boost = False  # Active Flag

        # Create a booster drop
        self.rect = pygame.Rect(0, 0, self.settings.booster_width,
                                self.settings.booster_height)
        self.x = float(self.rect.x)

        self.boost_list = [
            self.wide_bullet(), self.stronger_bullet(), self.explosion()]

    def draw_booster(self):
        """Draw a bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        """Move boost drop"""
        self.x += self.settings.booster_fall_speed
        self.rect.x = self.x
        catch_boost = pygame.sprite.groupcollide(
            self.ship, self.rect, False, True)
        if catch_boost:
            self.active_boost = True


    def boost_off(self):
        self.settings.bullet_width = 3

        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

    def wide_bullet(self):
        self.settings.bullet_width = 100

    def stronger_bullet(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, False, True)

    def explosion(self):
        for bullet in self.bullets:
            explode_aliens = pygame.sprite.spritecollide(bullet, self.aliens, True, True)
            # if explode_aliens:

