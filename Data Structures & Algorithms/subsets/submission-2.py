class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #use backtracking to get all subsets
        ans = []
        cur = []
        def backtrack(i):
            if i == len(nums): #base case when we finished iterating the entire array, we append our result to the output and return
                ans.append(cur.copy())
                return
            cur.append(nums[i]) #add the value at nums[i] then backtrack with this
            backtrack(i + 1)
            cur.pop() #remove the value we just added and continue backtracking
            backtrack(i + 1)
        backtrack(0)
        return ans