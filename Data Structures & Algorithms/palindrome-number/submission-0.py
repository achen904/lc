class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Naive solution turn int to string then run palidrome while with 2 pointer
        word = str(x)
        l, r = 0, len(word) - 1
        while l <= r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True
        