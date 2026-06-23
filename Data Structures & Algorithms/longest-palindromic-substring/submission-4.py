class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            #treat the index i as a center and not beginning
            #even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 >= len(ans):
                    ans = s[l:r+1]
                l -= 1
                r += 1
            #odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 >= len(ans):
                    ans = s[l:r+1]
                l -= 1
                r += 1
        return ans