class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [ ]

        for char in tokens:
            if char == '+':
                stack.append(stack.pop()+stack.pop())

            elif char == '-':
                stack.append(-1*stack.pop()+stack.pop())

            elif char == '*':
                stack.append(stack.pop()*stack.pop())
            
            elif char == '/':
                den = stack.pop()
                num = stack.pop()

                stack.append(int(num/den))

            else: 
                stack.append(int(char))

        return stack[-1]