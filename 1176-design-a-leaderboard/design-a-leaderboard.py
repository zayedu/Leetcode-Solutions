class Leaderboard:

    def __init__(self):
        self.leaderboard_map = { }

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.leaderboard_map:
            self.leaderboard_map[playerId] = score
        
        else:
            self.leaderboard_map[playerId] += score
        

    def top(self, k: int) -> int:
        items = self.leaderboard_map.items()

        items = list(items)
        items.sort(reverse = True, key=lambda x:x[1])
        print(items)
        top = 0
        for index in range(k):
            top += items[index][1]
        return top

    def reset(self, playerId: int) -> None:
        del self.leaderboard_map[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)