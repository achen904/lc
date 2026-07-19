class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #create a dp array where each index gives the minimum
        #number of coins needed to make change for the amount i
        #we can initialize value at each index to be amount + 1 since
        #the minimum value for a coin is 1 so there can't be more than
        #amount + i coins as the minimum to create change so that means
        #at the end of the algo if dp[amount + 1] == amount + 1 we return
        #-1 since there isn't a valid configuration to make it

        #initialize array
        dp = [amount + 1] *(amount + 1)
        #base case dp[0] = 0
        dp[0] = 0
        #iterate through each amount and each coin
        #we have amount on the other loop since we are doing bottom up dp

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] if dp[amount] <= amount else -1