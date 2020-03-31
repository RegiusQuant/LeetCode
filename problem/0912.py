# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 上午10:13
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0912.py
# @Desc    : 说明

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        bucket = [0] * 110000
        for x in nums:
            bucket[x + 50000] += 1
        result = []
        for i in range(len(bucket)):
            for c in range(bucket[i]):
                result.append(i - 50000)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.sortArray([5, 2, 3, 1]))
    print(solution.sortArray([5, 1, 1, 2, 0, 0]))
