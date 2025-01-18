from collections import defaultdict
from typing import List
import time
import copy


class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.followings = defaultdict(set)
        self.newsfeed = defaultdict(lambda: defaultdict(list))

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.newsfeed[userId][userId].append([tweetId, time.time()])
        for follower in self.followers[userId]:
            self.newsfeed[follower][userId].append([tweetId, time.time()])

    def getNewsFeed(self, userId: int) -> List[int]:
        n = 0
        newsfeeds = []
        for feeds in self.newsfeed[userId].values():
            n += len(feeds)
            newsfeeds += feeds
        newsfeeds.sort(key=lambda x: x[1])

        return list(map(lambda x: x[0], newsfeeds[::-1][:10]))

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].add(followeeId)
        self.followers[followeeId].add(followerId)
        self.newsfeed[followerId][followeeId] = copy.deepcopy(self.newsfeed[followeeId][followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followings[followerId]:
            self.followings[followerId].remove(followeeId)
        if followerId in self.followers[followeeId]:
            self.followers[followeeId].remove(followerId)
        if self.newsfeed[followerId][followeeId]:
            del self.newsfeed[followerId][followeeId]


twitter = Twitter()
print(twitter.postTweet(1, 5))
print(twitter.postTweet(1, 3))
print(twitter.postTweet(1, 101))
print(twitter.postTweet(1, 13))
print(twitter.postTweet(1, 10))
print(twitter.postTweet(1, 2))
print(twitter.postTweet(1, 94))
print(twitter.postTweet(1, 505))
print(twitter.postTweet(1, 303))
print(twitter.getNewsFeed(1))
