from tilematch_tools.model import Scoring

class CCScore(Scoring):
    def __init__(self):
            super().__init__()

    def award_for_match(self, match):
        self._points += match.value

