class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for string in strs:
            ret += str(len(string)) + "#" + string
        return ret
    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            size = int(s[i:j])
            i = j + 1
            j = i + size
            ret.append(s[i:j])
            i = j
        return ret