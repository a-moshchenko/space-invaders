import random

import pygame


class Target(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Target, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/targets/target.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.distance = 0
        self.vector = random.choice([1, -1])
        self.speed = .2

    def draw(self):
        self.dribbling()
        self.screen.blit(self.image, self.rect)

    def dribbling(self):
        self.x += self.vector
        self.distance += self.vector
        if self.distance >= 25:
            self.vector *= -1
            self.distance = 0
        if self.distance <= -25:
            self.vector *= -1
            self.distance = 0
        self.rect.x = self.x

    def update(self):
        self.y += self.speed
        self.rect.y = self.y



