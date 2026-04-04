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

        folwees_idxs = defaultdict(int)
        for f_id in self.user_follows[userId]:
            idx = len(self.user_posts[f_id]) - 1
            folwees_idxs[f_id] = idx
        folwees_idxs[userId] = len(self.user_posts[userId]) - 1 # добавим свои посты
        # print(folwees_idxs)
        
        flag = True
        while len(res) < 10 and flag:
            # print("while")
            flag = False # если ленты всех "блогеров" пусты
            most_relevant = -1
            most_rel_followee = None
            for f_id in folwees_idxs:
                idx = folwees_idxs[f_id]
                if  idx >= 0: # если у "блогера" есть посты
                    flag = True
                else:
                    continue
                
                if self.user_posts[f_id][idx][0] > most_relevant: #
                    most_relevant = self.user_posts[f_id][idx][0]
                    most_rel_followee = f_id
            if most_rel_followee:
                idx = folwees_idxs[most_rel_followee] # !!!!!
                post = self.user_posts[most_rel_followee][idx]
                folwees_idxs[most_rel_followee] -= 1
                res.append(post[1]) 
            # print("end-while")

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