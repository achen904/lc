class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for i in range(1, m ):
            temp = [1] * n
            for j in range(1, n):
                temp[j] = temp[j - 1] + dp[j]
            dp = temp
        return dp[n - 1]