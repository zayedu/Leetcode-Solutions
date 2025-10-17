import heapq
class Leaderboard:

    def __init__(self):
        self.leaderboard = defaultdict(int) 
        """
        player_id -> player_total_score
        """

    def addScore(self, playerId: int, score: int) -> None:        
        self.leaderboard[playerId] += score

    
    def top(self, k: int) -> int:
        heap = [-score for score in self.leaderboard.values()]

        heapq.heapify(heap)
        top_k  = 0

        for _ in range(k):
            top_k -= heapq.heappop(heap)

        return top_k

    def reset(self, playerId: int) -> None:

        self.leaderboard[playerId] = 0

        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)