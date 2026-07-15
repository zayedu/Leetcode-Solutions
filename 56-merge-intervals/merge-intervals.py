class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        """
        sort by start time
        use a stack and go up, update head interval until you find a start time after your end time and then new stack
        """

        intervals.sort(
            key = lambda interval: interval[0]
        )

        stack = []

        for interval in intervals:
            if stack and stack[-1][1] >= interval[0]:
                stack[-1][1] = max(interval[1], stack[-1][1])
            else:
                stack.append(interval)

        return stack
