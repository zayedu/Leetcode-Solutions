class Solution:
    def repeatedCharacter(self, s: str) -> str:
        chars = {}
        for i in s:
            if i not in chars:
                chars[i] = 1
            else: return i