class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr1 = [0] * 26
        arr2 = [0] * 26
        #create counts1
        for s in s1:
            index = ord(s) - ord('a')
            arr1[index] += 1
        l = 0
        for r in range(len(s2)):
            index = ord(s2[r]) - ord('a')
            arr2[index] += 1
            while r - l + 1 > len(s1):
                index = ord(s2[l]) - ord('a')
                arr2[index] -= 1
                l += 1
            if arr1 == arr2:
                return True
        return False
        