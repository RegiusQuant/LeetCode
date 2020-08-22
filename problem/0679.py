# -*- coding: utf-8 -*-
# @Time       : 2020/08/22 23:15:06
# @Author     : RegiusQuant <315135833@qq.com>
# @Project    : LeetCode
# @File       : 0679.py
# @Description: 文件说明

from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6

        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if i == j:
                    continue
                temp = [z for k, z in enumerate(nums) if k != i and k != j]

                if self.judgePoint24(temp + [x + y]):
                    return True
                if self.judgePoint24(temp + [x * y]):
                    return True
                if self.judgePoint24(temp + [x - y]):
                    return True
                if abs(y) > 1e-6 and self.judgePoint24(temp + [x / y]):
                    return True
        return False
