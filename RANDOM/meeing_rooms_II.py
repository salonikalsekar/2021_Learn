class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        h = []
        intervals = sorted(intervals, key=lambda x: x[0])

        heapq.heappush(h, intervals[0][1])

        for i in range(1, len(intervals)):

            if h[0] <= intervals[i][0]:
                heapq.heappop(h)

            heapq.heappush(h, intervals[i][1])

        return len(h)