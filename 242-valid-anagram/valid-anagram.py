class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_freq = {

        }

        '''
        char_freq should looks like:
            char - > freq
        '''
        
        for char in s:
            if char in char_freq:
                char_freq[char] += 1

            else:
                char_freq[char] =1

        
        for char in t:
            if char not in char_freq or char_freq[char] <= 0:
                return False

            char_freq[char] -= 1

        return min(char_freq.values()) == 0 and max(char_freq.values()) == 0 