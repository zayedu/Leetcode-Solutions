class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        '''
        stack should look like :[
            [temp0,ind0],
            [temp1,ind1],
            ...,
        ]
        '''

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                stackTemp, stackI = stack.pop()
                res[stackI] = i-stackI
            stack.append([temperatures[i],i])
        return res 