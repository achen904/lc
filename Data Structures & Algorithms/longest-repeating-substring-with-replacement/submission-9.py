class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ans = 0
        arr = [0] * 26
        for r in range(len(s)):
            index = ord(s[r]) - ord('A')
            arr[index] += 1
            mostFrequentVal = 0
            mostFrequentIndex = 0
            for i, num in enumerate(arr):
                if num > mostFrequentVal:
                    mostFrequentVal = num
                    mostFrequentIndex = i
            NeedToChange = (r - l + 1) - mostFrequentVal
            while NeedToChange > k:
                arr[ord(s[l]) - ord('A')] -= 1
                l += 1
                mostFrequentVal = max(arr)
                NeedToChange = (r - l + 1) - mostFrequentVal
            ans = max(ans, r - l  +1)
        return ans
