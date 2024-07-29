class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        perm_chars = { }

        for s in s1:
            if s in perm_chars:
                perm_chars[s] += 1
            else:
                perm_chars[s] = 1

        l = 0
        for r in range(len(s2)):
            while r - l + 1 > len(s1):
                if s2[l] in perm_chars:
                    perm_chars[s2[l]] += 1
                l += 1
            if s2[r] in perm_chars:
                perm_chars[s2[r]] -= 1

            else:
                while l < r:
                    if s2[l] in perm_chars:
                        perm_chars[s2[l]] += 1

                    l += 1

            if max(perm_chars.values()) == min(perm_chars.values()) == 0:
                return True

        return False
