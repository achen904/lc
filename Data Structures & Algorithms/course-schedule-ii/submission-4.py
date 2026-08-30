class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #run dfs, once dfs is done on a course that means we can take that course
        #so add it to the output
        #however if we detect a cycle early that means we can return []

        ans = []
        seen = set() #use seen for cycle detection for a give course then remove a course from it after knowing it is able to be completed so we don't mistake for a cycle on a different path that also uses this course
        completed = set() #use completed so we can prune early if we a later course requires a search through a path we already check is valid
        #first get reqs for each course
        reqs = defaultdict(set)
        for a, b in prerequisites:
            reqs[a].add(b)
        #dfs returns whether or not we are abel to take a class
        def dfs(i):
            if i in completed:
                return True
            if i in seen:
                return False
            seen.add(i)
            for req in reqs[i]:
                if not dfs(req):
                    return False
            #if we can take all the requirements for the course then we can take this course
            ans.append(i)
            completed.add(i)
            seen.remove(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans

