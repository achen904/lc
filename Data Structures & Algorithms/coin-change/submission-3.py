class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #greedy solution will not work for this problem
            #ex: need 13: coins[10, 1, 6]
            #greedy wil take the 10 then 3 1s = 4 coins
            #optimal will take 6 + 6 + 1 = 3 coins
        #I think a bottom up dp approach can work where we determine the least amount of coins we can use to make amounts from 0 to amount
        dp = [amount + 1] * (amount + 1) 
        #initialize dp where dp represents the fewest number of coins required to make dp
        dp[0] = 0 #base case, no coins needed to make 0
        #iterate through amount with a nested iteration of coins to see if we can make that amount with our set of coins
        for amnt in range(1, amount + 1):
            for coin in coins:
                if amnt - coin >= 0 and dp[amnt] > dp[amnt - coin] + 1:
                    dp[amnt] = dp[amnt - coin] + 1
        if dp[amount] == amount + 1:
            return -1
        return dp[-1]