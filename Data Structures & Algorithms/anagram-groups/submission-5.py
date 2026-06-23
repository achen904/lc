from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for ch in word:
                index = ord(ch) - ord('a')
                key[index] += 1
            key = tuple(key)
            map[key].append(word)
        ret = []
        for key in map:
            ret.append(map[key])
        return ret        