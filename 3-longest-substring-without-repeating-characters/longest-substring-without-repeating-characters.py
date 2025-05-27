class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len,running_len = 0,0

        positions = {

        }

        '''
        positions should looks like: {
            char -> idx
        }
        '''

        l = 0

        for r in range(len(s)):
            if s[r] not in positions:
                positions[s[r]] = r

            else:
                while l <= positions[s[r]]:
                    l += 1
                    running_len -= 1

                positions[s[r]] = r
            running_len +=1
            max_len = max(max_len,running_len)

        return max_len