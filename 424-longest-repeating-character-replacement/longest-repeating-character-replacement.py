class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        char_in_window_freq = {

        }

        l = 0
        running_max = 0
        longest = 0
        for r in range(len(s)):

            if s[r] in char_in_window_freq:
                char_in_window_freq[s[r]] +=1
            else:
                char_in_window_freq[s[r]] = 1

            running_max = max(char_in_window_freq.values())

            while running_max < (r-l+1) - k:
                char_in_window_freq[s[l]] -= 1
                l += 1
                running_max = max(char_in_window_freq.values())

            

            longest = max(longest,r-l+1)

        return longest

        '''
        s = "AABABBA", k = 1
                  ^
               ^
        longest = 4
        r_max = 3
        char_in_window_freq = {
            A : 1,
            B : 3,
        }

        '''