class Twitter:

    #tweets are composed of userIds and tweetIds

    def __init__(self):
        #list of tuples (tweetNo, userId, tweetId) for all tweets
        self.tweets = []
        #dictionary mapping userId to following
        self.users = {}
        #time counter
        self.count = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((-self.count, userId, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        #if not following anyone, 
        self.tweets.sort()
        if not userId in self.users:
            self.users[userId] = set()
            self.users[userId].add(userId)
        res = [x[2] for x in self.tweets if x[1] in self.users[userId] or x[1] == userId]
        print(res)
        return res[0:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            self.users[followerId].add(followeeId)
        else:
            self.users[followerId] = set()
            self.users[followerId].add(followeeId)
    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users and followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)

        
