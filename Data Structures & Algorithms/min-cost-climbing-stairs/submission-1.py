class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #cheapest cost to reach i = min(cheapest[i - 1] + cost[i], chepeast[i - 2] + cost[i - 2])
        #could use an array of size len(cost) + 1
        #but we only need the last 2 cheapest so can just use 2 variables
        #to save some space

        #base case, costs 0 to start at index 1 or 0
        oneBack = 0
        twoBack = 0
        cheapest = None
        for i in range(2, len(cost)):
            cheapest = min(oneBack + cost[i - 1], twoBack + cost[i -2])
            twoBack = oneBack
            oneBack = cheapest
        n = len(cost)
        return min(oneBack + cost[n - 1], twoBack + cost[n -2])