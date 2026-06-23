class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
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
        def backtrack(i, word):
            if len(word) == len(digits):
                ans.append(word)
                return
            for char in map[digits[i]]:
                backtrack(i + 1, word + char)
        backtrack(0, "")
        return ans
