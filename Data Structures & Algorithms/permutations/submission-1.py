class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #for this problem if we skip a number we must come back and get it later
        #so we must keep track if a number has been choosen
        #need to use a choosen list where each index corresponds to whether we have choosen it or not
        ans = []
        cur = []

        def backtrack(chosen):
            #base case is when our cur = len(nums)
            if len(cur) == len(nums):
                ans.append(cur.copy())
                return
            for i in range(len(nums)):
                if chosen[i]: #if this position is already used in cur continue
                    continue
                cur.append(nums[i])
                #mark it as chosen
                chosen[i] = True
                backtrack(chosen)
                cur.pop() #choose a different number for this position
                chosen[i] = False  #don't call backtrack again because we need this position filled in order to continue
        chosen = [False] *len(nums) #initialy no number is chosen
        backtrack(chosen)
        return ans
            