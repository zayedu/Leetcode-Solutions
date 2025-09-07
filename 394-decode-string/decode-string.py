class Solution:
    def decodeString(self, s: str) -> str:
        stack = [ ]

        for idx in range(len(s)):
            char = s[idx]

            if char != ']':
                stack.append(char)
            
            else:
                string_to_be_built = ""

                while stack and stack[-1] != '[':
                    string_to_be_built = stack.pop() + string_to_be_built

                stack.pop()
                
                
                multiplier = ""
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier

                multiplier = int(multiplier)
                stack.append(multiplier*string_to_be_built)


        return ''.join(stack)
                


                

