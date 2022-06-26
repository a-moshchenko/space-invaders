class Stats:

    def __init__(self):
        self.reset_stats()
        self.run_game = True
        with open("config/high_scores.txt", "r") as file:
            self.high_scores = int(file.readline())

    def reset_stats(self):
        self.boat_lefts = 3
        self.score = 0
