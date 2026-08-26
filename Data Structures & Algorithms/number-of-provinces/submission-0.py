class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        connections = defaultdict(list)

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i != j:
                    if isConnected[i][j] == 1:
                        connections[i].append(j)
                        connections[j].append(i)
        seen = set()
        ans = 0
        def dfs(i):
            seen.add(i)
            for neighbor in connections[i]:
                if neighbor not in seen:
                    dfs(neighbor)
        for i in range(len(isConnected)):
            if i not in seen:
                ans += 1
                dfs(i)
        return ans

