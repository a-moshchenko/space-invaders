import pygame
import sys
from bullet import Bullet
from target import Target
import time
from models.explosion import Explosion
from background import back_ground


def events(screen, gun, bullets):
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                sys.exit()
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_d:
                        gun.move_right = True
                    case pygame.K_a:
                        gun.move_left = True
                    case pygame.K_SPACE:
                        new_bullet = Bullet(screen, gun)
                        if len(bullets) < 6:
                            bullets.add(new_bullet)
            case pygame.KEYUP:
                match event.key:
                    case pygame.K_d:
                        gun.move_right = False
                    case pygame.K_a:
                        gun.move_left = False


def update(color, screen, stats, scores, gun, targets, bullets, explosion):
    screen.fill(color)
    screen.blit(back_ground.image, back_ground.rect)
    scores.show_score()
    explosion.draw(screen)
    explosion.update()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for target in targets:
        target.draw()
    gun.output()
    targets.draw(screen)

    pygame.display.flip()


def update_bullets(bullets, stats, scores, targets, screen, explosion, images):
    bullets.update()
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    colisions = pygame.sprite.groupcollide(bullets, targets, True, True)
    if colisions:
        for count in colisions.values():
            stats.score += 10 * len(count)
            exp = Explosion(count[0], images)
            explosion.add(exp)
        scores.image_score()
        update_high_score(stats, scores)
        scores.image_life()
    if len(targets) == 0:
        bullets.empty()
        time.sleep(1)
        create_army(screen, targets)


def update_targets(stats, screen, scores, boat, targets, bullets):
    targets.update()
    if pygame.sprite.spritecollideany(boat, targets):
        # exp = Explosion(boat, images)
        # explosion.add(exp)
        gun_kill(stats, screen, scores, boat, targets, bullets)
    target_check(stats, screen, scores, boat, targets, bullets)


def create_army(screen, targets):
    target = Target(screen)
    width = target.rect.width
    col = int((1000 - 2 * width) / width)
    for i in range(5):
        for target_number in range(col):
            if i % 2 == 0 and target_number % 2 != 0:
                continue
            if i % 2 != 0 and target_number % 2 == 0:
                continue
            target = Target(screen)
            target.x = width + width * target_number
            target.y = width + 40 + width * i
            target.rect.x = target.x
            target.rect.y = target.y
            targets.add(target)


def gun_kill(stats, screen, scores, boat, targets, bullets):
    if stats.boat_lefts > 0:

        pygame.event.pump()
        pygame.display.update()
        stats.boat_lefts -= 1
        pygame.time.wait(2000)
        scores.image_score()
        scores.image_life()
        targets.empty()
        bullets.empty()
        create_army(screen, targets)
        boat.create_gun()
    else:
        stats.run_game = False
        sys.exit()


def target_check(stats, screen, scores, boat, targets, bullets):
    screen_rect = screen.get_rect()
    for target in targets.sprites():
        if target.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, scores, boat, targets, bullets)
            break


def update_high_score(stats, scores):
    if stats.score > stats.high_scores:
        stats.high_scores = stats.score
        scores.image_high_score()
        with open('config/high_scores.txt', 'w') as file:
            file.write(str(stats.high_scores))
