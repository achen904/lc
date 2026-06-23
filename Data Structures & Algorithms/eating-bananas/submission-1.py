class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = float('inf')
        while l <= r:
            m = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m)
            if hours <= h:
                ans = min(ans, m)
                r = m - 1
            else:
                l = m + 1
        return ans
