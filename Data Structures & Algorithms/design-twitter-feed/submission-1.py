class Twitter:

    def __init__(self):
        self.user_follows = defaultdict(set)
        # self.user_feed = defaultdict(collections.deque)
        self.user_posts = defaultdict(list)
        self.tweetCount = 0

        
    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = (self.tweetCount, tweetId)
        self.tweetCount += 1

        heapq.heappush_max(self.user_posts[userId],tweet)
        # добавляем себе в ленту
        # if len(self.user_feed[userId]) > 9:
        #     self.user_feed[userId].pop()
        #     self.user_feed[userId].appendleft(tweet)
        # else:
        #     self.user_feed[userId].appendleft(tweet)
        
        # # добавляем в ленту подписчикам
        # followers = self.user_followers[userId]
        # for f in followers:
        #     if len(self.user_feed[f]) > 9:
        #         self.user_feed[f].pop()
        #         self.user_feed[f].appendleft(tweet)
        #     else:
        #         self.user_feed[f].appendleft(tweet)


    def getNewsFeed(self, userId: int) -> List[int]:
        # print("-----")
        
        res = []


        copy_folwees_posts = defaultdict(list)
        for f_id in self.user_follows[userId]:
            copy_folwees_posts[f_id] = self.user_posts[f_id].copy()
        copy_folwees_posts[userId] = self.user_posts[userId].copy() # добавим свои посты

        # print(copy_folwees_posts.keys())
        # print(copy_folwees_posts[userId])
        
        flag = True
        while len(res) < 10 and flag:
            # print("while")
            flag = False # если ленты всех "блогеров" пусты
            most_relevant = -1
            most_rel_followee = None
            for f_id in copy_folwees_posts.keys():
                if len(copy_folwees_posts[f_id]) > 0: # если у "блогера" есть посты
                    flag = True
                else:
                    # print(f"{f_id} - постов нет лох")
                    continue
                # print(copy_folwees_posts[f_id][0])
                # print(most_relevant)
                
                if copy_folwees_posts[f_id][0][0] > most_relevant: # [0] - вершина кучи, [0] - счётчик 
                    most_relevant = copy_folwees_posts[f_id][0][0]
                    most_rel_followee = f_id
            if most_rel_followee:
                # print(len(copy_folwees_posts[most_rel_followee]))
                post = heapq.heappop_max(copy_folwees_posts[most_rel_followee])
                # print(post)
                res.append(post[1]) 
            # print("end-while")
            # if not flag:
            #     break
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