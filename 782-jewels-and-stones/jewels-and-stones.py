class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        for i in stones:
            if i in jewels:
                cnt += 1

        return cnt