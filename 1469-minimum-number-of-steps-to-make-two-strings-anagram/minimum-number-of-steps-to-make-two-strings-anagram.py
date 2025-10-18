class Solution:
    def minSteps(self, s: str, t: str) -> int:
    
        count = [0] *26

        for char in s:
            count[ord(char)-ord('a')]+=1

        for char in t:
            if count[ord(char)-ord('a')]:
                count[ord(char)-ord('a')]-=1

        return sum(count)