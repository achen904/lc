class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        connections = defaultdict(list)
        modifications = defaultdict(list)
        for i in range(len(beginWord)):
            mod = beginWord[:i]
            mod += "*"
            mod += beginWord[i + 1:]
            connections[mod].append(beginWord)
            modifications[beginWord].append(mod)
        for word in wordList:
            for i in range(len(word)):
                mod = word[:i]
                mod += "*"
                mod += word[i + 1:]
                connections[mod].append(word)
                modifications[word].append(mod)
        q = deque()
        seen = set()
        ans = 0
        q.append(beginWord)
        while q:
            n = len(q)
            ans += 1
            for _ in range(n):
                word = q.popleft()
                seen.add(word)
                if word == endWord:
                    return ans
                for modification in modifications[word]:
                    for connection in connections[modification]:
                        if connection not in seen:
                            q.append(connection)
        return 0
        