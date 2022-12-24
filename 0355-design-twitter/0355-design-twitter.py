class Twitter:

    def __init__(self):
        self.count = 0
        self.twittermap = defaultdict(list)
        self.followmap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.twittermap[userId].append([self.count, tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heapmin = []
        heapq.heapify(heapmin)
        for post in self.twittermap[userId]:
            heapq.heappush(heapmin, post)
        for flwe in self.followmap[userId]:
            for post in self.twittermap[flwe]:
                heapq.heappush(heapmin, post)
        n = 0
        res = []
        while heapmin and n < 10:
            res.append(heapq.heappop(heapmin)[1])
            n += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)