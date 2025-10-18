class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        for index in range(len(s)):
            if s[index] == ')' and not stack:
                s[index] = ''

            if s[index] == '(':
                stack.append(index)

            if stack and s[index] == ')':
                stack.pop()


        for index in stack:
            s[index] = ''


        return "".join(s)

