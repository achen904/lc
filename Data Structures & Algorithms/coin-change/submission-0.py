class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #lets say we start at coins[0]
        #we can either choose to use it or skip it
            # if we choose to use it:
                #amount = amount - coins[i]
                #used = used + 1
                #then we can choose to use it again or move on
            #skip it
                #amount ; unchanged
                #used ; unchaged
        #dp[i] gives min coins to make i 
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        #loop through every i from 1 up to amount
        #while starting from 1:
            #loop through every coin to see check the min number of ways
            #to make the current amount i - coin value
        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])
        return dp[amount] if dp[amount] != (float('inf')) else -1