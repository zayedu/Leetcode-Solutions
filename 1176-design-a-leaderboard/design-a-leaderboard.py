class Leaderboard:

    def __init__(self):
        self.leaderboard_map = { }

    def addScore(self, playerId: int, score: int) -> None:
          
        if playerId not in self.leaderboard_map:
            self.leaderboard_map[playerId] = score
        
        else:
            self.leaderboard_map[playerId] += score
        

    def top(self, k: int) -> int:
        heap = []
        
        for score in self.leaderboard_map.values():
            if len(heap) < k:
                heapq.heappush(heap,score)
            else:
                if score > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,score)
            
        return sum(heap)
                

    def reset(self, playerId: int) -> None:
        del self.leaderboard_map[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)