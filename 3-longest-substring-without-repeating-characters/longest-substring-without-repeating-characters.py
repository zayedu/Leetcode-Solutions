class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = {

        }

        """
        Seen should look like:
        char -> position
        """
        max_val = 0

        l = 0
        for r in range(len(s)):
            if s[r] not in seen:
                seen[s[r]] = r
            
            else:
                while l <= seen[s[r]]:
                    l += 1
                seen[s[r]] = r

            max_val = max(max_val,r-l+1)

        return max_val