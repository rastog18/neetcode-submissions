class Twitter:

    def __init__(self):
        self.following = {}
        self.posts = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if self.posts.get(userId):
            self.posts[userId].appendleft((-self.time, tweetId))
        else:
            self.posts[userId] = deque([])
            self.posts[userId].append((-self.time, tweetId))
        self.time += 1

        return None

    def getNewsFeed(self, userId: int) -> List[int]:
        toRet = []
        heap = []
        heapq.heapify(heap)

        myPosts = self.posts.get(userId,)
        if myPosts:
            heapq.heappush(heap, (myPosts[0][0], myPosts[0][1], 0, userId))

        heFollows = self.following.get(userId)
        if heFollows:
            for fUserId in heFollows:
                posts = self.posts.get(fUserId)
                if posts:
                    element = (posts[0][0], posts[0][1], 0, fUserId)
                    heapq.heappush(heap, element)

        for i in range(10):
            if heap:
                timeStamp, tweet, index, fUserId = heapq.heappop(heap)
                toRet.append(tweet)
                index += 1
                if self.posts.get(fUserId) and len(self.posts.get(fUserId)) > index:
                    timeStamp, tweet = self.posts.get(fUserId)[index]
                    heapq.heappush(heap, (timeStamp, tweet, index, fUserId))
        return toRet


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return None
            
        if self.following.get(followerId):
            self.following[followerId].add(followeeId)
        else:
            self.following[followerId] = {followeeId}

        return None

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.following.get(followerId) and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

        return None
        
        
