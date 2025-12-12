class Solution:

    def __init__(self, w: List[int]):
        self.range = -1

        self.ranges = []
        self.w = w
        for weight in w:
            self.range+= weight
            self.ranges.append(self.range)

    def pickIndex(self) -> int:
        random_index = random.randint(0,self.range)

        low, high = 0, len(self.ranges)
        #left bisect, find first val >= target
        while low < high:

            mid = (high+low)//2

            if self.ranges[mid] < random_index:
                low = mid+1
            else:
                high = mid

        
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()