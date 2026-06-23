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
        cur = []
        def backtrack(i):
            if len(cur) == len(digits):
                ans.append("".join(cur.copy()))
                return
            for char in map[digits[i]]:
                cur.append(char)
                backtrack(i+1)
                cur.pop()
        backtrack(0)
        return ans
                 