# -*- coding: utf-8 -*-
# @Time    : 2020/2/17 上午10:31
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 15.py
# @Desc    : 说明

class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            n &= (n - 1)
            result += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.hammingWeight(9))
