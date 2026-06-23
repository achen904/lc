class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def contained(dic1, dic2):
            for key in dic1.keys():
                if dic2[key] < dic1[key]:
                    return False
            return True
        shortr = -1
        shortl = -1
        shortest = float('inf')
        l = 0
        countT = defaultdict(int)
        countS = defaultdict(int)
        for ch in t:
            countT[ch] += 1
        for r in range(len(s)):
            countS[s[r]] += 1
            while contained(countT, countS):
                dist = r - l + 1
                if dist < shortest:
                    shortest = min(shortest, dist)
                    shortr = r
                    shortl = l
                countS[s[l]] -= 1
                l += 1
        if shortr != -1:
            return s[shortl:shortr + 1]
        else:
            return ""

            

        