class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = set()
        cycle = set()
        cycleStart = -1
        connections = defaultdict(list)
        for a, b in edges:
            connections[a].append(b)
            connections[b].append(a)
        #DFS returns true if node is in a cycle, 
        def dfs(node, parent):
            nonlocal cycleStart
            if node in visited:
                if cycleStart == -1:
                    cycleStart = node
                    cycle.add(node)
                return True
            visited.add(node)
            for neighbor in connections[node]:
                if neighbor != parent:
                    if dfs(neighbor, node):
                        if cycleStart != -1:
                            cycle.add(node)
                        if node == cycleStart:
                            cycleStart = -1
                        return True
            return False
        dfs(1, -1)
        for a, b in reversed(edges):
            if a in cycle and b in cycle:
                return [a,b] 