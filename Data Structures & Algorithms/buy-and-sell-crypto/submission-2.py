class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        ans = 0
        while r < len(prices):
            if r == l:
                r += 1
            elif prices[l] < prices[r]:
                ans = max(ans, prices[r] - prices[l])
                r += 1
            else:
                l += 1
        return ans
        