class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([interval[0] for interval in intervals])
        ends = sorted([interval[1] for interval in intervals])
        
        meetings = len(intervals)

        start_index = 0
        end_index = 0

        max_overlaps = 0
        running_overlaps = 0

        while start_index < meetings and end_index < meetings:

            if starts[start_index] < ends[end_index]:
                running_overlaps += 1
                start_index += 1
            else:
                running_overlaps -= 1
                end_index += 1

            max_overlaps = max(max_overlaps,running_overlaps)

        return max_overlaps

