class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set()
        def isValid(x,y):
            if not 0 <= x < len(grid):
                return False
            if not 0 <= y < len(grid[0]):
                return False
            if grid[x][y] == 1:
                return True
        
        def dfs(i,j):
            current = 1
            seen.add((i,j))
            for dx, dy in directions:
                new = (i + dx, j + dy)
                if isValid(i + dx, j + dy) and new not in seen:
                    current += dfs(i + dx, j + dy)
            return current
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                loc = (i, j)
                if loc not in seen and grid[i][j] == 1:
                    ans = max(ans, dfs(i,j))
        return ans
                    
        
