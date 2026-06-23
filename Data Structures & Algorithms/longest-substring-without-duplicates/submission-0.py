class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chSet = set()
        l, r = 0, 0
        ret = 0
        while r < len(s):
            while s[r] in chSet:
                chSet.remove(s[l])
                l += 1
            chSet.add(s[r])
            ret = max(ret, r - l + 1)
            r+= 1
        return ret
