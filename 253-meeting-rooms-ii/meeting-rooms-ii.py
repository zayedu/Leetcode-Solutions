class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        #if start < earliest end at that point, then u have to reserve another room. 
        heap = []
        for start,end in intervals:
            if heap and start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
                
        return len(heap)


