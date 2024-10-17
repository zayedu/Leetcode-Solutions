class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_sub = 0
        l = 0
        freq_map = {}
        max_freq = 0

        for r in range(len(s)):
            # Update the frequency of the current character
            if s[r] not in freq_map:
                freq_map[s[r]] = 1
            else:
                freq_map[s[r]] += 1

            # Update the max frequency in the current window
            max_freq = max(max_freq, freq_map[s[r]])

            if (r - l + 1) - max_freq > k:

                freq_map[s[l]] -= 1
                l += 1

            max_sub = max(max_sub, r - l + 1)

        return max_sub
