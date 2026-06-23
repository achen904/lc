class Solution:
    def longestPalindrome(self, s: str) -> str:
        #check if each is a palindrome
        def isPalindrome(word):
            l,r = 0, len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True
        ans = ""
        for i in range(len(s)):
            j = len(s)
            while j > i:
                if j - i > len(ans) and isPalindrome(s[i:j]):
                    ans = s[i:j]
                j -= 1
        return ans

