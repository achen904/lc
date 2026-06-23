class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = 0
        for i in range(m, len(nums1)):
            nums1[i] = nums2[k]
            k += 1
        for i in range(m, len(nums1)):
            j = i
            while j >0 and nums1[j] < nums1[j-1]:
                nums1[j], nums1[j-1] = nums1[j-1], nums1[j]
                j -= 1
        

