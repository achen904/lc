class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        numFresh = 0
        numFound = 0
        ans = 0
        q = deque()
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    numFresh += 1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def isValid(x,y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1 and ((x,y)) not in seen:
                return True
            return False
        while q and numFresh != numFound:
            size = len(q)
            for i in range(size):
                x, y = q.popleft()
                for dx, dy in directions:
                    if isValid(x + dx , y + dy):
                        q.append((x + dx, y + dy))
                        seen.add((x + dx, y + dy))
                        numFound += 1
            ans += 1
        if numFound == numFresh:
            return ans
        return -1               
