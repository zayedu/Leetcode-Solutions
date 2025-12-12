from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timestamps = defaultdict(list)
        self.values = defaultdict(str)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append(timestamp)
        self.values[(key,timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:

        times = self.timestamps[key]

        low, high = 0, len(times)
        # left bisect, find first time >= timestamp

        while low < high:
            mid = (low+high)//2

            if times[mid] <= timestamp:
                low = mid +1
            else:
                high = mid

        if low == 0:
            return ""

        time = times[low -1]

        return self.values.get((key,times[low-1]))

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)