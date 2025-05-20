class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans,sol = [],[]

        def backtrack(openN:int,closeN:int):

            if openN == closeN and openN == n:

                sol.append(''.join(ans))
                return

            if openN < n:
                ans.append('(')
                backtrack(openN+1,closeN)
                ans.pop()

            if openN > closeN:
                ans.append(')')
                backtrack(openN,closeN+1)
                ans.pop()

        backtrack(0,0)
        return sol