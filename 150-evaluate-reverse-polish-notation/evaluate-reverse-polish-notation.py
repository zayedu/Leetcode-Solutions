class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [ ]
        '''
        stack should have all numbers, we will always look at the last two nums when we get an operand
        '''
        for token in tokens:
            if token == '+':
                stack.append(stack.pop()+stack.pop())
            elif token == '-':
                stack.append(-1*stack.pop()+stack.pop())
            elif token == '*':
                stack.append(stack.pop()*stack.pop())
            elif token == '/':
                den = stack.pop()
                num = stack.pop()
                stack.append(int(num/den))

            else:
                stack.append(int(token))

        return stack.pop()
        
        '''
        Complexities:
        Time = O(n) 
        Memory = O(n)
        '''