class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        seen = set()
        def isValid(x,y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1":
                return True
            return False 
        def dfs(i,j):
            seen.add((i,j))
            for dx, dy in directions:
                if (i + dx,j +dy) not in seen and isValid(i + dx, j + dy):
                    dfs(i + dx, j + dy)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in seen:
                    ans += 1
                    dfs(i,j)
        return ans