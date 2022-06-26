import pygame

from config.enums import Images
from config.config import settings
from models.bullets import Bullet


class SpaceShip(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(SpaceShip, self).__init__()
        self.bullets = pygame.sprite.Group()
        self.hp = 3
        self.screen = screen
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        self.speed = settings.DEFAULT_SPACESHIP_SPEED
        self.image = pygame.image.load(Images.COMMON_SPACESHIP)
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

    def move(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.speed
        if self.move_left and self.rect.left > self.screen_rect.left:
            self.center_x -= self.speed
        if self.move_up and self.rect.top >= self.screen_rect.top:
            self.center_y -= self.speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.speed

        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def update(self):
        self.screen.blit(self.image, self.rect)

    def create(self):
        self.center_x = self.screen_rect.centerx
        self.center_y = self.screen_rect.centerx

    def fire(self):
        ...


class CommonShip(SpaceShip):

    def __init__(self, screen):
        super(CommonShip, self).__init__(screen)
        self.name = 'Common Ship'

    def fire(self):
        if len(self.bullets) < 6:
            self.bullets.add(Bullet(self.screen, self))



