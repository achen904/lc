class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #Define DP[row][col] where DP[row][col] gives the
        #number of unique paths that can be taken from the top
        #left corder to [row][col]
        #Base case, top row and left column DP = 1
        DP = [[0] * n for _ in range(m)]
        for i in range(len(DP)):
            DP[i][0] = 1
        for i in range(len(DP[0])):
            DP[0][i] = 1
        #we can traverse from left to right horizontally, as the 
        #only directions we can come from are the left or the one
        #above, so at any position, we should have already calculated
        #the previous step 
        #the number of ways we can get to a index is the sum
        #of the number of ways we can get to the one directly
        #above + the number of ways we can get to the one directly
        #to the left
        for r in range(1, len(DP)):
            for c in range(1, len(DP[0])):
                DP[r][c] = DP[r-1][c] + DP[r][c-1]
        return DP[m-1][n-1]