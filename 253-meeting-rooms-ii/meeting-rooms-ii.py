class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        
        for s,e in intervals:
            start.append(s)
            end.append(e)
        
        start.sort()
        end.sort()
        room_count = 0 #increment if a meeting starts before one ends
        end_ptr = 0
        for s in start:
            if s < end[end_ptr]: 
                room_count += 1 
            else: 
                end_ptr += 1 
        
        return room_count



