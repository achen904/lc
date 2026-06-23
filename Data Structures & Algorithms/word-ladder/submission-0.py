class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        connections = defaultdict(list)
        modifications = defaultdict(list)
        for i in range(len(beginWord)):
            word = ""
            word += beginWord[0:i]
            word += "*"
            word += beginWord[i + 1:]
            connections[word].append(beginWord)
            modifications[beginWord].append(word)
        for wrd in wordList:
            for i in range(len(beginWord)):
                word = ""
                word += wrd[0:i]
                word += "*"
                word += wrd[i + 1:]
                connections[word].append(wrd)
                modifications[wrd].append(word)
        seen = set()
        q = deque()
        q.append(beginWord)
        count = 1
        while q:
            n = len(q)
            for _ in range(n):
                word = q.popleft()
                seen.add(word) #real word
                if word == endWord:
                    return count
                mods = modifications[word]
                for mod in mods:
                    for neighbor in connections[mod]:
                        if neighbor not in seen:
                            q.append(neighbor)
            count += 1
        return 0




    
        
            