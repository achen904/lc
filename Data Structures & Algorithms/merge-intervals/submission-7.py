class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        l, r= 0, 0
        while r < len(intervals):
            s1, e1 = intervals[l]
            while r < len(intervals):
                s2, e2 = intervals[r]
                if s1 <= s2 <= e1:
                    e1 = max(e1, e2)
                    r += 1
                elif s2 <= e1 <= e2:
                    e1 = max(e1, e2)
                    r += 1
                else:
                    break
            l = r
            ans.append([s1, e1])
        return ans