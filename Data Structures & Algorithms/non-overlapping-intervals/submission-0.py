class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0][1]
        ans = 0

        for start, end in intervals[1:]:
            if start < prev:
                ans += 1
                prev = min(end, prev)
            else:
                prev = end
        return ans