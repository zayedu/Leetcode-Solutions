class Solution:
    def isValid(self, s: str) -> bool:
        
        closers = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        stack = []

        for char in s:
            if char not in closers:
                stack.append(char)
            else:
                if not stack or stack[-1] != closers[char]:
                    return False
                stack.pop()

        return len(stack) == 0