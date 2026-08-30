class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #run BFS from pacific and atalantic cells then iterate through all cells to see if there is a connection to both pacific and atalantic cells
        #use a set for both pacific and atlantic
        pacific = set()
        atlantic = set()
        pq = deque()
        aq = deque()

        #initialize both queues and sets
        for i in range(len(heights[0])):
            pacific.add((0, i))
            atlantic.add((len(heights) - 1, i))
            pq.append((0, i))
            aq.append((len(heights)- 1, i))
        for i in range(len(heights)):
            pacific.add((i, 0))
            pq.append((i, 0))
            atlantic.add((i, len(heights[0])- 1))
            aq.append((i, len(heights[0]) - 1))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seenp = set()

        #run BFS on pacific
        while pq:
            n = len(pq)
            for i in range(n):
                x, y = pq.popleft()
                seenp.add((x,y))
                for dx, dy in directions:
                    if 0 <= x + dx < len(heights) and 0 <= y + dy < len(heights[0]) and ((x + dx, y + dy)) not in seenp and heights[x + dx][y + dy] >= heights[x][y]:
                        pacific.add((x + dx, y + dy))
                        pq.append((x + dx, y + dy))
        seena = set()
        while aq:
            n = len(aq)
            for i in range(n):
                x, y = aq.popleft()
                seena.add((x,y))
                for dx, dy in directions:
                    if 0 <= x + dx < len(heights) and 0 <= y + dy < len(heights[0]) and ((x + dx, y + dy)) not in seena and heights[x + dx][y + dy] >= heights[x][y]:
                        atlantic.add((x + dx, y + dy))
                        aq.append((x + dx, y + dy))
        ans = []
        for x in range(len(heights)):
            for y in range(len(heights[0])):
                tup = (x,y)
                if tup in atlantic and tup in pacific:
                    ans.append([x,y])
        return ans
