class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors = defaultdict(list)
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        seen = set()
        def dfs(node):
            seen.add(node)
            for neighbor in neighbors[node]:
                if neighbor not in seen:
                    dfs(neighbor)
        ans = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans