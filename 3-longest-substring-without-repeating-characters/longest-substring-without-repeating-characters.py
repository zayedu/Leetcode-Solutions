class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        seen = { }
        '''
        seen should look like:
        char -> last occured index
        '''
        l = 0
        max_len = 0

        
        for r in range(len(s)):
            if s[r] not in seen:
                seen[s[r]] = r
            else:
                ###Pre conddition: we have a substring with a repeated character


                while l <= seen[s[r]]:
                    
                    l += 1
                seen[s[r]] = r
            ###Post Condition: Substring from l -> r does not have a repeated character

            max_len = max(max_len,r - l + 1)

        return max_len