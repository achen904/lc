class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()
        map = defaultdict(set)

        for a, b in edges:
            map[b].add(a)
            map[a].add(b)

        def dfs(node, parent):
            if node in seen:
                return False
            seen.add(node)
            for child in map[node]:
                if child != parent:
                    if not dfs(child, node):
                        return False
            return True
        if dfs(0, None) and len(seen) == n:
            return True
        return False

         