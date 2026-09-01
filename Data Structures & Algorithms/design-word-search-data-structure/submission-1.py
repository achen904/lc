class TrieNode:
    def __init__(self):
        self.children = {}
        self.last = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.last = True

    def search(self, word: str) -> bool:
        def dfs(ind, root):
            for i in range(ind, len(word)):
                ch = word[i]
                if ch == ".":
                    for child in root.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if ch not in root.children:
                        return False
                    root = root.children[ch]
            return root.last
        return dfs(0, self.root)
                    
        
