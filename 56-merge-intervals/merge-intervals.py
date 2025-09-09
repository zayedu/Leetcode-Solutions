class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        merged_intervals_stack = [ ]

        intervals.sort(key = lambda interval:interval[0])

        for interval in intervals:
            if merged_intervals_stack and merged_intervals_stack[-1][1] >= interval[0]:
                merged_intervals_stack[-1][1] = max(interval[1],merged_intervals_stack[-1][1])
            else:
                merged_intervals_stack.append(interval)

        return merged_intervals_stack        