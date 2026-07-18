class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n -1 , -1, -1):
            for j in range(i, n):
                #if first and last letter match and middle is also
                #palindrome or if substring is len(2) or less then
                #the substring is a palindrome
                if s[i] == s[j] and (j - i + 1 <= 2 or dp[i + 1][j- 1]):
                    dp[i][j] = True
                    if end - start + 1 <= j - i + 1:
                        end = j
                        start = i
        return s[start:end + 1]