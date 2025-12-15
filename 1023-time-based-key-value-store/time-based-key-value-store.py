from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.times = defaultdict(list)
        self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[(key,timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        times = self.times[key]

        low,high = 0, len(times)

        while low < high:

            mid = (low+high)//2

            if times[mid] <= timestamp:
                low = mid + 1

            else:
                high = mid

        if low == 0:
            return ""
        
        return self.values[(key,times[low-1])]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)