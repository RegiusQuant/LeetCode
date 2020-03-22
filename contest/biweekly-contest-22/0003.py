# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 下午10:29
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

def calStep(x):
    step = 0
    while x != 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
        step += 1
    return step


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        temp = list(range(lo, hi + 1))
        temp.sort(key=lambda x: (calStep(x), x))
        return temp[k - 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.getKth(7, 11, 4))
    print(solution.getKth(10, 20, 5))
    print(solution.getKth(1, 1000, 777))
