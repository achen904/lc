class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #start at the same day, have a l (buy) and r (sell) pointer
        #while the the price at r is greater than the price at l
        #then we move continue moving r and take the max of the difference
        #if l is greater than r then we move l to r then continue
        ans = 0
        l, r = 0, 0
        while r < len(prices):
            if prices[r] > prices[l]:
                ans = max(ans, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r += 1
        return ans