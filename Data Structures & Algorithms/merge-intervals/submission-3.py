class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #first sort the intervals
        intervals.sort()
        #use a left and right pointer to know which intervals overlap
        l, r = 0, 0
        #iterate until we reach the end
        ans = []
        while r < len(intervals):
            #get start interval
            a1, b1 = intervals[l]
            #keep increasing end interval until it doesn;t over lap with start
            while r < len(intervals):
                #get current interval to compare
                a2, b2 = intervals[r]
                #Scenario 1: interval over laps if b1 is between a2 and b2
                if a2 <= b1 <= b2:
                    r += 1
                    #now our interval got stretched to handle larger b
                    b1 = b2
                #Scenario 2: interval overlaps if b2 is between a1 and b1
                elif a1 <= b2 <= b1:
                    r += 1
                else:
                    break
            a2, b2 = intervals[r - 1]
            ans.append([a1, max(b1, b2)])
            l = r
            
        return ans