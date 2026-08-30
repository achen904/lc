class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #must see if we detect a cycle, if cycle is detected then cannot finish all courses, if no cycle is detected then we can
        #build a dict to see what classes we must take to take class A
        reqs = defaultdict(list)
        for a, b in prerequisites:
            reqs[a].append(b)

        seen = set()
        processed = set()
        #do a dfs on every class to see if there is a cycle
        def dfs(i):
            if i in processed:
                return True
            if i in seen:
                return False
            seen.add(i)
            for req in reqs[i]:
                if not dfs(req):
                    return False
            processed.add(i)
            seen.remove(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True