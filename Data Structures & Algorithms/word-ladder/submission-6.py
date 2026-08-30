class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #run a BFS from beginWord to see if we can get to endWord
        #build a modifications dictionary where we map each word to its possible modifications, but instead of changing every character to another we change a character in a word to *
        #we have build another dictionary that maps a modification to the possible real words so that we add these possible words to a queue as a connection from the starting word
        modifications = defaultdict(list) #word : mods
        words = defaultdict(list) #mod : words

        for i in range(len(beginWord)):
            mod = beginWord[:i]
            mod += "*"
            mod += beginWord[i + 1:]
            modifications[beginWord].append(mod)
            words[mod].append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                mod = word[:i]
                mod += "*"
                mod += word[i + 1:]
                modifications[word].append(mod)
                words[mod].append(word)
        seen = set()
        q = deque()
        q.append(beginWord)
        ans = 0
        while q:
            ans += 1
            n = len(q)
            for i in range(n):
                word = q.popleft()
                if word == endWord:
                    return ans
                for mod in modifications[word]:
                    for connect in words[mod]:
                        if connect not in seen:
                            seen.add(connect)
                            q.append(connect)
        return 0