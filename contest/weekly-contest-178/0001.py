# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 上午10:08
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter, less = [0] * 101, [0] * 101
        for x in nums:
            counter[x] += 1
        for i in range(1, 101):
            less[i] = less[i - 1] + counter[i - 1]
        result = [less[x] for x in nums]
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
    print(solution.smallerNumbersThanCurrent([6, 5, 4, 8]))
    print(solution.smallerNumbersThanCurrent([7, 7, 7, 7]))
