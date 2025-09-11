class Leaderboard:

    def __init__(self):
        # playerId -> total score
        self.scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        # O(1)
        self.scores[playerId] = self.scores.get(playerId, 0) + score

    def top(self, K: int) -> int:
        # O(n log n) by sorting values
        sorted_scores = sorted(self.scores.values(), reverse=True)
        return sum(sorted_scores[:K])

    def reset(self, playerId: int) -> None:
        # O(1)
        if playerId in self.scores:
            del self.scores[playerId]
