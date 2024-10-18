class Solution:
    def customSortString(self, order: str, s: str) -> str:

        freq = {

        }

        """
        freq should look like:
        char -> freq
        """

        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        res = ""

        for char in order:
            if char in freq:
                res += (char*freq[char])
                freq[char] = 0
            
        for char,occ in freq.items():
            if occ != 0:
                res += (char*occ)

        return res
            


