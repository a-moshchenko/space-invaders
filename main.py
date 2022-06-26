import pygame
from pygame.sprite import Group

from config import settings
from config.enums import Color
from boat import SpaceBoat
from handlers import events, update, update_bullets, create_army, update_targets
from game_stats import Stats
from scores import Scores


def run():
    pygame.init()
    fps_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((settings.WINDOW_HEIGHT, settings.WINDOW_WIDTH))
    pygame.display.set_caption('HELLO')
    bg_color = Color.BLACK.value
    gun = SpaceBoat(screen)
    targets = Group()
    bullets = Group()
    create_army(screen, targets)
    stats = Stats()
    scores = Scores(screen, stats)
    explosion_group = Group()
    # images = [f'images/boom{i}.png' for i in range(1, 5)]
    images = [f'images/ex{i}.png' for i in range(1, 25)]

    while True:
        events(screen, gun, bullets)
        if stats.run_game:
            gun.move()
            bullets.update()
            targets.update()
            update(bg_color, screen, stats, scores, gun, targets, bullets, explosion_group)
            pygame.display.update()
            fps_clock.tick(settings.FPS)
            update_bullets(bullets, stats, scores, targets, screen, explosion_group, images)
            update_targets(stats, screen, scores, gun, targets, bullets)


if __name__ == '__main__':
    run()
