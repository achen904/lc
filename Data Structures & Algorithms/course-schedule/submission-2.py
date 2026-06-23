class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        connections = defaultdict(list)
        for a, b in prerequisites:
            connections[a].append(b)
        seen = set()
        def dfs(course):
            if course in seen:
                return False
            seen.add(course)
            for prereq in connections[course]:
                if prereq not in seen:
                    dfs(prereq)
                else:
                    return False
            seen.remove(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

