class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {

        }

        '''
        freq should like:
            char -> freq
        '''

        max_len = 0
        max_freq = 0
        l = 0

        for r in range(len(s)):
            
            if s[r] not in freq:
                freq[s[r]] = 1
            else:
                freq[s[r]] += 1

            max_freq = max(max_freq, freq[s[r]])

            while max_freq + k < (r-l+1) :
                if s[l] in freq:
                    freq[s[l]] -= 1
                l += 1

            max_len = max(max_len,r-l+1)

        return max_len

        """
        s = AABABBA

        """