class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)

        stack = []

        '''
        stack should look like:
            [
                [temp,index],
                ...,
            ]
        '''


        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                temp, idx = stack.pop()
                answer[idx] = i - idx
            stack.append([temperatures[i],i])

        return answer