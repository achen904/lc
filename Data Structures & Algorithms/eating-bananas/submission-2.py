class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, 1000000000
        while l < r:
            m = (l + r)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/m)
            if hours > h:
                l = m + 1
            else:
                r = m
        return l