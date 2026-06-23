class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = [], []
        if len(nums1) < len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1
        total = len(A) + len(B)
        half = total //2
        l, r = 0, len(A) - 1
        while True:
            i = (l + r)//2
            j = half - i - 2
            Aleft, Aright, Bleft, Bright = -1, -1, -1, -1
            if i < 0:
                Aleft = float('-inf')
            else:
                Aleft = A[i]
            if i + 1 >= len(A):
                Aright = float('inf')
            else:
                Aright = A[i + 1]
            if j < 0:
                Bleft = float('-inf')
            else:
                Bleft = B[j]
            if j + 1 >= len(B):
                Bright = float('inf')
            else:
                Bright = B[j + 1]
            if Bleft <= Aright and Aleft <= Bright:
                if total % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
            else:
                if Aleft > Bright:
                    r = i - 1
                else:
                    l = i + 1
    