# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 上午9:43
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0295.py
# @Desc    : 说明

import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.h1 = []
        self.h2 = []

    def addNum(self, num: int) -> None:
        if not self.h1 or num <= -self.h1[0]:
            heapq.heappush(self.h1, -num)
        else:
            heapq.heappush(self.h2, num)

        if len(self.h1) > len(self.h2) + 1:
            x = -heapq.heappop(self.h1)
            heapq.heappush(self.h2, x)
        if len(self.h2) > len(self.h1):
            x = heapq.heappop(self.h2)
            heapq.heappush(self.h1, -x)

    def findMedian(self) -> float:
        if len(self.h1) > len(self.h2):
            return -self.h1[0]
        return (-self.h1[0] + self.h2[0]) / 2


if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())
