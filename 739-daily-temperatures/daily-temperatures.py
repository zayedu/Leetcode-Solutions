class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = [

        ]

        '''
        stack should look like:
        stack = [
            [day(idx),temp],
            ...,
            [day(idx),temp],
        ]
        

        when we look at this stack we can compare temperatures and access 
        index and pop when we find a hotter day
        '''

        for i in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                day ,idx = stack.pop()
                ans[day] = i - day
            
            stack.append([i,temperatures[i]])

        return ans


        '''
        Complexities:
        Time = O(n)
        Space = O(n)
        '''