class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = -1
        while l <= r:
            m = ( l + r) // 2
            total = 0
            for pile in piles:
                total += math.ceil(pile / m)
            if total <= h:
                r = m - 1
                ans = m
            else:
                l = m + 1
        return ans