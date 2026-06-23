class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Naive solution, create a new array and find the middle value
        #takes m + n time where m is the len of nums 1 and n len of nums2
        #Instead we can run a binary search of how much of the first k
        #numbers to take from nums1 and nums2 since we know that the 
        #median is the middle of the 2 combined
        #Example nums1 = [1, 3, 5, 7] nums2 = [1, 2, 4, 5]
        #Combined [1, 1, 2, 3, 4, 5, 5, 7], 3.5 is median
        #since the total number elements is 8, we know that the median
        #is the average of the 4th and 5th in the sorted
        #That means if we can find the first half of the sorted
        #then we know the median. We can use binary search to find the first
        #half by seeing if the first total//2 elements of a combined nums1 and nums2 to work
        A, B = [], []
        if len(nums1) < len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1
        #we do the above because we want to know the smaller array
        #so that when we run binary search we don't run into out of bounds errors
        l, r = 0, len(A) - 1
        total = len(A) + len(B)
        half = total//2
        while True:
            mA = (l + r)//2
            mB = half - mA - 2 #the -2 is because of zero based index, but we used 1 based for the total and half so we account for it
            Aleft, Aright, Bleft, Bright = -1, -1, -1, -1
            #when creating the 2 sections of the arrays
            #we want the left section of one array to be <= right section of the other
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
            if mB + 1 >= len(B):
                Bright = float('inf')
            else:
                Bright = B[mB + 1]
            #We have a successful partition if the lefts are less than the opposing right
            if Aleft <= Bright and Bleft <= Aright:
                #odd length [1, 2] and [3]
                if total % 2 == 1:
                    #since we are doing floors, we take the right of our index
                    #we take the smaller right as it will be the middle
                    return min(Aright, Bright)
                #even length [1, 3], [2, 4]
                else:
                    #we take the average of the left and right
                    return (max(Aleft, Bleft) + min(Aright, Bright)) /2
            elif Aleft > Bright:
                #want less of A
                r = mA - 1
            else:
                #want more of A
                l = mA + 1
        
