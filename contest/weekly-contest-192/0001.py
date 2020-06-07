# -*- coding: utf-8 -*-
# @Time    : 2020/6/7 下午9:54
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(len(nums) // 2):
            result.append(nums[i])
            result.append(nums[i + len(nums) // 2])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.shuffle([2, 5, 1, 3, 4, 7], 3))
