class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counts = defaultdict(int)
        ans = 0
        l, r, total = 0, 0, 0
        for r in range(len(fruits)):
            counts[fruits[r]] += 1
            total += 1
            while len(counts) > 2:
                f = fruits[l]
                counts[f] -= 1
                total -= 1
                if counts[f] == 0:
                    del counts[f]
                l += 1
            ans = max(ans, total)
        return ans