import heapq
from collections import deque
from collections import defaultdict


class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.t, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId] = self.tweets[userId][-10:]
        self.t -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        self.following[userId].add(userId)

        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                user_tweets = self.tweets[followeeId]
                idx = len(user_tweets) - 1

                time, tId = user_tweets[idx]
                heapq.heappush(tweets, (time, tId, followeeId, idx - 1))

        ans = []
        while tweets and len(ans) < 10:
            _, tId, followeeId, idx = heapq.heappop(tweets)
            ans.append(tId)
            if idx >= 0:
                time, tId = self.tweets[followeeId][idx]
                heapq.heappush(tweets, (time, tId, followeeId, idx - 1))

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)