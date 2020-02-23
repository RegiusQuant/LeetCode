# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 下午10:22
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

from typing import List


class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n, self.count = n, 0
        self.discount = discount
        self.id2Price = {i: price for i, price in zip(products, prices)}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total = 0.
        for i, num in zip(product, amount):
            total += self.id2Price[i] * num
        self.count += 1
        if self.count % self.n == 0:
            total = total - (1.0 * total * self.discount) / 100
        return total


if __name__ == '__main__':
    cashier = Cashier(3, 50, [1, 2, 3, 4, 5, 6, 7], [100, 200, 300, 400, 300, 200, 100])
    print(cashier.getBill([1, 2], [1, 2]))
    print(cashier.getBill([3, 7], [10, 10]))
    print(cashier.getBill([1, 2, 3, 4, 5, 6, 7], [1, 1, 1, 1, 1, 1, 1]))
