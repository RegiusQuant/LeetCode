# -*- coding: utf-8 -*-
# @Time    : 2020/6/21 上午10:19
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = start
        for i in range(1, n):
            result ^= start + 2 * i
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.xorOperation(5, 0))
    print(solution.xorOperation(4, 3))
    print(solution.xorOperation(1, 7))
    print(solution.xorOperation(10, 5))
