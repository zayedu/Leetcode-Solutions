class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sols, ans = [],[]

        def backtrack(openb, closeb):
            if openb == closeb and openb == n:
                
                sols.append(''.join(ans))
                return

            if openb < n:
                ans.append('(')
                backtrack(openb+1,closeb)
                ans.pop()

            if closeb < openb:
                ans.append(')')
                backtrack(openb,closeb+1)
                ans.pop()

        backtrack(0,0)

        return sols