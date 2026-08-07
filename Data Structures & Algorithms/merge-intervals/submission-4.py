class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l, r = 0, 0
        ans = []
        while r < len(intervals):
            a1, b1 = intervals[l]
            while r < len(intervals):
                a2, b2 = intervals[r]
                if a2 <= b1 <= b2:
                    r += 1
                    b1 = b2
                elif a1 <= b2 <= b1:
                    r += 1
                else:
                    break
            a2, b2 = intervals[r - 1]
            ans.append([a1, max(b1, b2)])
            l = r
        return ans
                    