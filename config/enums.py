from enum import Enum


class Color(Enum):
    BLACK = (0, 0, 0)


class Images(str, Enum):
    COMMON_SPACESHIP = '../images/spaceships/spaceship22.png'
    COMMON_TARGET = '../images/targets/target.png'
    SPACESHIP_EXPLOSION = f'../images/explosion/ex{{i}}.png'
    TARGET_EXPLOSION = f'../images/explosion/boom{{i}}.png'
    HIT_POINT = '../images/health/life.png'
