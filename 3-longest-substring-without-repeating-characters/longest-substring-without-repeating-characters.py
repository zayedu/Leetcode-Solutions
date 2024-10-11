class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos = {

        }

        """
        pos should look like:
        char -> position
        """

        l = 0
        max_len = 0
        for r in range(len(s)):
            if s[r] not in pos:
                pos[s[r]] = r
            else:
                while l <= pos[s[r]]:
                    l += 1
                pos[s[r]] = r

            max_len = max(max_len, r-l+1)

        return max_len