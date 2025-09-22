from collections import deque
class HitCounter:

    def __init__(self):
        self.queue = deque()
        

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        count = 0
        while self.queue and abs(timestamp - self.queue[0]) >= 300:
            self.queue.popleft()
            count +=1

        return len(self.queue)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)