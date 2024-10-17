class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        
        """
        Sliding window:
        while we have a 

        """
        max_profit = 0

        l = 0
        r = 1
        while r < len(nums):
            if nums[r] > nums[l]:
                max_profit = max(max_profit,nums[r]-nums[l])

            else:
                l = r

            r += 1
        return max_profit