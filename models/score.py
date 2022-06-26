import pygame.font

from life import Life
from pygame.sprite import Group


class Scores:

    def __init__(self, screen, spaceship, stats):
        self.screen = screen
        self.stats = stats
        self.screen_rect = screen.get_rect()
        self.spaceship = spaceship
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(None, 36)

    def update_score(self):
        self.score_image = self.font.render(f"SCORE: {self.stats.score}", True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def update_high_score(self):
        self.high_score_image = self.font.render(f"RECORD: {self.stats.high_scores}", True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def update(self):
        self.update_score()
        self.update_high_score()
        self.update_hit_point()
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.lifes.draw(self.screen)

    def update_hit_point(self):
        self.lifes = Group()
        for life_count in range(self.spaceship.hp):
            life = Life(self.screen)
            life.rect.x = 15 + life_count * life.rect.width
            life.rect.y = 20
            self.lifes.add(life)