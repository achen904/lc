class Solution:
    def numDecodings(self, s: str) -> int:
        dp, dp1, dp2 = 0, 1, 0
        n = len(s)
        for i in range(n - 1, -1, -1):
            #if the current number is 0 then we can't make any letters
            if s[i] == "0":
                dp = 0
            else:
                dp = dp1

            if i + 1  < n and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                dp += dp2
            dp, dp1, dp2 = 0, dp, dp1
        return dp1