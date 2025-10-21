class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda interval:interval[0])

        stack = []

        for interval in intervals:
            if stack and stack[-1][1] >= interval[0]:
                stack[-1][1] = max(stack[-1][1],interval[1])
            else:
                stack.append(interval)

        return stack