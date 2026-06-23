class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #directed graph so if there is a cycle then cannot complete
        seen = set()
        connections = defaultdict(list)
        for a,b in prerequisites:
            connections[b].append(a)
        def dfs(node):
            if node in seen:
                return False
            seen.add(node)
            for neighbor in connections[node]:
                if not dfs(neighbor):
                    return False
            seen.remove(node)
            return True
        for node in range(numCourses):
            if not dfs(node):
                return False
        return True
        