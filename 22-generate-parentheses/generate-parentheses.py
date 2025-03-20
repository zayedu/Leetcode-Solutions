class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add ( if open < N
        #only add ) if closed < open
        # add to result if closed == open == n

        stack = []
        res = []

        def backtrack(openN,closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append('(')
                backtrack(openN+1,closeN)
                stack.pop()

            if openN > closeN:
                stack.append(')')
                backtrack(openN,closeN+1)
                stack.pop()
        backtrack(0,0)
        return res
