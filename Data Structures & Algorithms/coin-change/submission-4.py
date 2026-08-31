class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #top down approach
        #to know minimum number of coins to make amount we ask minimum to make amount - 1, amount -2, etc all the way down to amount = 0, which we know is 0
        memo = {}
        def dfs(i):
            if i == 0:
                return 0 #we know making 0 takes 0
            if i in memo:
                return memo[i] #we are doing dfs so if we already calcualted it we don't want to calculate it again and we return it
            res = amount + 1
            for coin in coins:
                if i - coin >= 0:
                    res = min(res, 1 + dfs(i - coin))
            memo[i] = res
            return res
        if dfs(amount) != amount + 1 :
            return dfs(amount) 
        else:
            return -1
