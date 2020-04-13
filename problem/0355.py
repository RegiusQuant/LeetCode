# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 上午10:10
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0355.py
# @Desc    : 说明

from typing import List
from collections import defaultdict


class User:

    def __init__(self):
        self.followee = set()
        self.tweet = []


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.tweet2Time = defaultdict(int)
        self.user = defaultdict(User)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.user[userId].tweet.append(tweetId)
        self.time += 1
        self.tweet2Time[tweetId] = self.time

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.user:
            return []
        result = self.user[userId].tweet[-10:]
        for f in self.user[userId].followee:
            result.extend(self.user[f].tweet[-10:])
        result.sort(key=lambda x: self.tweet2Time[x], reverse=True)
        return result[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            self.user[followerId].followee.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            self.user[followerId].followee.discard(followeeId)
