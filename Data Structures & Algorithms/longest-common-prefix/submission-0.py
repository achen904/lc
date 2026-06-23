class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #check the first word against everyword
        ans = ""
        if not strs:
            return ans
        for index, char in enumerate(strs[0]):
            for i in range(1, len(strs)):
                if index >= len(strs[i]):
                    return ans
                if char != strs[i][index]:
                    return ans
            ans += char
        return ans