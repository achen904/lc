class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #we can use 2 pointers, 1 pointer for each text. if the 2 pointers at the current index give the same character, then we add 1 then move both pointers, however if they don't match we try moving 1 poitner at a time to see which one gives us the large value. Since there are so many combinatinos this poitns us to using dp. We can use top down dp with memoizaton
        memo = {}

        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i >= len(text1) or j >= len(text2):
                return 0
            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + dfs(i + 1, j + 1)
            else:
                memo[(i,j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            return memo[(i,j)]
        return dfs(0, 0)