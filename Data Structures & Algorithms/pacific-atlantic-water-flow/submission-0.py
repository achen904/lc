class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = [[0] *(len(heights[0])) for _ in range(len(heights))]
        atlantic = [[0] *(len(heights[0])) for _ in range(len(heights))]
        directions = [(1,0), (-1,0), (0, 1), (0,-1)]
        qp = deque()
        qa = deque()
        ans = []
        def isValid(x,y):
            if not 0 <= x < len(heights):
                return False
            if not 0 <= y < len(heights[0]):
                return False
            return True
        for i in range(len(heights)):
            pacific[i][0] = 1
            qp.append((i, 0))
            atlantic[i][len(heights[0]) - 1] = 1
            qa.append((i, len(heights[0]) - 1))
        for i in range(len(heights[0])):
            pacific[0][i] = 1
            qp.append((0, i))
            atlantic[len(heights)- 1][i] = 1
            qa.append((len(heights) - 1, i))
        #run a BFS on pacific
        seenP = set()
        while qp:
            n = len(qp)
            for _ in range(n):
                x,y = qp.popleft()
                seenP.add((x,y))
                for dx, dy in directions:
                    nxt = (x + dx, y + dy)
                    if nxt not in seenP and isValid(x + dx, y + dy):
                        if heights[x + dx][y + dy] >= heights[x][y]:
                            pacific[x + dx][y + dy] = 1
                            qp.append((x + dx, y + dy))
        #run a BFS on atlantic
        seenA = set()
        while qa:
            n = len(qa)
            for _ in range(n):
                x,y = qa.popleft()
                seenA.add((x,y))
                for dx, dy in directions:
                    nxt = (x + dx, y + dy)
                    if nxt not in seenA and isValid(x + dx, y + dy):
                        if heights[x + dx][y + dy] >= heights[x][y]:
                            atlantic[x + dx][y + dy] = 1
                            qa.append((x + dx, y + dy))
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if pacific[i][j] == 1 and atlantic[i][j] == 1:
                    ans.append([i,j])
        return ans
        

