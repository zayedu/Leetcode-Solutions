class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        char_count = {

        }

        '''
        char_count is 
            char -> frequency_in_s
        '''

        for char in s:
            if char in char_count:
                char_count[char] += 1

            else:
                char_count[char] = 1

        for char in t:
            if char not in char_count or char_count[char] <= 0:
                return False
            
            char_count[char] -= 1
            
        return all(v==0 for v in char_count.values())