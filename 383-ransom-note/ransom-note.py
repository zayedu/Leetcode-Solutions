class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        '''
        ransomNote subset magazine
        '''

        magazine_chars = { }

        '''
        magazine_chars should look like:
        char -> instances
        '''

        for char in magazine:
            if char not in magazine_chars:
                magazine_chars[char] = 1
            else:
                magazine_chars[char] += 1


        #search through ransom note and decrement the character we want to use 

        for char in ransomNote:
            if char not in magazine_chars:
                return False

            else:
                magazine_chars[char] -= 1

        return min(magazine_chars.values()) >= 0