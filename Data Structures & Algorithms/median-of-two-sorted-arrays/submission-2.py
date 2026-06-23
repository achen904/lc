class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #we want to find the index in which to split nums1
        #and num2 at where the left side of nums1 is less than
        #right side of nums2 and the left side of nums2 is less than
        #the right side of nums1 while having half of the elements
        #in the left splits.
        #Run binary search on the shorter array to prevent out of bounds
        #issues. if B is larger and we assign it the remaining values
        #that it will be fine
        A = []
        B = []
        if len(nums1) < len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1
        total = len(nums1) + len(nums2)
        half = total//2
        l, r = 0, len(A) - 1 #not setting r to half because half can be greater than len(nums1) or len(nums2)
        
        while True:
            mA = (l + r)//2
            mB = half - mA - 2
            Aleft, Aright = 0, 0
            Bleft, Bright = 0, 0
            if mA < 0:
                Aleft = -float('inf')
            else:
                Aleft = A[mA]
            if mA + 1 >= len(A):
                Aright = float('inf')
            else:
                Aright = A[mA + 1]
            if mB < 0:
                Bleft = -float('inf')
            else:
                Bleft = B[mB]
            if mB + 1>= len(B):
                Bright = float('inf')
            else:
                Bright = B[mB + 1]
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
            elif Aleft > Bright:
                r = mA - 1
            else:
                l = mA + 1

            

        