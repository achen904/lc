class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = defaultdict(int)
        l, r = 0, 0
        ans = 0
        while r < len(s):
            if s[r] in unique:
                while unique[s[r]] > 0:
                    unique[s[l]] -= 1
                    l += 1
            unique[s[r]] += 1
            ans = max(ans, r- l + 1)
            r += 1      
        return ans
        