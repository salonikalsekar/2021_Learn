class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        inserted_int = []

        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            inserted_int.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        inserted_int.append(newInterval)

        while i < len(intervals):
            inserted_int.append(intervals[i])
            i += 1

        return inserted_int
