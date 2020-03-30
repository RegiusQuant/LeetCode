# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 上午11:40
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.userDict = dict()
        self.pathDict = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.userDict[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, enterTime = self.userDict[id]
        del self.userDict[id]
        self.pathDict[(startStation, stationName)].append(t - enterTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.pathDict[(startStation, endStation)]) / len(self.pathDict[(startStation, endStation)])
