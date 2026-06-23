class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ans = 0
        arr = [0] * 26
        mostFrequent = 0
        for r in range(len(s)):
            index = ord(s[r]) - ord('A')
            arr[index] += 1
            if arr[index] > mostFrequent:
                mostFrequent = arr[index]
            NeedToChange = (r - l + 1) - mostFrequent
            while NeedToChange > k:
                arr[ord(s[l]) - ord('A')] -= 1
                l += 1
                NeedToChange = (r - l + 1) - mostFrequent
            ans = max(ans, r - l  +1)
        return ans
