class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_idx = {

        }

        max_len = 0

        l = 0
        for r in range(len(s)):

            if s[r] not in char_idx:
                char_idx[s[r]] = r

            else:
                while l <= char_idx[s[r]]:
                    l += 1

                char_idx[s[r]] = r

            max_len = max(max_len,r-l+1)

        return max_len