class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i, ch in enumerate(s):
            lastIndex[ch] = i
        
        ans = []
        end = 0
        cur = 0
        for i in range(len(s)):
            end = max(end, lastIndex[s[i]])
            cur += 1
            if end == i:
                ans.append(cur)
                cur = 0
        return ans