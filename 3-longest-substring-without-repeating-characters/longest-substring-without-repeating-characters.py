class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0

        occurence = {

        }

        """
        occurence should look like:
            char -> last_occuring_idx
        """
        l = 0
        for r in range(len(s)):

            if s[r] not in occurence:
                occurence[s[r]] = r
                
            else:
                while l <= occurence[s[r]]:
                    l += 1
                    
                occurence[s[r]] = r
            longest = max(longest, r-l+1)

        return longest


            
