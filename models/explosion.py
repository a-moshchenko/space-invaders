import pygame
import pygame.image


class Explosion(pygame.sprite.Sprite):

    def __init__(self, screen, target, images, animation_speed):
        super(Explosion, self).__init__()
        self._images = []
        self.screen = screen
        for image in images:
            img = pygame.image.load(image)
            img = pygame.transform.scale(img, (100, 100))
            self._images.append(img)
        self.index = 0
        self.image = self._images[self.index]
        self.rect = self.image.get_rect()
        self.rect.centerx = target.rect.centerx
        self.rect.top = target.rect.top
        self.counter = 0
        self.animation_speed = animation_speed

    def update(self):
        self.counter += 1

        if self.counter >= self.animation_speed and self.index < len(self._images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self._images[self.index]
            self.screen.blit(self.image, self.rect)

        if self.index >= len(self._images) - 1 and self.counter >= self.animation_speed:
            self.kill()

