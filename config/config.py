from pydantic import BaseConfig


class Setting(BaseConfig):
    FPS: int = 60
    WINDOW_HEIGHT: int = 1500
    WINDOW_WIDTH: int = 800
    DEFAULT_SPACESHIP_SPEED:  int = 4.5
    HIGH_SCORE_FILE = '../config/high_scores.txt'



settings = Setting()
