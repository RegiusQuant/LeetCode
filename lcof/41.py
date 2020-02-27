# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 上午10:25
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 41.py
# @Desc    : 说明

import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.h1, self.h2 = [], []
        self.count = 0

    def addNum(self, num: int) -> None:
        if self.count == 0:
            heapq.heappush(self.h1, -num)
            self.count += 1
            return
        if num > -self.h1[0]:
            heapq.heappush(self.h2, num)
        else:
            heapq.heappush(self.h1, -num)
        while len(self.h1) - len(self.h2) > 1:
            x = -heapq.heappop(self.h1)
            heapq.heappush(self.h2, x)
        while len(self.h2) - len(self.h1) > 1:
            x = heapq.heappop(self.h2)
            heapq.heappush(self.h1, -x)
        self.count += 1

    def findMedian(self) -> float:
        if self.count == 0:
            return 0.
        elif self.count == 1:
            return -self.h1[0]
        elif self.count % 2 == 0:
            return (-self.h1[0] + self.h2[0]) / 2
        else:
            if len(self.h1) > len(self.h2):
                return -self.h1[0]
            else:
                return self.h2[0]


if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())

    obj = MedianFinder()
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())

    obj = MedianFinder()
    obj.addNum(-1)
    print(obj.findMedian())
    obj.addNum(-2)
    print(obj.findMedian())
    obj.addNum(-3)
    print(obj.findMedian())
    obj.addNum(-4)
    print(obj.findMedian())
    obj.addNum(-5)
    print(obj.findMedian())