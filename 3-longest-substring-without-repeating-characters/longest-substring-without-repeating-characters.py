class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {

        }
        # char -> last time it appeared

        longest = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in char_map:
                char_map[s[r]] = r

            else:
                while l <= char_map[s[r]]:
                    l += 1
                char_map[s[r]] = r

            longest = max(longest,r-l+1)

        return longest
                    