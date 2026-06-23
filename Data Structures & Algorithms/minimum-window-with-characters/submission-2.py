class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shortr = -1
        shortl = -1
        shortest = float('inf')
        l = 0
        countT = defaultdict(int)
        countS = defaultdict(int)
        have = 0
        for ch in t:
            countT[ch] += 1
        need = len(countT)
        for r in range(len(s)):
            countS[s[r]] += 1
            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                dist = r - l + 1
                if dist < shortest:
                    shortest = min(shortest, dist)
                    shortr = r
                    shortl = l
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        if shortr != -1:
            return s[shortl:shortr + 1]
        else:
            return ""

            

        