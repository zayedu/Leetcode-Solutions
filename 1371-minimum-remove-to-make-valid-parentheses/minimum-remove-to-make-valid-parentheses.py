class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s=list(s)
        for index in range(len(s)):

            if s[index] == '(':
                stack.append(index)

            if s[index] == ')' and stack:
                stack.pop()

            elif s[index] == ')':
                s[index] = ''

        for idx in stack:
            s[idx] = ''

        return "".join(s)