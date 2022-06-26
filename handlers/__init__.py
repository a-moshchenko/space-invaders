import pygame
import sys

from models.explosion import Explosion
from models.target import Target
from config.enums import Images
from models.statistics import Stats
from models.score import Scores
from config.config import settings


class Updater:

    def __init__(self, screen, spaceship):
        self.screen = screen
        self.spaceship = spaceship
        self.bullets = pygame.sprite.Group()
        self.explosion = pygame.sprite.Group()
        self.targets = pygame.sprite.Group()
        self.stats = Stats()
        self.scores = Scores(screen, self.spaceship, self.stats)
        self.spaceship_explosion_images = [Images.SPACESHIP_EXPLOSION.format(i=i) for i in range(1, 25)]
        self.target_explosion_images = [Images.TARGET_EXPLOSION.format(i=i) for i in range(1, 21)]

    def run(self):
        self.scores.update()
        self.check_collision()
        if not self.targets:
            self.create_army()
        print(len(self.targets))
        self.explosion.update()
        self.spaceship.update()
        self.spaceship.bullets.update()

    def update_high_score(self):
        if self.stats.score > self.stats.high_scores:
            self.stats.high_scores = self.stats.score
            self.scores.image_high_score()
            with open(settings.HIGH_SCORE_FILE, 'w') as file:
                file.write(str(self.stats.high_scores))

    def check_collision(self):
        if collisions := pygame.sprite.groupcollide(self.spaceship.bullets, self.targets, True, False):
            for bullet, targets in collisions.items():
                for target in targets:
                    target.hp -= bullet.power
                    if target.hp <= 0:
                        target.kill()
                        self.stats.score += 10
                        exp = Explosion(self.screen, target, self.target_explosion_images, 1)
                        self.explosion.add(exp)
        self.targets.update()
        for target in self.targets.sprites():
            if target.rect.bottom >= self.screen.get_rect().bottom:
                exp = Explosion(self.screen, self.spaceship, self.spaceship_explosion_images, 1)
                self.spaceship.hp -= 1
                self.explosion.add(exp)
                self.spaceship.create()
                self.targets.empty()
                self.bullets.empty()
                break
        if pygame.sprite.spritecollideany(self.spaceship, self.targets):
            exp = Explosion(self.screen, self.spaceship, self.spaceship_explosion_images, 1)
            self.spaceship.hp -= 1
            self.explosion.add(exp)
            self.spaceship.create()

    def create_army(self):
        target = Target(self.screen)
        width = target.rect.width
        col = int((settings.WINDOW_HEIGHT - 2 * width) / width)
        for i in range(5):
            for target_number in range(col):
                if i % 2 == 0 and target_number % 2 != 0:
                    continue
                if i % 2 != 0 and target_number % 2 == 0:
                    continue
                target = Target(self.screen)
                target.x = width + width * target_number
                target.y = width + 40 + width * i
                target.rect.x = target.x
                target.rect.y = target.y
                self.targets.add(target)


class CheckEvents:
    def __init__(self, screen, spaceship):
        self.screen = screen
        self.spaceship = spaceship
        self.updater = Updater(self.screen, self.spaceship)

    def start(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    sys.exit()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_d:
                            self.spaceship.move_right = True
                        case pygame.K_a:
                            self.spaceship.move_left = True
                        case pygame.K_w:
                            self.spaceship.move_up = True
                        case pygame.K_s:
                            self.spaceship.move_down = True
                        case pygame.K_SPACE:
                            self.spaceship.fire()
                case pygame.KEYUP:
                    match event.key:
                        case pygame.K_d:
                            self.spaceship.move_right = False
                        case pygame.K_a:
                            self.spaceship.move_left = False
                        case pygame.K_w:
                            self.spaceship.move_up = False
                        case pygame.K_s:
                            self.spaceship.move_down = False
        self.updater.run()

