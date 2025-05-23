class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [ ]
        '''
        stack is gonna hold numbers to have stuff done on it
        '''
        ans = 0
        for token in tokens:
            if token == '+':
               stack.append(stack.pop() + stack.pop())
            elif token == '-':
                stack.append(-1*stack.pop()+stack.pop())
            elif token == '*':
                stack.append(stack.pop()*stack.pop())
            elif token == '/':
                stack.append(int((1/stack.pop())*stack.pop()))

            else:
                stack.append(int(token ))
        return stack[0]
