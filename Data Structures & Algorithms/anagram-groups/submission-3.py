class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            temp = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                temp[index] += 1
            tup = tuple(temp)
            groups[tup].append(word)
        ans = []
        for group in groups:
            ans.append(groups[group])
        return ans