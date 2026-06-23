class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        map = defaultdict(list)
        for a, b in prerequisites:
            map[a].append(b)

        ans = []
        seen = set()
        visited = set()
        def dfs(node):
            if node in seen:
                return False
            if node in visited:
                return True
            seen.add(node)
            for neighbor in map[node]:
                if not dfs(neighbor):
                    return False
            seen.remove(node)
            visited.add(node)
            ans.append(node)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return ans
        
                