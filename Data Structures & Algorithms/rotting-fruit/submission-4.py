class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        seen = set()
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        def isValid(x,y):
            if not 0 <= x < len(grid):
                return False
            if not 0 <= y < len(grid[0]):
                return False
            if grid[x][y] == 1:
                return True
        # add rotten to queue
        freshFruit = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    seen.add((i,j))
                    q.append((i,j))
                elif grid[i][j] == 1:
                    freshFruit += 1
        if freshFruit == 0:
            return 0
        time = 0
        while freshFruit > 0 and q:
            n = len(q)
            for _ in range(n):
                x, y = q.popleft()
                seen.add((x,y))
                for dx, dy in directions:
                    nxt = (x + dx, y+ dy)
                    if nxt not in seen and isValid(x + dx, y + dy):
                        q.append(nxt)
                        grid[x + dx][y + dy] =2
                        freshFruit -= 1
            time += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return time