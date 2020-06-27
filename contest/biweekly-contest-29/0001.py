# -*- coding: utf-8 -*-
# @Time    : 2020/6/27 下午9:55
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.average([4000, 3000, 1000, 2000]))
    print(solution.average([1000, 2000, 3000]))
    print(solution.average([6000, 5000, 4000, 3000, 2000, 1000]))
    print(solution.average([8000, 9000, 2000, 3000, 6000, 1000]))
