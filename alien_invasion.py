import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import logging


class AlienInvasion(object):
    def __init__(self):
        self.init_display_and_font()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien invasion')
        self.ship = Ship(self)
        self.alien = Alien(self)
        self.logger_setting()

    # the logger settings
    def logger_setting(self):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fn = logging.FileHandler('logging.log')
        fn.setFormatter(formatter)
        logger.addHandler(fn)
        self.logger = logging.getLogger('alien_invasion')

    def init_display_and_font(self):
        """the method for lower usage CPU"""
        if not pygame.display.get_init():
            pygame.display.init()
        if not pygame.font.get_init():
            pygame.font.init()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.logger.info('go to right')
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.logger.info('go to left')
            self.ship.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.alien.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
