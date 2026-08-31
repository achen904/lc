class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        ans = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(x,y):
            if memo[x][y] != -1:
                return memo[x][y]
            cur = matrix[x][y]
            for dx, dy in directions:
                if 0 <= x + dx < len(matrix) and 0 <= y + dy < len(matrix[0]):
                    if matrix[x+dx][y+dy] > cur:
                        memo[x][y] = max(memo[x][y], 1 + dfs(x +dx, y+dy))
            memo[x][y] = max(memo[x][y], 1)
            return memo[x][y]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if memo[i][j] == -1:
                    ans= max(dfs(i,j), ans)
        return ans
        
