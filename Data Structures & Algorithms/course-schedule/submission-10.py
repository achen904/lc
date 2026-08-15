class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        connections = defaultdict(list)
        processed = set()
        seen = set()
        for a, b in prerequisites:
            connections[a].append(b)
        
        def dfs(node):
            if node in seen:
                return False
            if node in processed:
                return True
            seen.add(node)
            for neighbor in connections[node]:
                if not dfs(neighbor):
                    return False
            processed.add(node)
            seen.remove(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        
        