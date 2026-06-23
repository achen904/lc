class Solution:
    def isPalindrome(self, x: int) -> bool:
        #We can complete this in O(1) space without turning the 
        #number into a string
        if x < 0:
            return False
        if x == 0:
            return True
        #find number of digits in int
        checker = 1
        size = 0
        while x / checker >= 1:
            checker *= 10
            size += 1
        i = 0
        divide = 10 ** (size - 1)
        while x:
            if not x % 10 == x // divide:
                return False
            x = (x % divide) // 10
            divide /= 100
        return True
