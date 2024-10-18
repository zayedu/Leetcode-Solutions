class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        chars = {

        }

        """
        chars should look like:
        char - > freq
        """

        for char in s:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1

        for char in t:
            if char not in chars:
                return False
            else:
                chars[char] -= 1

        return min(chars.values()) == 0 and max(chars.values())==0 