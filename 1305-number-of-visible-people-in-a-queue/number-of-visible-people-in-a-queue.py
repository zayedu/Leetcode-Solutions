class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # monotonic decreasing stack
        # iterate backwards

        stack = []

        answer = [0]*len(heights)

        for index in range(len(heights)-1,-1,-1):
            height = heights[index] 

            count = 0
            while stack and stack[-1] < height:
                stack.pop()
                count += 1

            if stack:
                count += 1

            stack.append(height)
            answer[index] = count

        return answer