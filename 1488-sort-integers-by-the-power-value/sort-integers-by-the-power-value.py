class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        cache = {}

        def power(num):
            if num in cache:
                return cache[num]

            if num == 1:
                return 0

            if num %2:
                val = 1 + power(3*num+1)

            else:
                val = 1 + power(num/2)
            cache[num] = val
            return val
        
        power_num = defaultdict(list)

        for num in range(lo,hi+1):
            power_num[power(num)].append(num)

        buckets = [[] for _ in range(max(power_num.keys())+1)]

        for power, nums in power_num.items():
            buckets[power] = nums

        count = 0 

        for bucket in buckets:
            if not bucket:
                continue

            if k - count <= len(bucket):
                bucket.sort()
                return bucket[k-count-1]


            count += len(bucket)
