# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 上午10:27
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -k - 1
        for i in range(len(nums)):
            if nums[i] == 1:
                if i - prev - 1 < k:
                    return False
                prev = i
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.kLengthApart([1, 0, 0, 0, 1, 0, 0, 1], 2))
    print(solution.kLengthApart([1, 0, 0, 1, 0, 1], 2))
    print(solution.kLengthApart([1, 1, 1, 1, 1], 0))
    print(solution.kLengthApart([0, 1, 0, 1], 1))
