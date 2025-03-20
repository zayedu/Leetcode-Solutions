class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [ ]
        for c in tokens:
            if c == '+':
                stack.append(stack.pop()+stack.pop())
            elif c == '-':
                stack.append(-1*stack.pop()+stack.pop())
            elif c == '*':
                stack.append(stack.pop()*stack.pop())
            elif c == '/':
                den = stack.pop()
                num = stack.pop()
                stack.append(int(num/den))
            else:
                stack.append(int(c))

        return stack[0]
            
