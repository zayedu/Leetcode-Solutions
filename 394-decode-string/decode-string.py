class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for char in s:
            if char == ']':
                str_build = ''
                while stack[-1] != '[':
                    str_build = stack.pop()+str_build

                stack.pop()
                if not stack[-1].isdigit():
                    continue
                num_build = ''
                while stack and stack[-1].isdigit():
                    num_build = stack.pop()+num_build
                
                stack.append(int(num_build)*str_build)

            else:
                stack.append(char)

        return ''.join(stack)


