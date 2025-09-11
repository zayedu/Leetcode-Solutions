class Solution:
    def isValid(self, s: str) -> bool:

        closers = {
            '}':'{',
            ')':'(',
            ']':'['  
        }
        stack = [ ]
        for char in s:
            if char not in closers:
                stack.append(char)

            else:

                if not stack or stack.pop() != closers[char]:
                    return False

        return not stack


