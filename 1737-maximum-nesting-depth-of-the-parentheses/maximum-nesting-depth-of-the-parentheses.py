class Solution:
    def maxDepth(self, s: str) -> int:
        
        max_len = 0
        running_len = 0
        for char in s:
            if char == '(':
                running_len += 1

            if char == ')':
                running_len -= 1

            max_len = max(running_len,max_len)

        return max_len
