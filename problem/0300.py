# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 下午2:39
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0300.py
# @Desc    : 说明

import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        record = []
        for i in range(len(nums)):
            p = bisect.bisect_left(record, nums[i])
            if p == len(record):
                record.append(nums[i])
            else:
                record[p] = nums[i]
        return len(record)
