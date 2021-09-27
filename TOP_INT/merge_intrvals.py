class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        merged_intervals = []

        start = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= start[1]:
                start[1] = max(intervals[i][1], start[1])

            else:
                merged_intervals.append(start)
                start = intervals[i]

        merged_intervals.append(start)

        return merged_intervals