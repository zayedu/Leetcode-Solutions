class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        transformations = { }

        '''
        transformations should look like s[i] - > t[i]
        '''

        for i in range(len(s)):
            curr = s[i]
            should_be = t[i]

            if curr not in transformations:
                if should_be in transformations.values():
                    return False
                transformations[s[i]] = t[i]

            else:
                if transformations[s[i]] != t[i]:
                    return False

        return True