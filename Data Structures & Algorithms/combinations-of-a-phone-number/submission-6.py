class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        map = {}
        map["2"] = "abc"
        map["3"] = "def"
        map["4"] = "ghi"
        map["5"] = "jkl"
        map["6"] = "mno"
        map["7"] = "pqrs"
        map["8"] = "tuv"
        map["9"] = "wxyz"   
        ans = []
        def backtrack(i, word):
            if len(word) == len(digits):
                ans.append(word)
                return
            for char in map[digits[i]]:
                backtrack(i+1, word + char)
        backtrack(0, "")
        return ans
                 