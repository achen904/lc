class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #like the coin change problem
        #create a dp array of len(s) then try to make
        #substrings of s using wordDict, if a substring can be
        #created then we set the dp array at i (where the substring starts)
        #dp[i] = True. in the end if dp[0] == True then the s can be made out of wordDict

        #initialize array
        dp = [False] * (len(s) + 1)

        #base case
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i:i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]: #if we already found a valid decomp of the substring starting at i we don't need to search anymore
                    break
    
        return dp[0]
