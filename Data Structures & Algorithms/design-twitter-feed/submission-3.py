class Twitter:

    def __init__(self):
        self.user_follows = defaultdict(set)
        # self.user_feed = defaultdict(collections.deque)
        self.user_posts = defaultdict(list)
        self.tweetCount = 0

        
    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = (self.tweetCount, tweetId)
        self.tweetCount += 1
        self.user_posts[userId].append(tweet)


    def getNewsFeed(self, userId: int) -> List[int]:
        # print("-----")
        res = []

        maxHeap = []
        self.user_follows[userId].add(userId)

        for f_id in self.user_follows[userId]:
            idx = len(self.user_posts[f_id]) - 1
            if idx >= 0:
                count, postId = self.user_posts[f_id][idx]
                maxHeap.append((count, postId, f_id, idx))
        heapq.heapify_max(maxHeap)

        while len(res) < 10 and maxHeap:
            count, postId, f_id, idx = heapq.heappop_max(maxHeap)
            res.append(postId)
            if idx > 0:
                count, postId = self.user_posts[f_id][idx - 1]
                heapq.heappush_max(maxHeap, (count, postId, f_id, idx - 1))
        return res

        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.user_follows[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].discard(followeeId)




# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)