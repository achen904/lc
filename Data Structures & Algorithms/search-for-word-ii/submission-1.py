class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = -1
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i, word in enumerate(words):
            cur = root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.word = i
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ans = []
        def dfs(x, y, node):
            if node.word != -1:
               ans.append(words[node.word])
               node.word = -1
            for dx, dy in directions:
                if 0 <= x + dx < len(board) and 0 <= y + dy < len(board[0]) and board[x + dx][y + dy] != "#" and board[x + dx][y+ dy] in node.children:
                    temp = board[x + dx][y + dy]
                    board[x + dx][y + dy] = "#"
                    dfs(x + dx, y + dy, node.children[temp])
                    board[x+dx][y+dy] = temp
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] in root.children:
                    temp = board[x][y]
                    board[x][y] = "#"
                    dfs(x, y, root.children[temp])
                    board[x][y] = temp
        return ans
        