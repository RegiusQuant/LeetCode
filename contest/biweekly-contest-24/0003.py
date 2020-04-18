# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 下午10:22
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

class Solution:
    def __init__(self):
        self.count = 0
        self.result = ''

    def getHappyString(self, n: int, k: int) -> str:
        self.helper('', n, k)
        return self.result

    def helper(self, s, n, k):
        if len(s) == n:
            self.count += 1
            if self.count == k:
                self.result = s
            return

        if self.count == k:
            return
        for c in ['a', 'b', 'c']:
            if s == '' or s[-1] != c:
                self.helper(s + c, n, k)


if __name__ == '__main__':
    solution = Solution()
    print(solution.getHappyString(1, 3))

    solution = Solution()
    print(solution.getHappyString(1, 4))

    solution = Solution()
    print(solution.getHappyString(3, 9))

    solution = Solution()
    print(solution.getHappyString(2, 7))

    solution = Solution()
    print(solution.getHappyString(10, 100))