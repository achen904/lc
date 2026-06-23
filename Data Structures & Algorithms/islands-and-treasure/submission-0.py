class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])
        def valid(r,c):
            if r < 0 or r >= ROW or c < 0 or c >= COL or grid[r][c] == -1:
                return False
            return True
        q = deque()
        seen = set()
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r,c))
                    seen.add((r,c))
        def bfs(r,c):
            seen.add((r,c))
            grid[r][c] = dist
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        dist = 1
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                seen.add((r,c))
                for dx, dy in directions:
                    if valid(r + dx, c + dy) and (r+dx, c+dy) not in seen:
                        bfs(r+dx, c+dy)
                        q.append((r+dx, c+dy))
            dist += 1


