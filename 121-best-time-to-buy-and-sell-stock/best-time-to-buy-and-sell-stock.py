class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0

        l = 0

        for r in range(len(prices)):
            max_prof = max(max_prof,prices[r]-prices[l])

            if prices[r] < prices[l]:
                l=r

        return max_prof