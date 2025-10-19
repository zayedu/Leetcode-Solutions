class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount+1] *(amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i-coin >=0:
                    change = 1 + dp[i-coin]

                    dp[i] = min(dp[i],change)

        if dp[amount] != amount+1:
            return dp[amount]

        return -1