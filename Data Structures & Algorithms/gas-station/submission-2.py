class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        #if cost greater than gas than we know a route is not possible
        #if cost is less than or equal to then we know a route is possible

        total = 0
        ans = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0: #if we ever reach a negative then we cannot start
            #at any point along that segment because they will all run
            #out of gas at that point
                total = 0
                ans = i + 1
        return ans
