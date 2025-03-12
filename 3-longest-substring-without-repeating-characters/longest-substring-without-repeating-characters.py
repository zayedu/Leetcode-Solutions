class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {

        }

        '''
        seen should look like:
        
            char -> last_idx
        '''
        
        longest = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in seen:
                seen[s[r]] = r
            else:
                while l <= seen[s[r]]:                    
                    l+=1
                seen[s[r]] = r
            longest = max(r - l + 1, longest)
        return longest