class Solution:
    def climbStairs(self, n: int) -> int:
        #if we do recurion, it is going take 2^n since we have 2 decisions to make for n different numbers
        #However, we can realize that instead of computing everything from the 
        #beginning for every number, we can use our previously computed results
        #For example, to get to step 3, we must have came from step 2 or came from step 1
        #so that means the number of ways to get to step 3 is the sum of ways we can
        #get to step 1 + ways we can get to step 2
        twoBack = 1
        oneBack = 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in range(3, n):
            temp = oneBack + twoBack
            twoBack = oneBack
            oneBack = temp
        return oneBack + twoBack
        #Now we realize that we only use the previous 2 computed results
        #and we only need to store 2 values, the previous value, and value before that one
        
