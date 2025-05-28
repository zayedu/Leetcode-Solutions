class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
         
        perm = {

        }

        '''
        perm check permutation i.e multiplicity of chars
        {
            char(in s1) : freq_in_s1
        }
        '''

        for char in s1:
            if char not in perm:
                perm[char] = 1
            else:
                perm[char] += 1


        l = 0

        for r in range(len(s2)):
            if s2[r] in perm:
                perm[s2[r]] -= 1
                
                while perm[s2[r]] < 0:
                    if s2[l] in perm:
                        perm[s2[l]] += 1
                    l += 1

            else:
                while l <= r:
                    if s2[l] in perm:
                        perm[s2[l]] += 1
                    l += 1

            if max(perm.values()) == 0 and min(perm.values()) == 0:
                return True

        return False