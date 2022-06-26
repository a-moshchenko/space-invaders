from config.config import settings


class Stats:

    def __init__(self):
        self.reset_stats()
        with open(settings.HIGH_SCORE_FILE, "r") as file:
            self.high_scores = int(file.readline())

    def reset_stats(self):
        self.boat_lefts = 3
        self.score = 0