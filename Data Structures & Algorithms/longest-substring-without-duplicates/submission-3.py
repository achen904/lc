class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = {}
        l, r = 0, 0
        ans = 0
        while r < len(s):
            if s[r] in unique:
                l = max(unique[s[r]] + 1, l)
            unique[s[r]] = r
            ans = max(ans, r- l + 1)
            r += 1      
        return ans
        