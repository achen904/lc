class Solution:
    def climbStairs(self, n: int) -> int:
        #The number of ways to reach step n
        #is equal to the number of ways to reach
        #(n - 1) + (n - 2)
        #base case n = 1 and n = 2
        twoBack = 1 #one way to get to step 1: + 1
        oneBack = 2 #two ways to get to step 2 : 1 + 1, +2

        if n == 1:
            return 1
        if n == 2:
            return 2
        
        for _ in range(3, n):
            newStep = oneBack + twoBack
            twoBack = oneBack
            oneBack = newStep
        
        return oneBack + twoBack
            