class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(i, j):
            l,r = i, j
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        ans = ""
        for i in range(len(s)):
            j = len(s) - 1
            while j >= i:
                if j - i >= len(ans) and isPalindrome(i, j):
                    ans = s[i:j + 1]
                j -= 1
        return ans