class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen_freq = {

        }

        '''
        seen_freq should look like:
            char_in_window -> freq_in_window
        '''

        max_freq = 0
        longest = 0

        l = 0

        for r in range(len(s)):
            if s[r] not in seen_freq:
                seen_freq[s[r]] = 1
            else:
                seen_freq[s[r]] += 1
            max_freq = max(max_freq,seen_freq[s[r]])

            while r - l + 1 > max_freq + k:
                seen_freq[s[l]] -= 1
                l += 1

            longest = max(longest,r-l+1)

        return longest