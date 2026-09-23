class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = Counter(s)
        ans = []
        cur = counts[s[0]] - 1
        val = 1
        seen = set()
        seen.add(s[0])
        for i in range(1, len(s)):
            if cur == 0:
                ans.append(val)
                val = 0
                seen = set()
            if s[i] in seen:
                cur -= 1
                val += 1
            else:
                cur += counts[s[i]] - 1
                val += 1
                seen.add(s[i])
        ans.append(val)
        return ans
