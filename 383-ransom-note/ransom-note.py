class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        available_chars = {

        }

        for char in magazine:
            if char not in available_chars:
                available_chars[char] = 1
            else:
                available_chars[char] += 1

        for char in ransomNote:
            if char not in available_chars:
                return False
            
            available_chars[char] -= 1

            if min(available_chars.values()) < 0:
                return False

        return True

