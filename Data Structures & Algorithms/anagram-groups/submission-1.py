class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lists = defaultdict(list)
        for word in strs:
            arr = [0] * 26
            for ch in word:
                index = ord(ch) - ord('a')
                arr[index] += 1
            lists[tuple(arr)].append(word)
        return list(lists.values())
            