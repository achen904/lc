class Solution:
#Naive solution: build a graph by finding every words neighbor
#This would involve, for each word, checking it against every other
#word and seeing if the characters differ by only one
#However, instead of doing that, we can for each word change one
#of its characters to *, then use that modified word as a parent
#and the word itself as child, that way if words differ by one character
#they would all fall under the same parent
#Now we can run BFS starting from beginWord and checking each one
#of its modifications to see which words share the same parent
#and this will allow us to move to that word in the graph
#if we reach the end word then we know a transformation is possible
#and we can track the count for each loop of our
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        connections = defaultdict(list)
        modifications = defaultdict(list)
        #loop through modifications for beginWord
        n = len(beginWord)
        for i in range(n):
            temp = ""
            temp += beginWord[0:i]
            temp += "*"
            temp += beginWord[i + 1:]
            connections[temp].append(beginWord)
            modifications[beginWord].append(temp)
        #loop through wordList and get its modifications
        for word in wordList:
            for i in range(n):
                temp = ""
                temp += word[0:i]
                temp += "*"
                temp += word[i + 1:]
                connections[temp].append(word)
                modifications[word].append(temp)
        #Run BFS from beginWord
        seen = set()
        q = deque()
        q.append(beginWord)
        count = 0
        while q:
            n = len(q)
            count += 1
            for _ in range(n):
                cur = q.popleft()
                seen.add(cur)
                #if cur is the same as endWord we prune early
                if cur == endWord:
                    return count
                #Go through each modification of cur
                #if its modification is in connections
                #that means it differs from a word by 1 char
                #and we can move to that word  
                mods = modifications[cur]
                for mod in mods:
                    for neighbor in connections[mod]:
                        if neighbor not in seen:
                            q.append(neighbor)
        return 0      