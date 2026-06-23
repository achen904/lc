class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.time = 0
        self.posts = defaultdict(list)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time += 1
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        check = self.following[userId]
        check.add(userId)
        for user in check:
            if self.posts[user]:
                time, tweetId = self.posts[user][-1]
                index = len(self.posts[user]) - 1
                heap.append((-time, index, tweetId, user))
        heapq.heapify(heap)
        ans = []
        while len(ans) < 10 and heap:
            time, index, tweetId, tweeterID = heapq.heappop(heap)
            ans.append(tweetId)
            if index > 0:
                newTime, newTweet = self.posts[tweeterID][index - 1]
                tup = (-newTime, index - 1, newTweet, tweeterID)
                heapq.heappush(heap, tup)
        return ans
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
