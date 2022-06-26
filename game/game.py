import sys

import pygame

from config.config import settings
from config.enums import Color
from handlers import CheckEvents
from models.space_ships import CommonShip
from models.target import Target


class Game:
    NAME = 'Space Invaders'

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(self.NAME)
        self.fps_clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((settings.WINDOW_HEIGHT, settings.WINDOW_WIDTH))
        self.bg_color = Color.BLACK.value
        self.spaceship = self.get_spaceship()
        self.target = Target(self.screen)
        self.event_checker = CheckEvents(self.screen, self.spaceship)

    def start(self):
        while True:
            if self.spaceship.hp < 0:
                sys.exit()
            self.spaceship.move()
            self.screen.fill(self.bg_color)
            self.event_checker.start()
            self.fps_clock.tick(settings.FPS)

            pygame.display.update()

    def get_spaceship(self):
        return CommonShip(self.screen)


