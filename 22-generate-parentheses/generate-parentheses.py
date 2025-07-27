class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        answer = [ ]
        soln = []

        def backtrack(openN,closeN):

            if openN == closeN and openN == n:
                answer.append(''.join(soln))
                return

            if openN < n:
                soln.append('(')
                backtrack(openN+1,closeN)
                soln.pop()

            if openN > closeN:
                soln.append(')')
                backtrack(openN,closeN+1)
                soln.pop()

        backtrack(0,0)

        return answer
