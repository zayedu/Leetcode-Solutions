class Solution:
    def isValid(self, s: str) -> bool:
        closers = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }

        stack = []

        for c in s:
            if c in closers.keys():
                stack.append(c)
            else:
                if not stack or c != closers[stack.pop()]:
                    return False
        
        return len(stack)==0


        '''
        Complexity:
        Time = O(n)
        Space = O(n)
        '''