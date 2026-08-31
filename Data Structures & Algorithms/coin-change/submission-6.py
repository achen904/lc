class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #BFS solution
        #starter node is 0 and finishing node is amount
        #each level of BFS is a coin used
        q = deque()
        q.append(0)
        ans = 0
        seen = set()
        if amount == 0:
            return 0
        while q:
            ans += 1
            n = len(q)
            for i in range(n):
                node = q.popleft()
                for coin in coins:
                    if coin + node <= amount and coin + node not in seen:
                        if node + coin == amount:
                            return ans
                        else:
                            q.append(node + coin)
                    seen.add(coin + node)

        return -1
