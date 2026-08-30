class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        q = deque()
        deps = defaultdict(set)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            deps[b].add(a)
            indegree[a] += 1
        
        #find zero req
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            n = len(q)
            node = q.popleft()
            #remove node from deps in other
            for nei in deps[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
            ans.append(node)
        if len(ans) == numCourses:
            return ans
        return[]