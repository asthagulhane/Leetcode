from collections import defaultdict

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)     # userId -> list of (time, tweetId)
        self.following = defaultdict(set)   # followerId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        # Start with the user's own tweets
        feed = list(self.tweets[userId])
        
        # Gather tweets from all followed users
        for followeeId in self.following[userId]:
            feed.extend(self.tweets[followeeId])
            
        # Sort by timestamp in descending order and take the top 10
        feed.sort(key=lambda x: x[0], reverse=True)
        return [tweetId for _, tweetId in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
