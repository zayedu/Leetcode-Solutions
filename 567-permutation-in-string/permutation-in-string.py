class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        perm_chars = {

        }

        """
        perm_chars which should keep track of freq of chars in s1
        char -> freq
        """

        for char in s1:
            if char not in perm_chars:
                perm_chars[char] = 1
            else:
                perm_chars[char] += 1

        l = 0
        for r in range(len(s2)):
            if s2[r] in perm_chars:
                perm_chars[s2[r]] -= 1
            else:
                if s2[l] in perm_chars:
                    perm_chars[s2[l]] += 1
                l += 1
            while (r - l + 1) > len(s1):
                if s2[l] in perm_chars:
                    perm_chars[s2[l]] += 1
                l += 1
            if min(perm_chars.values()) == 0 and max(perm_chars.values()) == 0:
                return True

        return False


        
                