class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        seen = set()
        q = deque()
        def isValid(x,y):
            if not 0 <= x < len(grid):
                return False
            if not 0 <= y < len(grid[0]):
                return False
            if grid[x][y] == 2**31 - 1:
                return True
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))
                    seen.add((i,j))
        dist = 0
        while q:
            n = len(q)
            dist += 1
            for _ in range(n):
                x, y = q.popleft()
                seen.add((x,y))
                for dx, dy in directions:
                    nxt = (x + dx, y + dy)
                    if isValid(x + dx, y +dy) and nxt not in seen:
                        grid[x + dx][y + dy] = dist
                        q.append(nxt)

    
                            

        