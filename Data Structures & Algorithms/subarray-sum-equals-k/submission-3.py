class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #sliding window does not work because of potential negatives
        #instead keep track of prefix sums
        #then diff from running sum to see if we can make k

        prefixCounts = defaultdict(int)
        prefixCounts[0] = 1
        cur = 0
        ans = 0

        for num in nums:
            cur += num
            diff = cur - k
            ans += prefixCounts[diff]
            prefixCounts[cur] += 1
        return ans