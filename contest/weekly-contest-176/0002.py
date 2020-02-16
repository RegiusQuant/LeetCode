# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 上午10:35
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明


class ProductOfNumbers:

    def __init__(self):
        self.currProduct = 1
        self.lastZero = -1
        self.helper = []

    def add(self, num: int) -> None:
        self.currProduct *= num
        self.helper.append(self.currProduct)
        if self.currProduct == 0:
            self.lastZero = len(self.helper) - 1
            self.currProduct = 1

    def getProduct(self, k: int) -> int:
        if len(self.helper) - k <= self.lastZero:
            return 0
        else:
            if k == len(self.helper) or self.helper[-k - 1] == 0:
                return self.helper[-1]
            else:
                return self.helper[-1] // self.helper[-k - 1]


if __name__ == '__main__':
    pon = ProductOfNumbers()
    pon.add(3)
    pon.add(0)
    pon.add(2)
    pon.add(5)
    pon.add(4)
    print(pon.getProduct(2))
    print(pon.getProduct(3))
    print(pon.getProduct(4))
    print(pon.getProduct(5))
    pon.add(8)
    print(pon.getProduct(2))
    print(pon.getProduct(6))

    pon = ProductOfNumbers()
    pon.add(1)
    print(pon.getProduct(1))
