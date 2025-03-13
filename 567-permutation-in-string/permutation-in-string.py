class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        perm_chars = {

        }

        '''
        perm_chars should look like:
            chars -> freq
        '''

        for c in s1:
            if c not in perm_chars:
                perm_chars[c] = 1

            else:
                perm_chars[c] += 1

        
        l = 0

        for r in range(len(s2)):
            if s2[r] not in perm_chars:
                while l <= r:
                    if s2[l] in perm_chars:
                        perm_chars[s2[l]] += 1
                    l += 1
            else:
                perm_chars[s2[r]] -= 1

                while(perm_chars[s2[r]]<0):
                    if s2[l] in perm_chars:
                            perm_chars[s2[l]] += 1
                    l += 1
            if max(perm_chars.values()) == 0 and min(perm_chars.values())==0:
                return True
        return False


