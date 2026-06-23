class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l = maxfreqs = ret = 0
        for r in range(len(s)):
            if s[r] not in counts:
                counts[s[r]] = 1
            else:
                counts[s[r]] += + 1
            maxfreqs = max(maxfreqs,counts[s[r]])
            while (r - l + 1) - maxfreqs > k:
                counts[s[l]] -=  1
                l += 1
            ret = max(ret, r - l + 1)
        return ret