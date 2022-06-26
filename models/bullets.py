import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, spaceship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = (255, 255, 255)
        self.speed = 6
        self.power = 2
        self.rect.centerx = spaceship.rect.centerx
        self.rect.top = spaceship.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y
        if self.rect.bottom <= 0:
            self.kill()
        pygame.draw.rect(self.screen, self.color, self.rect)

