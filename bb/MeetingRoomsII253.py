class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        intervals.sort(key = lambda x : x[0])
        
        heapq.heappush(rooms, intervals[0][1])

        for interval in intervals[1:]:
            if interval[0] >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval[1])
        
        return len(rooms)