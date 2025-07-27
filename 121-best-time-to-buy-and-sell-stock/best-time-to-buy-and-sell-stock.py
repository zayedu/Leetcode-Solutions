class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        
        max_profit = 0
        l = 0
        min_price = nums[0]
        for r in range(len(nums)):
            max_profit = max(max_profit, nums[r]-nums[l])

            if nums[r] < min_price:
                l = r
                min_price = nums[l]
        return max_profit


