class Solution:
    def climbStairs(self, n: int) -> int:
        #if we do recurion, it is going take 2^n since we have 2 decisions to make for n different numbers
        #However, we can realize that instead of computing everything from the 
        #beginning for every number, we can use our previously computed results
        #for example the number of different ways to get to 3 is the same as 
        #the number of ways to get to 2 + the number of ways to get to 3 from 2
        #this means we can solve this problem with dynamic programming
        DP = [0] * (n + 1)
        DP[1] = 1
        if n == 1:
            return 1
        DP[2] = 2
        if n == 2:
            return 2
        for i in range(3, n + 1):
            DP[i] = DP[i - 1] + DP[i -2]
        return DP[n]
        
