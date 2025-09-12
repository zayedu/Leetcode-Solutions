class HitCounter:

    def __init__(self):
        self.hit_map = { }


    def hit(self, timestamp: int) -> None:

        if timestamp in self.hit_map:
            self.hit_map[timestamp] += 1
        else:
            self.hit_map[timestamp] = 1


    def getHits(self, period_timestamp: int) -> int:
        
        end_period = max(0,period_timestamp - 300)
        hits = 0
        for timestamp, count in self.hit_map.items():
            if timestamp > end_period and timestamp <= period_timestamp:
                hits += count

        return hits
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)