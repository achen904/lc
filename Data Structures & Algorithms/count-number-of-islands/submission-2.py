class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        seen = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def isValid(x, y):
            if not 0 <= x < len(grid):
                return False
            if not 0 <= y < len(grid[0]):
                return False
            if grid[x][y] == "1":
                return True
        def dfs(i,j):
            seen.add((i,j))
            for dx, dy in directions:
                tup = (i + dx, j + dy)
                if isValid(i + dx, j + dy) and tup not in seen:
                    dfs(i+dx, j +dy)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                tup = (i, j)
                if tup not in seen and grid[i][j] == "1":
                    ans += 1
                    dfs(i,j)
        return ans
            

