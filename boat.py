import pygame

from pygame.sprite import Sprite


class SpaceBoat(Sprite):

    def __init__(self, screen):
        super(SpaceBoat, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/spaceships/common_spaceship.png')
        self.image = pygame.transform.scale(self.image, (50, 70))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.move_right = False
        self.move_left = False

    def output(self):
        self.screen.blit(self.image, self.rect)

    def move(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += 4.3
        if self.move_left and self.rect.left > self.screen_rect.left:
            self.center -= 4.3

        self.rect.centerx = self.center

    def create_gun(self):
        self.center = self.screen_rect.centerx
