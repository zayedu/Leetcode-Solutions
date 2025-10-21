class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        running_sum = 0
        sums = defaultdict(int)

        count = 0
        sums[0] = 1
        for num in nums:
            running_sum += num

            if running_sum-k in sums:
                count+=sums[running_sum-k]

            sums[running_sum] += 1

        return count