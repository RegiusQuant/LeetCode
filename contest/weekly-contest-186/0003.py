# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 下午2:36
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

from typing import List
from collections import defaultdict, deque


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        record = defaultdict(deque)

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                record[i + j].appendleft(nums[i][j])

        result = []
        for k in sorted(record.keys()):
            while record[k]:
                result.append(record[k].popleft())
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(solution.findDiagonalOrder([[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]))
    print(solution.findDiagonalOrder([[1, 2, 3], [4], [5, 6, 7], [8], [9, 10, 11]]))
    print(solution.findDiagonalOrder([[1, 2, 3, 4, 5, 6]]))
