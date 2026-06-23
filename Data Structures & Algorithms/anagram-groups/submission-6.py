from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for s in strs:
            temp = [0] * 26
            for ch in s:
                index = ord('a') - ord(ch)
                temp[index] += 1
            tup = tuple(temp)
            map[tup].append(s)
        ans = []
        for key in map:
            ans.append(map[key])
        return ans

