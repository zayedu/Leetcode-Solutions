class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans,stack = [ ], [ ]
        #open < n: +open
        #open = close = n: return stack
        #open > close: +close
        def backtrack(openb,closeb):
            if openb == closeb and openb == n:
                ans.append(''.join(stack))
                return 
            if openb < n:
                stack.append('(')
                backtrack(openb+1,closeb)
                stack.pop()

            if openb > closeb:
                stack.append(')')
                backtrack(openb,closeb+1)
                stack.pop()

        backtrack(0,0)
        return ans

        '''
        Complexity:
            Time = O(2^n)
            Memory = O(k) k is the number of possible parentheses combination

        '''