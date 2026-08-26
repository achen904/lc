class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        ans = 0
        def dfs(i):
            seen.add(i)
            for province, neighbor in enumerate(isConnected[i]):
                if neighbor == 1 and province not in seen:
                    dfs(province)
        for i in range(len(isConnected)):
            if i not in seen:
                ans += 1
                dfs(i)
        return ans

