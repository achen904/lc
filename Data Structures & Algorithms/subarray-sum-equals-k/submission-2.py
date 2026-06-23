class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #naive/brute force solution would be to check every subarray
        #and see if it sums up to k, which would take O(n^2)
        #A sliding window solution can do this in O(n), but
        #nums can contain negative values which means that
        #shrinking the window is not guaranteed to decrease
        #the sum and increasing the window doesn't increase the
        #sum. However, if we keep track of the prefix sums, then
        #we can figure the difference between our current sum and
        #k and check how many prefix sums leadning up to the current
        #sum give us that difference and we can "chop" off those
        #prefixes and we will have that sum
        counts = defaultdict(int)
        counts[0] = 1 #nothing in the array gives us a sum of 1
        cur = 0
        ans = 0
        for r in range(len(nums)):
            cur += nums[r]
            diff = cur - k #we do cur - k instead of k - cur because
            #we need to see how much we need to chop off of cur
            #to get to k
            ans += counts[diff]
            counts[cur] += 1
        return ans
            