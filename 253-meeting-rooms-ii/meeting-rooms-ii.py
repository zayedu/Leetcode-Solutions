class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        define an overlap as start time < end time, ONE meeting will have start time < less than
         end time, and any start time before this end time will result in the allocation of an 
         additional meeting room
        """
        intervals.sort(key= lambda interval:interval[0])
        start_times = sorted(time[0] for time in intervals)
        end_times = sorted(time[1] for time in intervals)
        
        interval_count = len(intervals)

        start_index = end_index = 0
        max_rooms = 0
        running_room_sum = 0
        while start_index < interval_count and end_index < interval_count:
            
            if start_times[start_index] < end_times[end_index]:
                running_room_sum += 1
                start_index += 1

            else:
                running_room_sum -= 1
                end_index += 1

            max_rooms = max(max_rooms,running_room_sum)

        return max_rooms

