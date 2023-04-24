import os
import json


class GameStats:
    """Track statistics for Alien Invasion"""
    _score_fp = os.path.join(os.path.dirname(__file__), 'high_score.json')

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an active state
        self.game_active = False

        # High score should never be reset
        try:
            self.load_high_score()
        except FileNotFoundError:
            self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """Load high_score.json as high_score"""
        self.filename = self._score_fp
        with open(self.filename, 'r') as f:
            self.high_score = json.load(f)

    def save_high_score(self):
        """Save high_score as high_score.json"""
        self.filename = self._score_fp
        with open(self.filename, 'w') as f:
            json.dump(self.high_score, f)
