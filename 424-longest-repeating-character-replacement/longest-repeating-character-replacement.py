class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_in_window = {

        }

        '''
        freq in window should look like:
            char -> occurences in window
        '''

        l = 0
        max_len = 0
        max_occurences = 0
        for r in range(len(s)):
            if s[r] not in freq_in_window:
                freq_in_window[s[r]] = 1

            else:
                freq_in_window[s[r]] += 1

            max_occurences = max(max_occurences,freq_in_window[s[r]])

            while r-l+1 - max_occurences > k:
                freq_in_window[s[l]] -= 1
                l += 1

            max_len = max(max_len,r-l+1)

        return max_len
    