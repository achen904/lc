class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        i = 0
        start, end = newInterval
        while i < n and intervals[i][1] < start:
            ans.append(intervals[i])
            i += 1
        
        while i < n and end >= intervals[i][0]:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        ans.append([start, end])

        while i < n:
            ans.append(intervals[i])
            i += 1
        return ans

