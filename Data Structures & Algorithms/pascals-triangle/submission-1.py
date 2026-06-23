class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        ans.append([1])
        for i in range(1, numRows):
            l, r = -1, 0
            cur = []
            prev = ans[i - 1]
            while -1 <= l < len(prev):
                v1 = prev[l] if 0 <= l < len(prev) else 0
                v2 = prev[r] if 0 <= r < len(prev) else 0
                cur.append(v1 + v2)
                l += 1
                r += 1
            ans.append(cur)
        return ans