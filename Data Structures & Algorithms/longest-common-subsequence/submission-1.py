class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #bottom up apporach
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)] #stores the longest matching subsequence starting at i for text1 and at j for text2
        #at the end we want dp[0][0] to hold answer
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1 ,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]
