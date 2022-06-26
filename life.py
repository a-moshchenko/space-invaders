import pygame
from pygame.sprite import Sprite

from config.enums import Images


class Life(Sprite):

    def __init__(self, screen):
        super(Life, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(Images.HIT_POINT)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
