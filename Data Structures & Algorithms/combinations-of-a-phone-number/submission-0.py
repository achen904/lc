class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = defaultdict(list)
        map["2"] = ["a", "b", "c"]
        map["3"] = ["d", "e", "f"]
        map["4"] = ["g", "h", "i"]
        map["5"] = ["j", "k", "l"]
        map["6"] = ["m", "n", "o"]
        map["7"] = ["p", "q", "r", "s"]
        map["8"] = ["t", "u", "v"]
        map["9"] = ["w", "x", "y", "z"]
        ans = []
        cur = []
        def backtrack(i):
            if cur and len(cur) == len(digits):
                ans.append("".join(cur.copy()))
                return
            for i in range(i, len(digits)):
                digit = digits[i]
                for char in map[digit]:
                    cur.append(char)
                    backtrack(i + 1)
                    cur.pop()
        backtrack(0)
        return ans
