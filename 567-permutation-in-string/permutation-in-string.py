class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        perm_len = len(s1)
        perm_chars = { }
    
        for char in s1:
            if char not in perm_chars:
                perm_chars[char] = 1

            else:
                perm_chars[char] += 1

        #perm_chars contains count of chars in s1

        l = 0

        for r in range(len(s2)):
            while r - l + 1 > perm_len:
                if s2[l] in perm_chars:
                    perm_chars[s2[l]] += 1
                l += 1

            else:
                if s2[r] in perm_chars:
                    perm_chars[s2[r]] -= 1

                else:
                    while l < r:
                        if s2[l] in perm_chars:
                            perm_chars[s2[l]] += 1
                        l += 1


            if max(perm_chars.values()) == 0 and min(perm_chars.values()) == 0:
                return True
        return False



