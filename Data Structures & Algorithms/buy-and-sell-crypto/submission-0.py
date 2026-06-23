class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        ret = 0
        while r < len(prices):
            if l == r:
                r += 1
            elif prices[l] < prices[r]:
                ret = max(ret, prices[r] - prices[l])
                r += 1
            else:
                l += 1
        return ret
