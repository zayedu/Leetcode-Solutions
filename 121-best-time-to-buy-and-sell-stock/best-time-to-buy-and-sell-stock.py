class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        l = 0 
        max_profit = 0

        for r in range(len(nums)):

            max_profit = max(max_profit, nums[r]-nums[l])

            if nums[r] < nums[l]:
                l = r


        return max_profit