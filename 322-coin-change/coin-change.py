class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')]*(amount+1)

        dp[0] = 0

        for index in range(len(dp)):
            for coin in coins:
                if index - coin >= 0:
                    dp[index] = min(dp[index],1+dp[index-coin]) 


        return dp[amount] if dp[amount] != float('inf') else -1
