class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []
        l = r = 0
        while r < len(nums):
            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()
            dq.append(r)
            if dq[0] < l:
                dq.popleft()
            if r + 1>= k:
                ans.append(nums[dq[0]])
                l += 1
            r+= 1
        return ans