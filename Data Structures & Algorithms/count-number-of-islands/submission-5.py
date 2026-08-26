class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
       seen = set()
       directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

       ans = 0
       def isValid(x, y):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1" and (x, y) not in seen:
            return True
        return False
       def dfs(x, y):
        seen.add((x, y))
        for dx, dy in directions:
            if isValid(x + dx, y + dy):
                dfs(x + dx, y + dy)
       for x in range(len(grid)):
        for y in range(len(grid[0])):
            if isValid(x,y):
                ans += 1
                dfs(x, y)
       return ans


