class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        ans = 0
        def isValid(x,y):
            if not 0 <= x < len(grid):
                return False
            if not 0 <= y < len(grid[0]):
                return False
            return True
        def dfs(x,y):
            if (x, y) not in seen:
                seen.add((x,y))
                for dx, dy in directions:
                    if isValid(x + dx, y + dy) and grid[x + dx][y + dy] == "1":
                        dfs(x + dx, y + dy)
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                tup = (x,y)
                if grid[x][y] == "1" and tup not in seen:
                    ans += 1
                    dfs(x,y)
        return ans
