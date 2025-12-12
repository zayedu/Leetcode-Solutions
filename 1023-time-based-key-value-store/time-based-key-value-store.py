class TimeMap:

    def __init__(self):
        self.key_time = defaultdict(list)
        self.kt_val = defaultdict(str)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_time[key].append(timestamp)
        self.kt_val[(key,timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        #get time
        times = self.key_time[key]

        low, high = 0, len(times)

        while low < high:
            mid = (low+high)//2

            if times[mid] <= timestamp:
                low = mid + 1

            else:
                high = mid
        if low == 0:
            return ""
        time = times[low-1]
        return self.kt_val[(key,time)]
    


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)