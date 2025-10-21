class Solution:
    def longestBalanced(self, s: str) -> int:
        
        max_len = 0

        for left in range(len(s)):

            count = defaultdict(int)
            for right in range(left,len(s)):
                count[s[right]] += 1
                if min(count.values()) == max(count.values()):
                    max_len = max(max_len,right-left+1)


        return max_len