class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #check the first word against everyword
        if not strs:
            return ""
        for index, char in enumerate(strs[0]):
            for i in range(1, len(strs)):
                if index >= len(strs[i]):
                    return strs[0][:index]
                if char != strs[i][index]:
                    return strs[0][:index]
        return strs[0]
#Runtime: m is the length of our first string and n is the number
#of strings in strs. then we are checking every character of our first
#string against every word at thaat same index which takes O(n*m)
#instead of appending to an ans, we return a splice of the string