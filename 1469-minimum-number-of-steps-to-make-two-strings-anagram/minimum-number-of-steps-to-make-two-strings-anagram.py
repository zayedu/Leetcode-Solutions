class Solution:
    def minSteps(self, s: str, t: str) -> int:

        counts = [0]*26

        for char in s:
            counts[ord(char)-ord('a')] += 1

        for char in t:
            if counts[ord(char)-ord('a')]:
                counts[ord(char)-ord('a')] -= 1
            # else:
            #     counts[ord(char)-ord('a')] += 1

        return sum(counts)

