class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        neighbors = defaultdict(list)
        modifications = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                mod = word[:i]
                mod += "*"
                mod += word[i + 1:]
                neighbors[mod].append(word)
                modifications[word].append(mod)
        for i in range(len(beginWord)):
            mod = beginWord[:i]
            mod += "*"
            mod += beginWord[i + 1:]
            neighbors[mod].append(beginWord)
            modifications[beginWord].append(mod)
        q = deque()
        seen = set()
        seen.add(beginWord)
        q.append(beginWord)
        ans = 0
        while q:
            n = len(q)
            ans += 1
            for i in range(n):
                node = q.popleft()
                if node == endWord:
                    return ans
                for mod in modifications[node]:
                    for neighbor in neighbors[mod]:
                        if neighbor not in seen:
                            q.append(neighbor)
                            seen.add(neighbor)
        return 0



        