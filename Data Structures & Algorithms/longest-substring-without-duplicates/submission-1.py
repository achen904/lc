class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l, r = 0, 0
        ret = 0
        while r < len(s):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            ret = max(ret, r - l + 1)
            r+= 1
        return ret
