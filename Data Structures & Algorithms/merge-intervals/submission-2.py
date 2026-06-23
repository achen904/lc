class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l, r = 0, 0
        ans =[]
        while r < len(intervals):
            a, b = intervals[l]
            while r < len(intervals):
                a2, b2 = intervals[r]
                #[[0, 2], [1, 4], [3 ,5]]
                if a2 <= b <= b2:
                    r += 1
                    b = b2
                elif a <= b2 <= b:
                    r += 1
                else:
                    break
            a2, b2 = intervals[r-1]
            ans.append([a,max(b, b2)])
            l = r
        return ans
