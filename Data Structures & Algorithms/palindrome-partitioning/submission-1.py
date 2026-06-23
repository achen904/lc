#have 2 pointers, one gives the starting index of substring and the other we will
#iterate to be the ending index of a substring
#once our starting index reaches the end of the string we have completed partitioning
#can use a helper to determine if our substring is a palindrome
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        cur = []
        def isPalindrome(word):
            l, r = 0, len(word) - 1
            while l <= r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True
        def backtrack(i, j):
            if i == len(s):
                ans.append(cur.copy())
                return
            for j in range(j, len(s) + 1):
                if isPalindrome(s[i:j]):
                    cur.append(s[i:j])
                    backtrack(j, j+1)
                    cur.pop()
        backtrack(0, 1)
        return ans