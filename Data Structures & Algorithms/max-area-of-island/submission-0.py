class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        neighbors = defaultdict(list)
        directions = [(1,0), (-1, 0), (0, 1), (0, - 1)]
        def valid(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return False
            return True
        for r in range (len(grid)):
            for c in range (len(grid[0])):
                if grid[r][c] == 1:
                    neighbors[(r,c)] = []
                    for dx, dy in directions:
                        if valid(r + dx, c + dy) and grid[r + dx][c + dy] == 1:
                            neighbors[(r,c)].append((r + dx, c + dy))
        seen = set()
        ans = 0
        stack = []
        def dfs(node):
            size = 1
            seen.add(node)
            stack.append(node)
            while stack:
                neighbor = stack.pop()
                for next in neighbors[neighbor]:
                    if next not in seen:
                        seen.add(next)
                        stack.append(next)
                        size += 1
            return size

        for neighbor in neighbors:
            if neighbor not in seen:
                ans = max (ans, dfs(neighbor))
        return ans