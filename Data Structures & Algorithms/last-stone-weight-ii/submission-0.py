class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        #i don't think most difficult part of this problem is reading it then determining that this is a 0/1 knapsack problem
        #when we smash 2 stones together, say a and b, the weight on the remaining stone is either going  |a - b|, then if we pick another 2 more stones say c and d we will have |c - d|. Without the abs, this can be represented in multiple ways a - b - (c - d) = a - b - c + d, or another way. The final stone weight is going to be all the stones that have a positive weight - stones that have a negative weight. To minimize the final stone weight, it equals the sum of the positives (above a and b)  minus the sum of negatives (above c and d), so we have to make both sums as close as possible. To do that we need to determine what the total weight of all the stones are then make each pile as close to half of the total. So conceptually if we pick 2 stones, the heavier stone goes into the positve pile and the lighter stone goes into the negative pile. 

        total = sum(stones)
        half = total // 2
        dp = [False] * (half + 1) #dp[i] tells us whether we can make of the piles have weight i
        dp[0] = True #base case, we don't put anything in positive pile
        for stone in stones:
            for i in range(len(dp) - 1, -1, -1):
                if i + stone < len(dp) and dp[i]:
                    dp[i + stone] = True
        closest = -1
        for i in range(len(dp) - 1, -1, -1):
            if dp[i]:
                closest = i
                break

        answer = total - (2 * closest)
        return answer